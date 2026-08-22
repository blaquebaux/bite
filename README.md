# Blaque Baux Bite

**Event-driven / merger arbitrage — the last uncorrelated-alpha hope. Tested: watered-down and crisis-correlated. An honest null.**

Bite is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Bite pointed that engine at the deal-spread
premium — and found the listed version thin and correlated where it needed to be fat and uncorrelated.

> **Not investment advice.** Educational/research software. Nothing here is validated to a live-money bar. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/bite.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Merger arbitrage: after a deal is announced, buy the target and capture the spread to close — you're paid
the **deal-break risk premium**. The hope: deal risk is **idiosyncratic**, not equity beta, so this could be
the genuinely uncorrelated alpha the family keeps looking for — the [bore](https://github.com/blaquebaux/bore)
pattern (a portable-alpha source), the one [bridge](https://github.com/blaquebaux/bridge) *wished* it was.
Testable via `MNA` (merger arb) and `CSD` (spin-offs). Honest prior from [bind](https://github.com/blaquebaux/bind):
the listed merger-arb ETF is "watered-down."

## The test — and the verdict: honest shelf

[`research/bite_1_eventdriven.py`](research/bite_1_eventdriven.py) — Alpaca SIP 2016–2026, fat-tail toolkit:

| instrument | Sharpe | CAGR | vol | maxDD | beta-SPY | skew | corr-SPY |
|---|---|---|---|---|---|---|---|
| merger arb (MNA) | +0.47 | +3% | 6.5% | −17% | +0.19 | **−2.36** | +0.50 |
| spin-offs (CSD) | +0.63 | +13% | 24.8% | −59% | **1.15** | −0.32 | +0.81 |
| SPY (reference) | +0.88 | +15% | 17.5% | −34% | 1.00 | −0.35 | 1.00 |

**Two ways it fails:**
- **MNA is watered-down.** Its Sharpe +0.47 is mostly the risk-free rate — the **excess over cash is +0.14
  Sharpe / +0.7%/yr**. The actual deal-spread premium is thin, and it carries a **−2.36 skew** (deals break
  in clusters — regulatory waves, bear markets) with a **crisis-corr of +0.70**: deals break *when equities
  fall*, so it's *not* the uncorrelated alpha we hoped. Ported onto SPY it fails (Jensen +0.1%, M² −0.4%).
- **CSD isn't event alpha at all** — beta 1.15, corr 0.81, −59% drawdown. Spin-offs are just high-beta
  small-cap equity wearing an event-driven label.

The real merger-arb edge — **single-deal selection, leverage, and access to deal flow** — is
private/unreplicable through a listed ETF (the same wall as [bind](https://github.com/blaquebaux/bind)'s
pod-shops). What's harvestable via `MNA` is the diluted, crisis-correlated residue.

## Status
**Research complete — an honest null; no live driver.** Merger arb via the listed ETF is a thin
(~0.7%/yr over cash), negatively-skewed (−2.36), crisis-correlated (+0.70) premium — not the uncorrelated
portable-alpha source it looked like, and the real edge (deal selection + leverage + access) is unreplicable.
Spin-offs (CSD) are just small-cap beta. On the record as rejected, with the reason — joins
brace/bridge/bounty/bear/backsliders/brute-force.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   _bite_common.py + bite_1_eventdriven.py (merger arb + spin-offs — concluded null) + scorecard
live/       (no driver — honest null)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
