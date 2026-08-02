#!/usr/bin/env python3
"""Estimate exchange-wallet swap revenue as volume x official fee-rate scenarios.

Volume is first-hand (DefiLlama aggregators). Fee rates come from official fee
pages; because every wallet blends 0%-tier and paid-tier pairs, we model an
EFFECTIVE blended rate as low / base / high scenarios. Wallets with real
on-chain fee data are shown as actuals for comparison.

Input : research/data/firsthand/defillama_exchange_wallet_volume.csv
        research/data/firsthand/defillama_wallet_fees_revenue.csv
Output: research/data/firsthand/revenue_estimates_30d.csv
        research/charts/6_actual_vs_estimated_revenue_30d.png
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

BASE = os.path.join(os.path.dirname(__file__), "..")
DATA = os.path.join(BASE, "data", "firsthand")
OUT = os.path.join(BASE, "charts")

SURFACE, SERIES_1, SERIES_2 = "#fcfcfb", "#2a78d6", "#eb6834"
INK, INK_2, MUTED, GRID, BASELINE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
for f in ["WenQuanYi Zen Hei", "Noto Sans CJK SC"]:
    if any(font.name == f for font in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = [f, "DejaVu Sans"]
        break
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE})

# Effective blended fee-rate scenarios (fraction, not %).
# Sources: Binance announcement 2025-11-26 (0% majors/Alpha, 0.5% others);
# OKX dex-fees page (tiers 0/0.1/0.25/0.5%); Bitget undisclosed (~0.3% market
# convention). Low/high bound the unknown mix of 0%-tier volume.
SCENARIOS = {
    "Binance Wallet": (0.001, 0.0025, 0.005),
    "OKX Swap": (0.0005, 0.0015, 0.0025),
    "Bitget Wallet X": (0.001, 0.003, 0.005),
}

vol = {r["protocol"]: float(r["vol_30d"]) for r in
       csv.DictReader(open(os.path.join(DATA, "defillama_exchange_wallet_volume.csv")))}
fees = {r["protocol"]: float(r["usd_30d"] or 0) for r in
        csv.DictReader(open(os.path.join(DATA, "defillama_wallet_fees_revenue.csv")))
        if r["metric"] == "fees"}

rows = []
est = []
for name, (lo, mid, hi) in SCENARIOS.items():
    v = vol[name]
    rows.append([name, "estimated", round(v), lo, mid, hi,
                 round(v * lo), round(v * mid), round(v * hi)])
    est.append((name.replace(" X", "").replace(" Swap", " Wallet"), v * lo, v * mid, v * hi))

ACTUALS = {"Phantom Wallet": "Phantom", "MetaMask Wallet": "MetaMask",
           "Base App": "Base App (Coinbase)", "Trust Wallet Wallet": "Trust Wallet"}
act = []
for proto, disp in ACTUALS.items():
    f = fees.get(proto, 0)
    rows.append([disp, "actual", "", "", "", "", "", f, ""])
    act.append((disp, f))

os.makedirs(DATA, exist_ok=True)
with open(os.path.join(DATA, "revenue_estimates_30d.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["wallet", "kind", "vol_30d_usd", "rate_low", "rate_base", "rate_high",
                "rev_30d_low_usd", "rev_30d_base_usd", "rev_30d_high_usd"])
    w.writerows(rows)
print("wrote revenue_estimates_30d.csv")

# ---- chart: actual fees (blue) vs estimated base with low-high range (orange)
items = sorted(act, key=lambda x: -x[1]) + sorted(est, key=lambda x: -x[2])
labels = [i[0] for i in items]
fig, ax = plt.subplots(figsize=(9.5, 0.62 * len(labels) + 2.1), dpi=200)
y = list(range(len(labels)))[::-1]


def fmt(v):
    return f"${v/1e6:.1f}M" if v >= 1e6 else f"${v/1e3:.0f}K"

span = 0
for yi, item in zip(y, items):
    if len(item) == 2:  # actual
        _, v = item
        ax.barh(yi, v, height=0.55, color=SERIES_1, zorder=3)
        ax.text(v * 1.02 + 3e5, yi, fmt(v) + "（实收）", va="center", color=INK_2, fontsize=10)
        span = max(span, v)
    else:               # estimated with range
        _, lo, mid, hi = item
        ax.barh(yi, mid, height=0.55, color=SERIES_2, zorder=3)
        ax.errorbar(mid, yi, xerr=[[mid - lo], [hi - mid]], fmt="none",
                    ecolor=INK_2, elinewidth=1.2, capsize=4, zorder=4)
        ax.text(hi * 1.02 + 3e5, yi, f"{fmt(mid)}（估算 {fmt(lo)}–{fmt(hi)}）",
                va="center", color=INK_2, fontsize=10)
        span = max(span, hi)

ax.set_yticks(y)
ax.set_yticklabels(labels, color=INK_2, fontsize=11)
for side in ["top", "right", "left"]:
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color(BASELINE)
ax.tick_params(colors=MUTED, length=0)
ax.xaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.xaxis.set_major_formatter(lambda v, _: fmt(v) if v else "0")
ax.set_xlim(0, span * 1.42)

import matplotlib.patches as mpatches
leg = ax.legend(handles=[mpatches.Patch(color=SERIES_1, label="实收手续费（链上一手）"),
                         mpatches.Patch(color=SERIES_2, label="估算收入 = 交易量 × 官方费率情景")],
                frameon=False, loc="lower right", fontsize=10, labelcolor=INK_2)
fig.text(0.02, 0.97, "近 30 天：钱包实收手续费 vs 交易所系钱包按费率估算的潜在收入",
         color=INK, fontsize=13.5, fontweight="bold", va="top")
fig.text(0.02, 0.97 - 0.05 * (9 / fig.get_figheight()),
         "交易量：DefiLlama API 一手 · 费率：各家官方费率页 · 估算区间反映 0% 费率档占比的不确定性 · 2026-08-02",
         color=MUTED, fontsize=9, va="top")
fig.subplots_adjust(top=1 - 1.15 / fig.get_figheight(), bottom=0.65 / fig.get_figheight(),
                    left=0.185, right=0.98)
fig.savefig(os.path.join(OUT, "6_actual_vs_estimated_revenue_30d.png"))
print("wrote 6_actual_vs_estimated_revenue_30d.png")
