#!/usr/bin/env python3
"""Fetch first-hand Web3 wallet data from public APIs (no API keys required).

Sources:
  1. DefiLlama  - on-chain wallet fees/revenue (https://api.llama.fi)
  2. Chrome Web Store - live extension user counts
  3. Google Play - install brackets for mobile wallets
  4. CoinGecko  - wallet-token market data (https://api.coingecko.com)

Output: CSV files under research/data/firsthand/
Run:    python3 research/scripts/fetch_wallet_data.py
"""
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.request

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "firsthand")
os.makedirs(OUT_DIR, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}


def get(url, retries=3, as_json=True):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode("utf-8", errors="replace")
            return json.loads(body) if as_json else body
        except Exception as e:
            if i == retries - 1:
                print(f"  FAILED {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 ** (i + 1))


def write_csv(name, rows, header):
    path = os.path.join(OUT_DIR, name)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


# ---------------------------------------------------------------- DefiLlama
# Wallet-category protocols plus wallet-adjacent protocols tracked elsewhere.
LLAMA_EXTRA_NAMES = re.compile(
    r"(wallet|metamask|phantom|rabby|rainbow|zerion|backpack|exodus|solflare|"
    r"base app|bitget|okx|coinbase|family|safepal|tokenpocket|imtoken|trust)",
    re.I,
)


def fetch_defillama():
    rows = []
    for data_type, label in [("dailyFees", "fees"), ("dailyRevenue", "revenue")]:
        d = get(
            "https://api.llama.fi/overview/fees?excludeTotalDataChart=true"
            f"&excludeTotalDataChartBreakdown=true&dataType={data_type}"
        )
        if not d:
            continue
        for p in d.get("protocols", []):
            if p.get("category") == "Wallets" or LLAMA_EXTRA_NAMES.search(p.get("name", "")):
                rows.append([
                    label, p.get("name"), p.get("category"), p.get("slug"),
                    p.get("total24h"), p.get("total7d"), p.get("total30d"),
                    p.get("total1y"), p.get("totalAllTime"),
                    ";".join(p.get("chains") or []),
                ])
    write_csv(
        "defillama_wallet_fees_revenue.csv", rows,
        ["metric", "protocol", "category", "slug", "usd_24h", "usd_7d",
         "usd_30d", "usd_1y", "usd_all_time", "chains"],
    )

    # Daily fee time series per wallet -> monthly aggregation.
    slugs = ["metamask", "phantom-wallet", "trust-wallet", "rabby-wallet",
             "rainbow-wallet", "zerion-wallet", "base-app", "coinbase-wallet"]
    monthly = {}
    for slug in slugs:
        d = get(f"https://api.llama.fi/summary/fees/{slug}?dataType=dailyFees")
        if not d or not d.get("totalDataChart"):
            print(f"  no daily series for {slug}")
            continue
        name = d.get("name", slug)
        for ts, usd in d["totalDataChart"]:
            month = dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).strftime("%Y-%m")
            monthly[(name, month)] = monthly.get((name, month), 0) + (usd or 0)
        time.sleep(0.5)
    rows = [[n, m, round(v, 2)] for (n, m), v in sorted(monthly.items())]
    write_csv("defillama_wallet_fees_monthly.csv", rows,
              ["protocol", "month", "fees_usd"])


# ------------------------------------------------------- Chrome Web Store
CHROME_EXTENSIONS = {
    "MetaMask": "nkbihfbeogaeaoehlefnkodbefgpgknn",
    "Phantom": "bfnaelmomeimhlpmgjnjophhpkkoljpa",
    "OKX Wallet": "mcohilncbfahbmgdjkbpemcciiolgcge",
    "Coinbase Wallet": "hnfanknocfeofbddgcijnmhnfnkdnaad",
    "Trust Wallet": "egjidjbpglichdcondbcbdnbeeppgdph",
    "Rabby": "acmacodkjbdgmoleebolmdjonilkdbch",
    "Bitget Wallet": "jiidiaalihmmhddjgbnbgdfflelocpak",
    "Backpack": "aflkmfhebedbjioipglgcbcmnbpgliof",
    "Rainbow": "opfgelmcmbiajamepnmloijbpoleiama",
    "Keplr": "dmkamcknogkgcdfhhbddcghachkejeap",
    "Solflare": "bhhhlbepdkbapadjdnnojkbgioiodbic",
}


