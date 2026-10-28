from dataclasses import FrozenInstanceError, replace

import pytest

from cre_underwriting import BASE_CASE, exit_cap_sensitivity, underwrite


@pytest.fixture
def base():
    return underwrite(BASE_CASE)


def test_year1_noi(base):
    # 100,000 SF x $8 = $800k rent, minus 5% vacancy, minus $160k opex.
    assert base.cash_flows.noi[1] == pytest.approx(600_000)


def test_noi_grows_each_year(base):
    noi = base.cash_flows.noi
    assert noi[0] == 0
    assert all(later > earlier for earlier, later in zip(noi[1:], noi[2:]))


def test_sale_uses_forward_noi(base):
    cf = base.cash_flows
    assert cf.sale_price[-1] == pytest.approx(cf.forward_noi / BASE_CASE.exit_cap_rate)
    assert cf.forward_noi > cf.noi[-1]


def test_equity_is_price_plus_costs_minus_loan(base):
    assert base.returns.equity_invested == pytest.approx(10_150_000 - 6_000_000)


def test_headline_returns(base):
    r = base.returns
    assert r.levered_irr == pytest.approx(0.0762, abs=1e-4)
    assert r.unlevered_irr == pytest.approx(0.0668, abs=1e-4)
    assert r.levered_equity_multiple == pytest.approx(1.396, abs=1e-3)
    assert r.going_in_cap_rate == pytest.approx(0.06)
    assert r.year1_dscr == pytest.approx(600_000 / 360_000)
    assert r.debt_yield == pytest.approx(0.10)


def test_total_profit_is_sum_of_levered_flows(base):
    assert base.returns.total_profit == pytest.approx(sum(base.cash_flows.levered))


def test_all_cash_deal_has_identical_levered_and_unlevered_flows():
    result = underwrite(replace(BASE_CASE, ltv=0))
    assert result.cash_flows.levered == pytest.approx(result.cash_flows.unlevered)
    assert result.returns.levered_irr == pytest.approx(result.returns.unlevered_irr)


def test_higher_exit_cap_lowers_returns():
    irrs = [r.levered_irr for _, r in exit_cap_sensitivity(BASE_CASE, [0.055, 0.06, 0.065, 0.07, 0.075])]
    assert irrs == sorted(irrs, reverse=True)


def test_sensitivity_matches_spreadsheet_table():
    expected = {0.055: 0.1431, 0.06: 0.1090, 0.065: 0.0762, 0.07: 0.0444, 0.075: 0.0130}
    for cap, r in exit_cap_sensitivity(BASE_CASE, list(expected)):
        assert r.levered_irr == pytest.approx(expected[cap], abs=1e-4)


def test_hold_period_changes_number_of_years():
    result = underwrite(replace(BASE_CASE, hold_years=7))
    assert result.cash_flows.years == list(range(8))


@pytest.mark.parametrize("field, bad", [("purchase_price", 0), ("exit_cap_rate", 0), ("ltv", 1.2)])
def test_invalid_inputs_rejected(field, bad):
    with pytest.raises(ValueError):
        replace(BASE_CASE, **{field: bad})


def test_assumptions_are_immutable():
    with pytest.raises(FrozenInstanceError):
        BASE_CASE.purchase_price = 1  # type: ignore[misc]
