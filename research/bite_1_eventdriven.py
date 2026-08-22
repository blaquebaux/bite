#!/usr/bin/python3
# =============================================================================
# bite_1_eventdriven.py — is event-driven / merger-arb a genuine uncorrelated alpha, or watered-down?
#
# Merger arb (MNA) and spin-offs (CSD) vs SPY, with the fat-tail toolkit. The tests: (1) positive Sharpe,
# and how thin is the return? (2) is it genuinely UNCORRELATED (low beta / crisis corr) — the deal-break
# premium is idiosyncratic, unlike carry/VRP? (3) is it a PORTABLE-ALPHA source (port onto SPY, clears the
# hurdle with low crisis corr = the bore pattern)? Also excess-over-CASH (merger arb = collateral + spread),
# since post-2022 the risk-free rate flatters the raw return. Honest prior (bind): MNA is watered-down.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bite_common import MERGER, SPINOFF, CASH, panel, rets, riskadj, corr, beta, portable_alpha

P, dates = panel([MERGER, SPINOFF, CASH, "SPY"])
spy = rets(P["SPY"]); cash = rets(P[CASH])
print("=" * 96, f"\nBITE #1 — event-driven / merger arbitrage  ({dates[0]} → {dates[-1]}, {len(dates)} days)\n" + "=" * 96)
print(f"  {'instrument':<26}{'Sharpe':>8}{'CAGR':>7}{'vol':>7}{'maxDD':>7}{'beta-SPY':>10}{'skew':>7}{'corr-SPY':>10}")
for label, s in [("merger arb (MNA)", MERGER), ("spin-offs (CSD)", SPINOFF), ("SPY (reference)", "SPY")]:
    if s not in P: print(f"  {label:<26}  (insufficient history)"); continue
    r = rets(P[s]); m = riskadj(r, spy)
    print(f"  {label:<26}{m['sh']:>+8.2f}{m['cagr']*100:>+6.0f}%{m['vol']*100:>6.1f}%{m['dd']*100:>+6.0f}%"
          f"{beta(r,spy):>+10.2f}{m['skew']:>+7.2f}{corr(r,spy):>+10.2f}")

# the real deal-spread premium = MNA excess over cash
mna = rets(P[MERGER]); exc = mna - cash
me = riskadj(exc, spy)
print(f"\n  merger-arb EXCESS over cash (MNA − BIL): Sharpe {me['sh']:+.2f}, CAGR {me['cagr']*100:+.1f}%, skew {me['skew']:+.2f}")
print(f"  (post-2022 the T-bill rate flatters MNA's raw return; the spread over cash is the actual premium)")

pa = portable_alpha(mna, spy)
print(f"\n  Portable-alpha check (MNA ported onto SPY): clears={pa['clears']}  "
      f"Jensen α {pa['alpha_ann']*100:+.1f}%  M² {pa['m2_excess']*100:+.1f}%  full/crisis corr {pa['fullcorr']:+.2f}/{pa['crisiscorr']:+.2f}")
print("\n  READ: genuinely uncorrelated (low beta, low crisis corr) + positive Sharpe = the bore pattern (portable-")
print("  alpha keeper — the one bridge wished it was). Thin-after-fees / ~cash = watered-down null (bind's finding).")
