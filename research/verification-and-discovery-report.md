# 数据二次核验与增量数据报告

> 执行时间：2026-08-02 · 方式：3 个并行 agent（① API 重拉+算术核验+查重，② 新端点数据挖掘，③ 数据源侦察）
> 修正已全部落库；新数据集在 `research/data/firsthand/discovered/`（10 个 CSV）。

---

## 一、核验结果总览

### ✅ 通过核验、可放心引用的数据

- **DefiLlama 全部一手数据**：7 个钱包的费用（24h/30d/1y/累计）、3 家交易所钱包的交易量——重新拉取 API 后 15+ 项指标全部 0% 漂移，逐项 PASS。
- **revenue_estimates_30d.csv 的全部 9 个乘法**：逐一重算，全部精确。
- **月度序列抽查**（Phantom 2024-11 / 2025-01 / 2025-09 / 2026-07）：与 API 重新聚合结果完全一致。
- **MetaMask 隐含费率交叉验证**：30 天费用 ÷ 30 天交易量 = 1.0%，与公示 0.875% 同量级（差额可解释为质押抽成等），逻辑自洽。
- **OKX 实际费率 0.006%**：累计费用 ÷ 累计交易量重算无误。
- 所有 CSV 按自然键查重：**零重复行**。

### ⚠️ 发现并已修正的错误（7 处）

| # | 错误 | 修正 |
|---|---|---|
| 1 | **月度 CSV 中 Base App 全部数值被双倍计数**（`base-app` 与 `coinbase-wallet` 是同一协议的别名，脚本把两个都加了一遍） | 修复脚本 slug 列表，重新拉取，月度合计已与累计值 $125.6M 对齐 |
| 2 | **MetaMask/Trust 月度序列误用父口径**（含 Perps/mUSD/预测市场收入，而 Phantom 是纯钱包口径，图 5 对比不公平） | 改用子口径 slug；图 5 已重绘并标注口径 |
| 3 | Phantom 近 12 个月峰值写成 2025-09 $15.7M（实为 **2025-08 $21.3M**） | 已改 |
| 4 | 摘要文档 24h 数值引用了过期快照（MetaMask $54,798→$61,237 等） | 已改 |
| 5 | 月度序列标注"2020 至今"（实际最早 2023-01） | 已改 |
| 6 | Rabby 安装量两处写法矛盾（440 万 vs 420 万） | 统一为 420 万 |
| 7 | Rabby 的 MAU 列错填了安装量（与粘性 0.41 矛盾，DAU 14 万 ÷ 0.41 隐含 MAU ≈34 万） | MAU 列清空并注明推算值 |

### 🚫 判定为不可信、已标记 DISPUTED 的二手数字（4 个）

1. **"MetaMask 累计 $3.25 亿（DefiLlama 口径）"**——DefiLlama 实测累计只有 $1.929 亿，累计值不可能随时间缩水；该数字与 Phantom 2025 总收入 $3.2589 亿高度雷同，疑为二手站张冠李戴。三份报告中的相关表述已全部改写。（CoinLaw 的 $1.986 亿与实测吻合，可用。）
2. **Binance Alpha "2025 年交易量 $1 万亿"**——DefiLlama 链上口径 2025 全年仅 ~$838 亿，差 12 倍，远超"刷量"能解释的范围。保留原话但标记 DISPUTED。
3. **Rabby Q3 2025 费用 $232 万（CoinLaw）**——一手 DefiLlama 月度加总为 $392 万，差 69%。
4. **Phantom 2025 年 1 月 swap 量 $57 亿**——对应一手费用 $1.15 亿，隐含费率 2%，是公示费率 0.85% 的 2.4 倍，交易量疑被低估（更可能约 $130 亿）。

### 📌 上游数据自身的坑（无法修，引用时注意）

- OKX Swap 2025-04 月交易量只有 $1,359（适配器断档）；Bitget Wallet X 缺 2024-05~2024-10；Base App 2025-11/12、Rabby 2025-11 有适配器故障月。
- 两个月度 CSV 的 **2026-08 行是 1–2 天的不完整月**，任何分析必须剔除（图表已剔除）。

---

## 二、新发现的数据（10 个新 CSV，已入库 `discovered/`）

### ⭐ 最重磅：Exodus 的 SEC 审计财报（全行业唯一审计级钱包数据）

`exodus_sec_kpis.csv` / `exodus_sec_revenue_history.csv`（来源：SEC EDGAR，10-Q/10-K XBRL）

- MAU 150 万（2026-03）；季度入金用户 140 万（同比 -22%）
- **2026 Q1 收入 $2270 万，其中"交易聚合（swap 路由）"收入 $2000 万，占 87.9%**
- 年度收入：2023 $5620 万 → 2024 $1.163 亿 → 2025 $1.216 亿
- 隐含 ARPU ≈ $15/入金用户/季度

