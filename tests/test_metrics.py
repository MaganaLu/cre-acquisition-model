import pytest

from cre_underwriting import equity_multiple, irr, npv


def test_npv_at_zero_rate_is_plain_sum():
    assert npv(0.0, [-100, 30, 80]) == pytest.approx(10)


def test_irr_one_period():
    # Invest 100, get 110 back a year later: 10%.
    assert irr([-100, 110]) == pytest.approx(0.10)


def test_irr_makes_npv_zero():
    flows = [-1000, 100, 100, 1100]
    assert npv(irr(flows), flows) == pytest.approx(0, abs=1e-6)


def test_irr_can_be_negative():
    assert irr([-100, 90]) == pytest.approx(-0.10)


def test_irr_raises_without_sign_change():
    with pytest.raises(ValueError):
        irr([100, 50])


def test_equity_multiple():
    assert equity_multiple([-100, 20, 130]) == pytest.approx(1.5)


def test_equity_multiple_requires_investment():
    with pytest.raises(ValueError):
        equity_multiple([100, 50])
