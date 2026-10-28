# Learning Plan: Commercial Real Estate Fundamentals

A 3-month, hands-on plan for learning CRE investing and asset management alongside this project. The loop: **watch someone build it → build it yourself without the video → apply it to a real deal.** Tick items off as you go.

## Weekly rhythm

| When | Activity | Time |
|---|---|---|
| Two weekday evenings | Watch one modeling video, then rebuild it without the video | 2 × 45 min |
| Weekend | Underwrite one real listing | 1–2 hrs |
| Monthly | A local industry event, or a deal review with a mentor | 1–2 hrs |

## Weeks 0–2: Prerequisites

The background you need before modeling. About 10–12 hours over 1–2 weeks. Each topic ends with a self-test: if you can answer it out loud, move on.

### 1. Time value of money (most important)
A dollar today is worth more than a dollar later, because you could invest it in the meantime. NPV and IRR are built on this.
- [ ] Watch: [Time value of money](https://www.youtube.com/watch?v=733mgqrzNKs) (Khan Academy)
- [ ] Watch: [Introduction to present value](https://www.youtube.com/watch?v=ks33lMoxst0) (Khan Academy)
- [ ] Watch: [Present Value 4 (and discounted cash flow)](https://www.youtube.com/watch?v=6WCfVjUTTEY) (Khan Academy)
- [ ] Watch: [Internal Rate of Return (IRR) Explained with Example](https://www.youtube.com/watch?v=tylBkAZMcFw) (EPM)
- [ ] Alternate IRR explainer: [What is IRR?](https://www.youtube.com/watch?v=Vw_K0DGAibE) (Ryan O'Connell, CFA)
- [ ] More practice: [Khan Academy: Interest and debt unit](https://www.khanacademy.org/economics-finance-domain/core-finance/interest-tutorial)
- [ ] **Self-test:** Why is $1M received in year 5 worth less than $1M today? What does it mean that a deal's IRR is 7.6%?

### 2. Accounting basics
Enough to understand revenue vs. expenses, and cash vs. profit.
- [ ] Watch: [Comparing accrual and cash accounting](https://www.khanacademy.org/v/comparing-accrual-and-cash-accounting) (Khan Academy)
- [ ] Watch: [Basic cash flow statement](https://www.khanacademy.org/economics-finance-domain/core-finance/accounting-and-financial-stateme/financial-statements-tutorial/v/basic-cash-flow-statement) (Khan Academy)
- [ ] More practice: [Khan Academy: Accounting and financial statements unit](https://www.khanacademy.org/economics-finance-domain/core-finance/accounting-and-financial-statements)
- [ ] **Self-test:** Why is a new roof (capex) treated differently from a monthly cleaning bill (opex)? Why can a profitable business run out of cash?

### 3. How loans work
Interest, principal, amortization, and why leverage magnifies returns.
- [ ] Watch: [Introduction to mortgage loans](https://www.khanacademy.org/v/introduction-to-mortgage-loans) (Khan Academy)
- [ ] More practice: [Khan Academy: Housing unit](https://www.khanacademy.org/economics-finance-domain/core-finance/housing) (mortgages, balloon payments)
- [ ] **Build:** a mortgage amortization table in Excel from scratch: yearly payment, interest, principal, remaining balance (use [PMT](https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441))
- [ ] **Self-test:** On a 30-year loan, why does most of the early payment go to interest? If a building yields 6% and the loan costs 7%, does borrowing help or hurt?

### 4. Real estate basics
Property types, lease types, and what cap rates mean.
- [ ] Skim: [A.CRE Glossary of Commercial Real Estate Terms](https://www.adventuresincre.com/glossary-commercial-real-estate-terms/) (look up cap rate, NOI, NNN lease, gross lease, absorption, Class A/B/C)
- [ ] Read: [Cap Rates, Explained](https://www.jpmorgan.com/insights/real-estate/commercial-term-lending/cap-rates-explained) (J.P. Morgan)
- [ ] Practice: [A.CRE cap rate mental math tool](https://www.adventuresincre.com/cap-rate/)
- [ ] **Self-test:** In a triple net (NNN) lease, who pays property taxes and insurance? If cap rates rise from 5% to 6% and NOI stays the same, what happens to value? (It falls about 17%.)

### 5. Excel skills
Learn these while rebuilding the model, not before.
- [ ] Read: [Relative, absolute, and mixed references](https://support.microsoft.com/en-us/office/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9) (`B5` vs `$B$5`)
- [ ] Read: [IRR function](https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc) and [XIRR function](https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d) (IRR with exact dates)
- [ ] Habits: inputs in one place, blue for inputs and black for formulas, no typed-in numbers inside formulas
- [ ] **Self-test:** Why does the model use `$B$7` in `=$B$7*$B$8*(1+$B$9)^(D$20-1)`?

### 6. A little economics
Why cap rates and values move.
- [ ] Read: [Cap Rates and Interest Rates](https://www.wallstreetprep.com/knowledge/cap-rates-and-interest-rates/) (Wall Street Prep)
- [ ] **Self-test:** When interest rates rise, why do property values usually fall? Why has e-commerce increased demand for warehouses?

## Month 1: Core concepts

**Watch**
- [ ] [A.CRE YouTube channel](https://www.youtube.com/@AdventuresinCRE): a basic acquisition model walkthrough
- [ ] Justin Kivel (Rockstar Financial): beginner CRE modeling videos

**Build**
- [ ] Rebuild the Excel model from a blank sheet, checking against [the original](tests/fixtures/CRE_Acquisition_Model.xlsx) only when stuck
- [ ] Explain in your own words: NOI, cap rate, IRR, equity multiple, DSCR, debt yield
- [ ] Change one input at a time in the model and predict the IRR before running it

**Real world**
- [ ] Underwrite your first real industrial listing (Crexi or LoopNet)
- [ ] Drive past it: note condition, loading docks, truck access, neighbors

## Month 2: Modeling and markets

**Watch**
- [ ] A.CRE YouTube: amortizing loans and lease-by-lease modeling
- [ ] Free sample videos from Breaking Into Wall Street or Wall Street Prep (decide if a paid course is worth it)
- [ ] Two Walker Webcast episodes on industrial real estate or interest rates

**Build**
- [ ] Project: add amortizing loans (write the tests first)
- [ ] Project: add a two-way sensitivity table (price × exit cap)
- [ ] Complete one A.CRE practice modeling test, timed

**Real world**
- [ ] Underwrite one listing per week
  - [ ] Week 1:
  - [ ] Week 2:
  - [ ] Week 3:
  - [ ] Week 4:
- [ ] Compare your assumptions to a CBRE, JLL, or Cushman & Wakefield industrial market report
- [ ] Look up 3 recent industrial sales in county assessor records and work out the cap rates they sold at

## Month 3: Think like an asset manager

**Watch**
- [ ] A.CRE YouTube: equity waterfall walkthrough
- [ ] A recorded ULI or NAIOP conference panel

**Build**
- [ ] Project: build an equity waterfall (preferred return, catch-up, promote)
- [ ] Model a value-add scenario: lease up vacant space or raise below-market rents

**Real world**
- [ ] Attend a local NAIOP or ULI event
- [ ] Mock deal: pitch one underwritten listing to a mentor as if to an investment committee, and ask them to push back
- [ ] Informational chats with people in asset or portfolio management
  - [ ] 1:
  - [ ] 2:
  - [ ] 3:
- [ ] Optional: buy a small position in an industrial REIT and read its quarterly report (for learning, not investment advice)

## Optional reading

Books go deeper than videos. Use them as references when something doesn't click.

- [ ] Frank Gallinelli, *What Every Real Estate Investor Needs to Know About Cash Flow* (best beginner book)
- [ ] Sean Cook, *Investing in Real Estate Private Equity* (fund structures, waterfalls)
- [ ] Peter Linneman, *Real Estate Finance and Investments: Risks and Opportunities*
- [ ] Geltner & Miller, *Commercial Real Estate Analysis and Investments* (reference textbook)
- [ ] MIT OpenCourseWare: *Real Estate Finance and Investment* lecture notes
- [ ] ULI/PwC *Emerging Trends in Real Estate* (annual)

## Later

- [ ] Pick one paid modeling course: A.CRE Accelerator, Breaking Into Wall Street, Wall Street Prep, or REFM
- [ ] ARGUS Enterprise certification (once actively applying for roles)
- [ ] Project: Monte Carlo simulation, lease-by-lease rent roll, portfolio dashboard

## Notes

Write down what surprised you, what confused you, and questions to bring to mentor conversations.

-