**这是"钱包=流量路由生意"的审计级铁证**：一家上市钱包公司近 9 成收入来自把用户交易路由给做市商/交易所的抽成。可作为整个研究的锚点证据。

### 钱包新业务线（DefiLlama 免费端点）

- `defillama_wallet_perps_monthly_fees.csv`：五大钱包 2026 年扎堆上线永续合约——Phantom Perps 累计费用 $2360 万（2026-05 才上线）、MetaMask Perps $830 万、Trust Wallet Perps 月环比 10 倍增长。永续**交易量**端点已收费（402），费用是免费替代口径。
- `defillama_wallet_card_fomo_monthly_volume.csv`：MetaMask Card 累计刷卡量 $6610 万、Bitget Wallet Card $4290 万、SafePal Card $1200 万；以及 fomo Wallet 的爆发曲线（$2700 万→$2.74 亿→$4.87 亿，三个月）。
- `defillama_wallet_fees_vs_revenue.csv`：**几乎所有钱包 revenue == fees（100% 留存费用）**——钱包不像 DEX 要分给 LP，入口位置的钱全归自己。唯一例外 fomo Wallet（留存 ~92%）。
- `defillama_wallet_products_overview.csv`：47 个钱包系产品的全景表（swap/perp/卡/预测市场）。
- `defillama_metamask_aggregator_monthly_volume.csv`：MetaMask 月度交易量序列（补齐费用序列的分母，可算逐月隐含费率）。

### 分发与生态数据

- `appstore_wallet_ratings.csv`（iTunes 官方 API，美区）：iOS 评分数排名 Trust 19.8 万 > Base App 16.1 万 > MetaMask 7.6 万 > Phantom 6.4 万——补上了 Apple 生态的缺口。
- `npm_wallet_sdk_downloads.csv`：**Coinbase Wallet SDK 月下载 834 万次**、WalletConnect provider 479 万、MetaMask SDK 266 万——开发者把钱包 SDK 装进 dApp，证明"dApp 主动接入钱包"而非相反，是入口论的开发者侧证据。
- `github_wallet_repos.csv`：metamask-extension 13,191★（今日仍活跃提交）；Phantom/Solflare 闭源。

### 数据源侦察结论（验证过、可随时启用）

| 排名 | 数据源 | 能拿到什么 | 成本 |
|---|---|---|---|
| 1 | **Blockscout 公共 API**（免 key） | 链上路由合约交易数——MetaMask Swap Router 累计 **17,294,973 笔**、OKX 路由 437,088 笔（以太坊）；可用 label 搜索找到各家路由地址，覆盖 Base/OP/Polygon 等链 | 极低 |
| 2 | **Firefox 商店 API**（免 key） | 真实 **日活**（Chrome 只给安装数）：MetaMask Firefox 日活 304,052 | 极低 |
| 3 | **iTunes API + 评论 RSS** | iOS 评分数/评论流 | 极低（已入库） |
| 4 | **WalletConnect 官方披露** | 54M+ 独立活跃钱包、380M+ 连接、80,000+ 接入应用；dataroom 实时 24h：17.6 万连接/$11.4 亿量——**直接度量"钱包→dApp 连接"这件事本身** | 低（无 JSON API，需引用/抓页面） |
| 5 | **Wayback Machine** | Chrome 商店历史快照→可回溯构建插件用户数时间序列 | 中 |
| — | SEC EDGAR 全文检索 | 82 份上市公司文件提到 MetaMask；Consensys IPO 的 S-1 公开后将是终极一手数据，值得设监控 | 低 |
| ✗ | 死胡同 | Similarweb（403）、Token Terminal（需付费 key）、DefiLlama 衍生品交易量（转收费 402）、growthepie apps 端点（403） | — |

---

## 三、修正后的关键结论（最终口径）

1. Phantom 链上累计费用 **$552.4M**，MetaMask **$192.9M**（2.9 倍）；近 30 天 3.6 倍。✅ 一手验证
2. MetaMask 累计收入正确口径是 **$1.93–1.99 亿**（DefiLlama 实测 + CoinLaw 互证）；$3.25 亿是讹传。
3. MetaMask（纯钱包口径）月费用 2026 年中 $1.6–1.9M/月；Phantom $5–6M/月。
4. 钱包收入=费用（100% 留存），且 88% 收入来自 swap 路由（Exodus 审计数据）——入口即生意的最硬证据。
5. 交易所系钱包零费买流量的结论不变，且有了新佐证（Binance 自报交易量与链上差 12 倍）。
