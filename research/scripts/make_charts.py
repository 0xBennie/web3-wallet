#!/usr/bin/env python3
"""Render bar charts of wallet on-chain fees from the first-hand DefiLlama data.

Input : research/data/firsthand/defillama_wallet_fees_revenue.csv
        research/data/firsthand/defillama_wallet_fees_monthly.csv
Output: research/charts/*.png
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
os.makedirs(OUT, exist_ok=True)

# palette / chrome (dataviz reference instance, light mode)
SURFACE = "#fcfcfb"
SERIES_1 = "#2a78d6"   # blue  - categorical slot 1
SERIES_2 = "#eb6834"   # orange - categorical slot 2
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"

for f in ["WenQuanYi Zen Hei", "Noto Sans CJK SC"]:
    if any(font.name == f for font in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = [f, "DejaVu Sans"]
        break
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "svg.fonttype": "none"})


def fmt_usd(v):
    if v >= 1e9:
        return f"${v/1e9:.2f}B"
    if v >= 1e6:
        return f"${v/1e6:.1f}M"
    if v >= 1e3:
        return f"${v/1e3:.0f}K"
    return f"${v:.0f}"


def style_axes(ax):
    for side in ["top", "right", "left"]:
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(BASELINE)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


def hbar(fname, title, subtitle, labels, values, color=SERIES_1):
    fig, ax = plt.subplots(figsize=(9, 0.62 * len(labels) + 1.9), dpi=200)
    y = range(len(labels))[::-1]
    ax.barh(list(y), values, height=0.55, color=color, zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, color=INK_2, fontsize=11)
    style_axes(ax)
    ax.xaxis.set_major_formatter(lambda v, _: fmt_usd(v) if v else "0")
    span = max(values)
    for yi, v in zip(y, values):
        ax.text(v + span * 0.012, yi, fmt_usd(v), va="center",
                color=INK_2, fontsize=10)
    ax.set_xlim(0, span * 1.14)
    fig.text(0.02, 0.965, title, color=INK, fontsize=14, fontweight="bold", va="top")
    fig.text(0.02, 0.965 - 0.055 * (9 / fig.get_figheight()), subtitle,
             color=MUTED, fontsize=10, va="top")
    fig.subplots_adjust(top=1 - 1.05 / fig.get_figheight(), bottom=0.6 / fig.get_figheight(),
                        left=0.20, right=0.97)
    fig.savefig(os.path.join(OUT, fname))
    plt.close(fig)
    print("wrote", fname)


# ------------------------------------------------ load first-hand data
rows = list(csv.DictReader(open(os.path.join(DATA, "defillama_wallet_fees_revenue.csv"))))
fees = {r["protocol"]: r for r in rows if r["metric"] == "fees"}

WALLETS = {  # DefiLlama protocol name -> display name
    "Phantom Wallet": "Phantom",
    "MetaMask Wallet": "MetaMask",
    "Base App": "Base App (Coinbase)",
    "Trust Wallet Wallet": "Trust Wallet",
    "Rabby Wallet": "Rabby",
    "Rainbow Wallet": "Rainbow",
    "Zerion Wallet": "Zerion",
}
NEW_LINES = {
    "fomo Wallet": "fomo Wallet (交易App)",
    "Phantom Perps": "Phantom 永续合约",
    "Telegram Wallet": "Telegram Wallet",
    "MetaMask Perps": "MetaMask 永续合约",
    "Phantom SOL": "Phantom SOL 质押",
    "MetaMask Predictions": "MetaMask 预测市场",
    "Trust Wallet Perps": "Trust Wallet 永续合约",
    "Rabby Perps": "Rabby 永续合约",
}


def series(names, col):
    data = [(disp, float(fees[p][col] or 0)) for p, disp in names.items() if p in fees]
    data.sort(key=lambda x: -x[1])
    return [d[0] for d in data], [d[1] for d in data]

STAMP = "数据源：DefiLlama API（链上手续费，一手数据）· 采集于 2026-08-02"

labels, values = series(WALLETS, "usd_all_time")
hbar("1_wallet_fees_cumulative.png", "主流 Web3 钱包累计链上手续费",
     f"{STAMP} · 上线至今累计", labels, values)

labels, values = series(WALLETS, "usd_1y")
hbar("2_wallet_fees_1y.png", "主流 Web3 钱包近一年链上手续费",
     f"{STAMP} · 近 365 天", labels, values)

labels, values = series(WALLETS, "usd_30d")
hbar("3_wallet_fees_30d.png", "主流 Web3 钱包近 30 天链上手续费",
     f"{STAMP} · 近 30 天", labels, values)

labels, values = series(NEW_LINES, "usd_30d")
hbar("4_wallet_new_business_30d.png", "钱包新业务线近 30 天费用（永续/质押/预测市场）",
     f"{STAMP} · 近 30 天", labels, values, color=SERIES_2)

# ------------------------------------------------ monthly grouped bars
monthly = list(csv.DictReader(open(os.path.join(DATA, "defillama_wallet_fees_monthly.csv"))))
months = sorted({r["month"] for r in monthly if "2025-07" <= r["month"] <= "2026-07"})
pm = {(r["protocol"], r["month"]): float(r["fees_usd"]) for r in monthly}
ph = [pm.get(("Phantom Wallet", m), 0) for m in months]
mm = [pm.get(("MetaMask", m), 0) for m in months]

fig, ax = plt.subplots(figsize=(11, 5), dpi=200)
x = range(len(months))
w = 0.38
b1 = ax.bar([i - w / 2 for i in x], ph, width=w - 0.03, color=SERIES_1, zorder=3, label="Phantom")
b2 = ax.bar([i + w / 2 for i in x], mm, width=w - 0.03, color=SERIES_2, zorder=3, label="MetaMask")
ax.set_xticks(list(x))
ax.set_xticklabels([m.replace("-", "/") for m in months], color=MUTED, fontsize=9)
for side in ["top", "right", "left"]:
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color(BASELINE)
ax.tick_params(colors=MUTED, length=0)
ax.yaxis.grid(True, color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
ax.yaxis.set_major_formatter(lambda v, _: fmt_usd(v) if v else "0")
# selective direct labels: peak month of each series only
for bars, vals in [(b1, ph), (b2, mm)]:
    i = vals.index(max(vals))
    ax.text(bars[i].get_x() + bars[i].get_width() / 2, vals[i] * 1.02,
            fmt_usd(vals[i]), ha="center", color=INK_2, fontsize=9)
leg = ax.legend(frameon=False, loc="upper right", fontsize=10, labelcolor=INK_2)
fig.text(0.02, 0.97, "Phantom vs MetaMask 月度链上手续费（近 12 个月）",
         color=INK, fontsize=14, fontweight="bold", va="top")
fig.text(0.02, 0.905, STAMP, color=MUTED, fontsize=10, va="top")
fig.subplots_adjust(top=0.82, bottom=0.09, left=0.07, right=0.97)
fig.savefig(os.path.join(OUT, "5_phantom_vs_metamask_monthly.png"))
plt.close(fig)
print("wrote 5_phantom_vs_metamask_monthly.png")
