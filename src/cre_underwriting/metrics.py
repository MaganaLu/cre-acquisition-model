"""Generic return math. Nothing here knows about real estate."""

from collections.abc import Sequence


def npv(rate: float, cash_flows: Sequence[float]) -> float:
    """Net present value, with cash_flows[0] at time 0 (not discounted).

    Note: Excel's NPV() assumes the first cash flow is one period out.
    This matches the convention IRR uses instead.
    """
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))


def irr(cash_flows: Sequence[float], low: float = -0.99, high: float = 10.0, tol: float = 1e-10) -> float:
    """Internal rate of return: the discount rate where NPV = 0.

    Uses bisection: slow but always converges once the answer is bracketed.
    Raises ValueError if NPV doesn't change sign between `low` and `high`
    (e.g. all cash flows are positive, so no rate makes NPV zero).
    """
    npv_low, npv_high = npv(low, cash_flows), npv(high, cash_flows)
    if npv_low * npv_high > 0:
        raise ValueError("IRR not found: NPV has the same sign at both ends of the search range")

    for _ in range(200):
        mid = (low + high) / 2
        npv_mid = npv(mid, cash_flows)
        if abs(npv_mid) < tol:
            return mid
        if npv_low * npv_mid < 0:
            high = mid
        else:
            low, npv_low = mid, npv_mid
    return (low + high) / 2


def equity_multiple(cash_flows: Sequence[float]) -> float:
    """Total cash returned / cash invested. Expects cash_flows[0] to be the (negative) investment."""
    if cash_flows[0] >= 0:
        raise ValueError("cash_flows[0] must be a negative investment")
    return sum(cash_flows[1:]) / -cash_flows[0]
