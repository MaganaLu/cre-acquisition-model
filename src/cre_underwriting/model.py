"""The acquisition model: assumptions -> cash flows -> returns.

Mirrors CRE_Acquisition_Model.xlsx. Every list is indexed by year:
index 0 is the purchase date, 1..hold_years are the hold period.
"""

from dataclasses import dataclass, replace

from .assumptions import DealAssumptions
from .metrics import equity_multiple, irr


@dataclass(frozen=True)
class CashFlows:
    years: list[int]
    gross_potential_rent: list[float]
    vacancy_loss: list[float]  # negative
    effective_gross_income: list[float]
    operating_expenses: list[float]  # negative
    noi: list[float]
    capex_reserve: list[float]  # negative
    purchase: list[float]  # negative, year 0 only
    sale_price: list[float]  # positive, exit year only
    selling_costs: list[float]  # negative, exit year only
    unlevered: list[float]
    loan_proceeds: list[float]  # positive, year 0 only
    interest: list[float]  # negative
    loan_repayment: list[float]  # negative, exit year only
    levered: list[float]
    forward_noi: float  # NOI in the year after sale; what the next buyer pays for


@dataclass(frozen=True)
class Returns:
    equity_invested: float
    total_profit: float
    levered_irr: float
    levered_equity_multiple: float
    unlevered_irr: float
    going_in_cap_rate: float
    year1_cash_on_cash: float
    year1_dscr: float
    debt_yield: float


@dataclass(frozen=True)
class Underwriting:
    assumptions: DealAssumptions
    cash_flows: CashFlows
    returns: Returns


def _grown(base: float, growth: float, year: int) -> float:
    """Year-1 amount `base`, compounded at `growth` for each year after."""
    return base * (1 + growth) ** (year - 1)


def _noi(a: DealAssumptions, year: int) -> float:
    gpr = _grown(a.building_sf * a.rent_per_sf, a.rent_growth, year)
    opex = _grown(a.building_sf * a.opex_per_sf, a.expense_growth, year)
    return gpr * (1 - a.vacancy_pct) - opex


def build_cash_flows(a: DealAssumptions) -> CashFlows:
    n = a.hold_years
    years = list(range(n + 1))

    def by_year(fn) -> list[float]:
        """Apply fn to operating years 1..n; year 0 has no operations."""
        return [0.0] + [fn(y) for y in years[1:]]

    def at(year: int, amount: float) -> list[float]:
        """A one-time amount in a single year."""
        return [amount if y == year else 0.0 for y in years]

    gpr = by_year(lambda y: _grown(a.building_sf * a.rent_per_sf, a.rent_growth, y))
    vacancy = [-g * a.vacancy_pct for g in gpr]
    egi = [g + v for g, v in zip(gpr, vacancy)]
    opex = by_year(lambda y: -_grown(a.building_sf * a.opex_per_sf, a.expense_growth, y))
    noi = [e + o for e, o in zip(egi, opex)]
    capex = by_year(lambda y: -_grown(a.building_sf * a.capex_per_sf, a.expense_growth, y))

    # Exit: the next buyer values the building on the following year's NOI.
    forward_noi = _noi(a, n + 1)
    gross_sale = forward_noi / a.exit_cap_rate

    purchase = at(0, -a.purchase_price * (1 + a.closing_cost_pct))
    sale = at(n, gross_sale)
    selling = at(n, -gross_sale * a.selling_cost_pct)
    unlevered = [sum(parts) for parts in zip(noi, capex, purchase, sale, selling)]

    loan = a.purchase_price * a.ltv
    proceeds = at(0, loan)
    interest = by_year(lambda y: -loan * a.interest_rate)
    repayment = at(n, -loan)
    levered = [sum(parts) for parts in zip(unlevered, proceeds, interest, repayment)]

    return CashFlows(
        years=years,
        gross_potential_rent=gpr,
        vacancy_loss=vacancy,
        effective_gross_income=egi,
        operating_expenses=opex,
        noi=noi,
        capex_reserve=capex,
        purchase=purchase,
        sale_price=sale,
        selling_costs=selling,
        unlevered=unlevered,
        loan_proceeds=proceeds,
        interest=interest,
        loan_repayment=repayment,
        levered=levered,
        forward_noi=forward_noi,
    )


def compute_returns(a: DealAssumptions, cf: CashFlows) -> Returns:
    loan = cf.loan_proceeds[0]
    debt_service = -cf.interest[1]
    year1_cash_to_equity = cf.noi[1] + cf.capex_reserve[1] + cf.interest[1]
    equity = -cf.levered[0]

    return Returns(
        equity_invested=equity,
        total_profit=sum(cf.levered),
        levered_irr=irr(cf.levered),
        levered_equity_multiple=equity_multiple(cf.levered),
        unlevered_irr=irr(cf.unlevered),
        going_in_cap_rate=cf.noi[1] / a.purchase_price,
        year1_cash_on_cash=year1_cash_to_equity / equity,
        # With no loan there's no debt to cover, so these are undefined.
        year1_dscr=cf.noi[1] / debt_service if debt_service else float("inf"),
        debt_yield=cf.noi[1] / loan if loan else float("inf"),
    )


def underwrite(a: DealAssumptions) -> Underwriting:
    """Run the full model for one set of assumptions."""
    cf = build_cash_flows(a)
    return Underwriting(assumptions=a, cash_flows=cf, returns=compute_returns(a, cf))


def exit_cap_sensitivity(a: DealAssumptions, exit_caps: list[float]) -> list[tuple[float, Returns]]:
    """Rerun the whole model at each exit cap rate, holding everything else fixed."""
    return [(cap, underwrite(replace(a, exit_cap_rate=cap)).returns) for cap in exit_caps]
