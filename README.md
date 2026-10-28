# cre-underwriting

A small, tested Python model for underwriting a commercial real estate acquisition: buy a building, hold it for a few years, sell it, and measure the return.

It's a code version of a spreadsheet model ([`tests/fixtures/CRE_Acquisition_Model.xlsx`](tests/fixtures/CRE_Acquisition_Model.xlsx)). The tests check that both produce the same numbers.

## What it does

Given a deal's assumptions (price, rent, expenses, loan, exit cap rate), it builds year-by-year cash flows and reports:

| Metric | Base case | What it means |
|---|---|---|
| Levered IRR | 7.6% | Annual return on the investor's equity, accounting for timing |
| Equity multiple | 1.40x | Dollars back per dollar invested |
| Unlevered IRR | 6.7% | Return of the building with no loan |
| Going-in cap rate | 6.0% | Year-1 NOI ÷ purchase price |
| Year-1 cash-on-cash | 5.4% | Year-1 cash to equity ÷ equity invested |
| Year-1 DSCR | 1.67x | NOI ÷ loan payments (lenders want ~1.25x+) |
| Debt yield | 10.0% | NOI ÷ loan amount |

It also runs an **exit cap sensitivity**, rerunning the whole model at different sale cap rates. That's usually the assumption that moves returns the most.

## How the model works

```
Assumptions
  └─ Gross potential rent − vacancy = Effective gross income
       └─ − operating expenses = NOI (net operating income)
            └─ − capex reserve − purchase + sale = Unlevered cash flow
                 └─ + loan − interest − repayment = Levered cash flow
                      └─ IRR, equity multiple, DSCR, ...
```

Key conventions:
- **Year 0** is the purchase date. Years 1..N are the hold.
- **Sale price = next year's NOI ÷ exit cap rate.** A buyer pays for the income they'll receive.
- **Capex sits below NOI**, so cap rates compare cleanly across buildings.
- **The loan is interest-only**, repaid in full at sale.

## Usage

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv run pytest                          # run the tests
uv run python examples/base_case.py    # print the base-case summary
```

```python
from dataclasses import replace
from cre_underwriting import BASE_CASE, underwrite

# What if rents grow 4% instead of 3%?
result = underwrite(replace(BASE_CASE, rent_growth=0.04))
print(f"{result.returns.levered_irr:.1%}")
```

Load assumptions straight from the spreadsheet:

```python
from cre_underwriting.excel import load_assumptions
deal = load_assumptions("tests/fixtures/CRE_Acquisition_Model.xlsx")
```

## Project layout

```
src/cre_underwriting/
  assumptions.py   # DealAssumptions: the inputs ("blue cells")
  model.py         # cash flows, returns, sensitivity
  metrics.py       # generic IRR / NPV / equity multiple math
  excel.py         # read inputs from the spreadsheet
tests/             # unit tests + spreadsheet comparison
examples/          # runnable scripts
```

## Roadmap

- [ ] Amortizing loans (principal paid down over time)
- [ ] Two-way sensitivity tables (e.g. price × exit cap)
- [ ] Monte Carlo simulation over uncertain assumptions
- [ ] Lease-by-lease rent roll for multi-tenant buildings
- [ ] Equity waterfall (preferred return, promote)

See [LEARNING.md](LEARNING.md) for the study plan this project is part of.

*Example inputs are illustrative, not market data.*