def fetch_chrome_store():
    rows = []
    for name, ext_id in CHROME_EXTENSIONS.items():
        html = get(f"https://chromewebstore.google.com/detail/{ext_id}", as_json=False)
        users = rating = rating_count = None
        if html:
            m = re.search(r"([\d,.]+)\s*users", html)
            users = m.group(1).replace(",", "") if m else None
            m = re.search(r"([\d.]+)\s*\(([\d,.]+K?)\s*ratings?\)", html)
            if m:
                rating, rating_count = m.group(1), m.group(2)
        rows.append([name, ext_id, users, rating, rating_count])
        time.sleep(0.5)
    write_csv("chrome_store_users.csv", rows,
              ["wallet", "extension_id", "users", "rating", "rating_count"])


# ------------------------------------------------------------ Google Play
PLAY_APPS = {
    "Trust Wallet": "com.wallet.crypto.trustapp",
    "MetaMask": "io.metamask",
    "Phantom": "app.phantom",
    "Coinbase Wallet": "org.toshi",
    "OKX (exchange+wallet)": "com.okinc.okex.gp",
    "Bitget Wallet": "com.bitkeep.wallet",
    "SafePal": "io.safepal.wallet",
    "TokenPocket": "vip.mytokenpocket",
    "imToken": "im.token.app",
    "Exodus": "exodusmovement.exodus",
    "Rainbow": "me.rainbow",
}


def fetch_google_play():
    rows = []
    for name, pkg in PLAY_APPS.items():
        html = get(f"https://play.google.com/store/apps/details?id={pkg}&hl=en_US", as_json=False)
        downloads = rating = None
        if html:
            m = re.search(r'\[\[\["([\d.,]+[KMB]?\+)"\]\],\[\["Downloads"\]\]', html)
            if not m:
                m = re.search(r'"([\d.,]+[KMB]?\+)"[^"]{0,200}?Downloads', html)
            if not m:
                m = re.search(r'([\d.,]+[KMB]\+)\s*</div>\s*<div[^>]*>Downloads', html)
            downloads = m.group(1) if m else None
            m = re.search(r'"([\d.]+)\s*star', html)
            rating = m.group(1) if m else None
        rows.append([name, pkg, downloads, rating])
        time.sleep(0.5)
    write_csv("google_play_installs.csv", rows,
              ["wallet", "package", "downloads_bracket", "rating"])


# -------------------------------------------------------------- CoinGecko
CG_IDS = {
    "trust-wallet-token": "Trust Wallet (TWT)",
    "safepal": "SafePal (SFP)",
    "tokenpocket": "TokenPocket (TPT)",
    "okb": "OKX (OKB)",
    "bitget-token": "Bitget (BGB)",
    "exodus-shares": "Exodus (tokenized stock)",
}


def fetch_coingecko():
    ids = ",".join(CG_IDS)
    d = get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
        f"&ids={ids}&order=market_cap_desc&per_page=50&sparkline=false"
    )
    rows = []
    for c in d or []:
        rows.append([
            CG_IDS.get(c["id"], c["id"]), c["id"], c.get("current_price"),
            c.get("market_cap"), c.get("fully_diluted_valuation"),
            c.get("total_volume"), c.get("price_change_percentage_24h"),
            c.get("ath"), c.get("ath_date"),
        ])
    write_csv("coingecko_wallet_tokens.csv", rows,
              ["wallet_token", "coingecko_id", "price_usd", "market_cap_usd",
               "fdv_usd", "volume_24h_usd", "chg_24h_pct", "ath_usd", "ath_date"])


if __name__ == "__main__":
    print(f"fetch started {dt.datetime.now(dt.timezone.utc).isoformat()}")
    fetch_defillama()
    fetch_chrome_store()
    fetch_google_play()
    fetch_coingecko()
    print("done")
