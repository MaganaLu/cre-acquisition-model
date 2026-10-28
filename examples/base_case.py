"""Run the example deal and print a summary like the spreadsheet's.

    uv run python examples/base_case.py
"""

from cre_underwriting import BASE_CASE, exit_cap_sensitivity, underwrite


def money(x: float) -> str:
    return f"(${-x:,.0f})" if x < 0 else f"${x:,.0f}"


def main() -> None:
    result = underwrite(BASE_CASE)
    cf, r = result.cash_flows, result.returns

    rows = [
        ("Net operating income", cf.noi),
        ("Unlevered cash flow", cf.unlevered),
        ("Levered cash flow", cf.levered),
    ]
    print(f"{'Year':<24}" + "".join(f"{y:>14}" for y in cf.years))
    for label, values in rows:
        print(f"{label:<24}" + "".join(f"{money(v):>14}" for v in values))

    print()
    print(f"Equity invested       {money(r.equity_invested)}")
    print(f"Total profit          {money(r.total_profit)}")
    print(f"Levered IRR           {r.levered_irr:.1%}")
    print(f"Equity multiple       {r.levered_equity_multiple:.2f}x")
    print(f"Unlevered IRR         {r.unlevered_irr:.1%}")
    print(f"Going-in cap rate     {r.going_in_cap_rate:.1%}")
    print(f"Year-1 cash-on-cash   {r.year1_cash_on_cash:.1%}")
    print(f"Year-1 DSCR           {r.year1_dscr:.2f}x")
    print(f"Debt yield            {r.debt_yield:.1%}")

    print("\nExit cap sensitivity")
    for cap, sr in exit_cap_sensitivity(BASE_CASE, [0.055, 0.06, 0.065, 0.07, 0.075]):
        print(f"  {cap:.1%}  IRR {sr.levered_irr:>6.1%}  multiple {sr.levered_equity_multiple:.2f}x")


if __name__ == "__main__":
    main()
