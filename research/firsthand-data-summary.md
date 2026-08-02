# 一手数据（Public API 直采）说明与摘要

> 采集时间：2026-08-02 15:26 UTC
> 采集脚本：`research/scripts/fetch_wallet_data.py`（无需任何 API key，可随时重跑刷新）
> 数据文件：`research/data/firsthand/` 下 5 个 CSV

## 数据源与口径

| 文件 | 来源 | 口径说明 |
|---|---|---|
| `defillama_wallet_fees_revenue.csv` | DefiLlama API (`api.llama.fi`) | **链上真实抽成**（用户支付给钱包的费用），24h/7d/30d/1y/累计，按协议 × fees/revenue 两种 metric |
| `defillama_wallet_fees_monthly.csv` | DefiLlama API | 各钱包**逐月费用时间序列**（2020 至今，232 行），可直接做趋势/回归分析 |
| `chrome_store_users.csv` | Chrome Web Store 页面 | 各插件钱包**当前活跃安装数**（Google 官方披露口径） |
| `google_play_installs.csv` | Google Play 页面 | 安卓端**下载量区间**（如 50M+） |
| `coingecko_wallet_tokens.csv` | CoinGecko API | 钱包相关代币的价格/市值/FDV（市场对钱包生态的定价） |

这些全部是**平台方/链上第一手口径**，与此前二手统计站的数据相互独立，可用来交叉验证。

## 核心发现（截至 2026-08-02）

### 1. 链上费用：Phantom 已反超 MetaMask 3.5 倍

| 钱包 | 24h 费用 | 30d 费用 | 近 1 年费用 | 累计费用 |
|---|---|---|---|---|
| Phantom | $138,044 | $5.68M | $117.4M | **$552.4M** |
| MetaMask | $54,798 | $1.59M | $41.7M | $192.9M |
| Base App (Coinbase) | $5,445 | $0.47M | $21.3M | $125.6M |
| Trust Wallet | $1,744 | $0.20M | $4.4M | $34.6M |
| Rabby | $2,889 | $0.09M | $4.0M | $13.0M |
| Rainbow | $1,614 | $0.03M | $1.4M | $8.3M |
| Zerion | $0 | $0 | $0.43M | $3.4M |

注意：这与二手报告"MetaMask 变现第一"的叙事相反——**按链上实收，Phantom 累计费用（$552M）已是 MetaMask（$193M）的 2.9 倍，近一年是 2.8 倍**。二手报告普遍滞后 1 年以上。

### 2. 钱包的第二增长曲线已在链上可见（DefiLlama 单列的新业务线，30d 费用）

- fomo Wallet（Trading App 类）：$7.33M —— 甚至超过 Phantom 主 swap
- Phantom Perps：$1.02M（累计 $23.6M）
- Telegram Wallet：$0.69M
- MetaMask Perps：$0.65M（累计 $8.3M）
- Phantom SOL 质押：$0.50M
- MetaMask Predictions（预测市场）：$0.24M（刚上线）
- Trust Wallet Perps：$0.17M

**钱包正在把 perp、质押、预测市场做成独立收入线**，验证了"入口 → 超级 App"的路径。

### 3. 插件端分发（Chrome Web Store 实时活跃安装）

MetaMask 1200 万 > Phantom 400 万 > OKX/Coinbase/Trust/Keplr 各 100 万 > Rabby 80 万 > Solflare 70 万 > Bitget/Backpack 各 30 万 > Rainbow 10 万。
**插件端 MetaMask 仍是绝对霸主（3 倍于第二名）**，与链上费用形成反差：Phantom 的收入靠移动端。

### 4. 移动端分发（Google Play 下载区间）

Trust Wallet 50M+ 一档独大；MetaMask / Phantom / Coinbase Wallet / OKX / Bitget 同在 10M+ 档；SafePal / TokenPocket / Exodus 5M+；imToken 1M+；Rainbow 500K+。

### 5. 市场定价（CoinGecko，钱包相关代币）

OKB $18.2 亿市值 > BGB $11.4 亿 > TWT $1.59 亿 > SFP $1.08 亿。
交易所系平台币不纯粹代表钱包业务，但 TWT/SFP 是最接近"纯钱包"的市场定价样本。

### 6. 费用月度趋势（近 12 个月）

- Phantom：2025-09 峰值 $15.7M/月 → 2026 年中稳定在 $5–6M/月（腰斩后企稳）
- MetaMask：2025-10 峰值 $7.7M/月 → 2026 年中 $2.5–2.7M/月
- 两者收入均与行情周期强相关，但 Phantom 在每个时点都保持约 2 倍于 MetaMask 的月费用
- 完整月度序列（2020 至今）在 `defillama_wallet_fees_monthly.csv`，可做行情 β 回归

## 一手 vs 二手数据的差异清单

| 结论 | 二手报告说法 | 一手数据 |
|---|---|---|
| 钱包变现第一名 | MetaMask（累计 $199–325M） | **Phantom**（链上累计 $552M，且仍在拉开差距） |
| MetaMask 累计收入 | $325M（DefiLlama 口径被二手站引用） | 当前实际 API 值为 $193M（fees 口径），二手站数字已过期或口径混用 |
| Coinbase Wallet 存在感 | MAU 320 万，较弱 | Base App 累计费用 $125.6M，链上变现全行业第三 |
| Telegram Wallet | 只有"激活 1.1 亿"的宣传口径 | 链上月费用 ~$0.69M，真实变现规模很小但在增长 |

## 交易所系钱包（OKX / Binance / Bitget）：交易量一手可得，收入需归因

新增两个数据文件（2026-08-02 二次采集）：
- `defillama_exchange_wallet_volume.csv`：三家 swap **交易量**总览
- `defillama_exchange_wallet_monthly.csv`：三家逐月交易量序列 + OKX Swap 逐月费用序列

| 钱包 | 30d 交易量 | 近 1 年交易量 | 累计交易量 | 费用数据 |
|---|---|---|---|---|
| Binance Wallet | $113.1 亿 | $636.8 亿 | $1068.2 亿 | 无适配器（补贴期近零费） |
| OKX Swap | $63.9 亿 | $1023.8 亿 | $1933.7 亿 | 有适配器：累计仅 $1086 万，近月为 $0（零费策略） |
| Bitget Wallet X | $12.6 亿 | $62.0 亿 | $143.3 亿 | 无适配器 |

**结论：这三家的"收入"低不是数据缺失，而是商业模式**——交易所系钱包用零费/补贴买流量（OKX 累计 $1933 亿交易量只收了 $1086 万费用，实际费率 0.006%），变现发生在交易所内部（导流开户、上币、平台币），链上无法归因。若要估算收入：交易量 × 假设费率做情景分析，或做链上费用归集地址追踪（见下）。

- DefiLlama 只覆盖对接了其适配器的钱包：OKX Wallet、Bitget Wallet、Binance Web3 Wallet 的钱包内抽成**不在此列**（交易所系钱包费用多走内部账，链上不可直接归因）。
- Chrome/Play 商店数字是**分发量**不是 MAU；Apple App Store 不公开下载数。
- MAU 类数据没有免费一手 API（Dune/DappRadar/Sensor Tower 均需付费 key）。如需，下一步可以：① 申请 Dune 免费 API key 跑 wallet report 查询；② 用各链公开 RPC 统计已知钱包路由合约的交互地址数（工程量较大但完全一手）。

## 重跑方式

```bash
python3 research/scripts/fetch_wallet_data.py
```
