"""Deal inputs: the 'blue cells' of the spreadsheet."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DealAssumptions:
    """Everything the model needs to know about a deal.

    Percentages are decimals (5% -> 0.05). Per-SF amounts are annual.
    """

    # Purchase
    purchase_price: float
    closing_cost_pct: float

    # Income
    building_sf: float
    rent_per_sf: float
    rent_growth: float
    vacancy_pct: float

    # Expenses
    opex_per_sf: float
    expense_growth: float
    capex_per_sf: float  # grows at expense_growth, like the spreadsheet

    # Financing (interest-only loan, repaid at sale)
    ltv: float
    interest_rate: float

    # Exit
    exit_cap_rate: float
    selling_cost_pct: float
    hold_years: int = 5

    def __post_init__(self) -> None:
        if self.purchase_price <= 0:
            raise ValueError("purchase_price must be positive")
        if self.building_sf <= 0:
            raise ValueError("building_sf must be positive")
        if self.exit_cap_rate <= 0:
            raise ValueError("exit_cap_rate must be positive")
        if not 0 <= self.ltv < 1:
            raise ValueError("ltv must be in [0, 1)")
        if not 0 <= self.vacancy_pct <= 1:
            raise ValueError("vacancy_pct must be in [0, 1]")
        if self.hold_years < 1:
            raise ValueError("hold_years must be at least 1")


# The example deal from CRE_Acquisition_Model.xlsx. Illustrative, not market data.
BASE_CASE = DealAssumptions(
    purchase_price=10_000_000,
    closing_cost_pct=0.015,
    building_sf=100_000,
    rent_per_sf=8.00,
    rent_growth=0.03,
    vacancy_pct=0.05,
    opex_per_sf=1.60,
    expense_growth=0.03,
    capex_per_sf=0.15,
    ltv=0.60,
    interest_rate=0.06,
    exit_cap_rate=0.065,
    selling_cost_pct=0.02,
)
