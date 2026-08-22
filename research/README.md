# Blaque Baux Bite — research

Is event-driven / merger arbitrage a genuine uncorrelated alpha (the bore pattern) or watered-down (bind's
prior)? `MNA` (merger arb), `CSD` (spin-offs) vs SPY, excess-over-cash (`BIL`). Read-only Alpaca SIP bars,
fat-tail toolkit + portable_alpha.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/bite_1_eventdriven.py
```

## Scorecard (2016-01 → 2026-07 SIP)

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Is merger arb (MNA) real, uncorrelated alpha? | Sharpe +0.47 but **excess-over-cash +0.14 / +0.7%/yr**; skew **−2.36**, crisis-corr **+0.70** | ❌ thin & crisis-correlated — watered-down (bind confirmed) |
| 2 | Are spin-offs (CSD) event alpha? | beta **1.15**, corr 0.81, maxDD −59% | ❌ just high-beta small-cap equity |
| 3 | Portable-alpha source? | MNA ported onto SPY fails — Jensen +0.1%, M² −0.4% | ❌ not the bore pattern |

## The synthesis

**The last uncorrelated-alpha hope, and it's diluted.** Merger arb *should* be idiosyncratic (deal-break
risk, not equity beta) — but the harvestable version (`MNA`) is thin over cash (~0.7%/yr), brutally negatively
skewed (−2.36, deals break in clusters), and **crisis-correlated (+0.70)** — deals break *when markets fall*,
so it isn't the uncorrelated stream we needed. The real edge — **single-deal selection, leverage, deal-flow
access** — is private/unreplicable through an ETF (bind's pod-shop wall). Spin-offs (`CSD`) aren't event alpha
at all, just small-cap beta.

So bite joins **brace/bridge/bounty** on the shelf — the fourth classic "harvestable/uncorrelated premium"
(sell-vol, pairs, carry, merger-arb) that, in listed-instrument form, is decayed, correlated, or too thin. The
only genuinely uncorrelated, portable-alpha source the family has found remains **bore** (crisis-corr −0.39).

## Status
**Research complete — an honest null; no live driver.** Listed merger arb is thin, negatively skewed, and
crisis-correlated — not the uncorrelated alpha it looked like; the real edge is unreplicable, and spin-offs are
just beta. On the record as rejected, with the reason.
