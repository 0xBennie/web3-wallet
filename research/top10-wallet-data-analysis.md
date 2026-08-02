# Top 10 Web3 钱包数据分析（2025–2026）

> 配套数据表：`research/data/top10_wallets.csv`（钱包明细）、`research/data/industry_metrics.csv`（行业/链上指标）。
> 数据截至 2026 年 8 月。不同来源口径差异较大，冲突之处已在「口径与冲突说明」一节列出，做分析时请先读该节。

---

## 一、链上 / 行业核心数据清单

### 1. 行业规模指标

| 指标 | 数值 | 时点 | 来源 |
|---|---|---|---|
| 全球活跃加密钱包用户 | ~8.2 亿（约占全球互联网人口 15%） | 2025 | CoinLaw |
| 全球加密资产持有者 | ~7.41 亿（同比 +12.4%） | 2025 | CoinLaw/SQ Magazine |
| 每月活跃链上地址 | ~2.2 亿 | 2024 末 | 行业估算 |
| 对应真实自然人月活 | 估计 3000 万～6000 万 | 2024 末 | 行业估算 |
| dApp 日活独立钱包（dUAW） | 2430 万（同比 +247%） | 2025 Q2 | DappRadar 系口径 |
| 全球 dApp 独立 MAU（前端口径） | 500 万～1000 万 | 2025 | CoinLaw |
| 与 dApp 交互过的钱包占比 | ~48% | 2025 | PatentPC |
| 移动端钱包使用偏好 | 72%（插件钱包仅 ~12%） | 2025 | CoinLaw |
| 协议网站访客→连接钱包→成交转化 | 200 : 10 : 1（~0.5%） | 2025 | PatentPC |
| 零售稳定币交易规模 | 2025 年增长约 10 倍 | 2025 | The Paypers |
| C2M 稳定币支付发起端 | ~2/3 来自交易所账户（非自托管钱包） | 2025 | BCG 白皮书 |

### 2. 区域分布（活跃钱包用户，2025）

| 区域 | 用户数 | 占比/特征 |
|---|---|---|
| 亚太 | ~3.5 亿 | 43%，全球最大 |
| 欧洲 | ~1.4 亿 | 同比 +12% |
| 北美 | ~1.34 亿 | ~16% |
| 拉美 | ~9200 万 | 汇款/抗通胀驱动 |
| 非洲 | ~7500 万 | 增速最快 |

### 3. 链上交易/收入类指标（钱包侧）

| 指标 | 数值 | 说明 |
|---|---|---|
| MetaMask swap 费率 | 0.875% | 另有 ETH 质押抽成 10% |
| MetaMask 累计收入 | $1.93 亿（DefiLlama 实测）～$1.99 亿（CoinLaw） | 链上分布：ETH $1.4 亿、BSC $2930 万、Arbitrum $747 万、Polygon $717 万；流传的 $3.25 亿口径已证伪 |
| Phantom 2025 年收入 | $7910 万（净）／$3.26 亿（协议总收入口径） | 2025.1 单月 swap 量 $57 亿 |
| Phantom 占 Solana 转账量 | 峰值 10%～20% | 2024 末–2025 初 |
| Binance Wallet（Alpha）单日交易量 | 峰值 >$50 亿（2025.5.19，占 top12 钱包 95.3%） | Alpha 2.0 全年交易量 >$1 万亿、17M 用户 |
| Rabby 季度手续费 | $232 万（2025 Q3） | 小体量高粘性样本 |
| Ronin Wallet 周 swap 量 | 峰值 >$5500 万（2025 初） | 游戏链样本 |

---

## 二、Top 10 名单及选取标准

以 **MAU（月活）为主、总用户/下载量为辅**排序，兼顾类型代表性（独立钱包 / 交易所系 / 社交内嵌）：

| 排名 | 钱包 | 类型 | MAU（保守口径） |
|---|---|---|---|
| 1 | Trust Wallet | 交易所系（Binance）独立品牌 | ~6000 万 |
| 2 | MetaMask | 独立（ConsenSys） | 3000 万+ |
| 3 | Phantom | 独立（Solana 系起家） | ~1700–2000 万 |
| 4 | Binance Web3 Wallet | 交易所内嵌 | Alpha 用户 1700 万（年度） |
| 5 | OKX Wallet | 交易所系 | 500 万～1500 万（口径差异大） |
| 6 | Bitget Wallet | 交易所系 | 1200 万+ |
| 7 | Telegram TON Wallet | 社交内嵌 | 激活 1.1 亿+（MAU 未披露） |
| 8 | Coinbase Wallet | 交易所系独立 App | 320 万（CoinLaw）～7000 万（ratex，存疑） |
| 9 | SafePal | 独立（硬件+软件） | 总用户 2500 万+（MAU 未披露） |
| 10 | TokenPocket | 独立（亚洲市场） | 总用户 2500 万+（MAU 未披露） |

**候补/观察名单**（体量小但分析价值高）：Rabby（420 万安装、粘性最高）、Exodus（150 万 MAU、美股上市）、Zerion（200 万 MAU）、Rainbow、Safe（机构多签，留存 70%）、Backpack、imToken（150+ 国家，未披露用户数）。

---

## 三、Top 10 逐个分析

### 1. Trust Wallet —— 移动端规模之王
- **数据**：累计下载 2 亿+（2025.3）；MAU ~6000 万（另有 ratex 口径 1.15 亿）；DAU ~380 万；2025 年底 MAU 市场份额 ~35%；支持 70+ 链。
- **模式**：Binance 收购的独立品牌，移动端为主，swap 路由 ~95% 走第三方聚合器（1inch/Jupiter/Paraswap）。
- **强项**：新兴市场（东南亚/拉美/非洲）渗透率第一；多链覆盖最广。
- **弱项**：变现效率低（ARPU 远低于 MetaMask/Coinbase Wallet）；与 Binance Web3 Wallet 左右手互搏。

### 2. MetaMask —— 变现效率与生态位标杆
- **数据**：MAU 3000 万+（4 个月 +55%）；下载 1.43 亿；DAU ~100 万；ARPU ~$10.8/年；累计收入 $1.93–1.99 亿（DefiLlama 实测/CoinLaw）；月留存 ~65%。
- **模式**：swap 抽成 0.875% + 质押抽成 10%；2025.10 上线 40x 永续；发行 mUSD 稳定币 + MetaMask Card；评估 IPO。
- **强项**：EVM 生态默认入口（"Connect Wallet"事实标准）；变现验证最充分。
- **弱项**：移动端弱于 Trust/Phantom；DAU/MAU 粘性（~0.03）远低于 Rabby（0.41）；非 EVM 链起步晚（2025.12 才原生支持 BTC）。

### 3. Phantom —— 行情驱动的高增长样本
- **数据**：MAU 1500 万→近 2000 万（同比 5 倍）；2025 收入 $7910 万；周 swap 峰值 1000 万笔；2025.1 月 swap 量 $57 亿；峰值占 Solana 转账量 10–20%；估值 $30 亿（Sequoia C 轮 $1.5 亿）。
- **模式**：内置 swap 抽成，ARPU ~$4.8；从 Solana 扩展到 EVM/BTC 多链，向"消费级金融 App"转型。
- **强项**：meme/链上交易场景的第一入口；移动端体验标杆；印度、尼日利亚等新兴市场增长最快。
- **弱项**：收入与 Solana meme 行情高度相关（β 极大）；多链扩张成效待验证。

### 4. Binance Web3 Wallet —— 交易所流量灌注的天花板
- **数据**：Alpha 2.0 全年交易量 >$1 万亿、参与用户 1700 万；单日交易量峰值 >$50 亿（2025.5，占 top12 钱包监控口径 95.3%）；2025 年处理主流链上交易 >60%（Binance 口径）；母体 Binance 注册用户 3 亿。
- **模式**：内嵌于 Binance App，用 Alpha 打新/空投（5 月人均空投价值 $1076）把 CEX 流量灌进链上。
- **强项**：获客成本近乎为零；空投激励制造了全行业最大的链上交易量。
- **弱项**：交易量含大量刷分/激励套利水分；用户忠诚于空投而非产品；数据多为自报口径。

### 5. OKX Wallet —— 交易所系里的"产品派"
- **数据**：下载 5000 万+；MAU 500 万+（CoinLaw，Q2 2025，同比 +20%；ratex 口径 1500 万）；swap/跨链活动同比 +57%；覆盖 100+ 国家；ARPU ~$4.5。
- **模式**：CEX + Wallet 双 App，主打聚合交易（DEX 聚合器）和 Web3 门户定位。
- **强项**：产品口碑好，聚合路由深度强；亚洲链上交易用户占比高。
- **弱项**：MAU 口径分歧大；独立于交易所的品牌心智弱于 MetaMask/Phantom。

### 6. Bitget Wallet —— 下载量黑马
- **数据**：宣称总用户 8000 万（2025 中）；MAU 1200 万+（2025.8 当月全球下载第一）；支持 70+ 链。
- **模式**：交易所系，主打新兴市场 + meme 交易 + 跟单。
- **强项**：增长速度（从 6000 万到 8000 万用户仅半年口径）；下载榜表现强。
- **弱项**：总用户数为宣称口径，MAU/总用户比（~15%）偏低，活跃质量待验证。

### 7. Telegram TON Wallet —— 社交内嵌的规模怪物
- **数据**：累计激活 1.1 亿+（2025，较年初 +10%）；2025.7 向 8700 万美国用户开放；TON Mini App 超 1000 个（+25% since 2025.7）。
- **模式**：系统级内嵌（无需下载），MoonPay 零费入金，直连 Mini App 生态。
- **强项**：获客路径最短（Telegram 9 亿+ 用户就地转化）；美国合规开放是里程碑。
- **弱项**：激活≠活跃，MAU 未披露；资产沉淀和交易深度远弱于头部独立钱包；生态绑定单链（TON）。

### 8. Coinbase Wallet —— 合规市场的入口 + 最高 ARPU
- **数据**：安装 1500 万+（35% 来自美国以外）；MAU 320 万（CoinLaw；ratex 给出 7000 万，疑将 Coinbase 主 App 计入，谨慎采用）；DAU ~230 万（ratex 口径）；ARPU ~$35（全行业最高）；月留存 ~68%。
- **模式**：与 Base 链、USDC、Coinbase 主站形成闭环；swap 100% 走聚合器。
- **强项**：合规品牌 + Base 生态导流；单用户变现能力第一。
- **弱项**：规模远小于主 App（120M MAU 的 ~2.7%）；增长依赖美国监管友好周期。

### 9. SafePal —— 硬件+软件一体的差异化玩家
- **数据**：总用户 2500 万+；覆盖 127 个国家/200+ 地区；Binance Labs 投资。
- **模式**：硬件钱包（$50 价位）+ 软件钱包 + 交易聚合，硬件销售提供非行情相关收入。
- **强项**：安全心智 + 硬件现金流；新兴市场渠道。
- **弱项**：MAU 未披露；软件端活跃度与头部差距大。

### 10. TokenPocket —— 亚洲多链老牌
- **数据**：总用户 2500 万+（2018 年至今累计）；亚洲（尤其中文区）渗透高。
- **模式**：多链 + dApp 浏览器 + 内置聚合交易。
- **强项**：EOS/TRON 时代积累的存量用户；中文区品牌。
- **弱项**：MAU 未披露，增长叙事弱；国际化和合规布局落后。

---

## 四、横向对比表（保守口径）

| 钱包 | MAU | DAU | 总用户/下载 | ARPU($/年) | 月留存 | DAU/MAU | 2025 收入 | 支持链 |
|---|---|---|---|---|---|---|---|---|
| Trust Wallet | 60M | 3.8M | 200M+ 下载 | 低 | – | ~0.06 | 未披露 | 70+ |
| MetaMask | 30M+ | 1M | 143M 下载 | 10.8 | 65% | ~0.03 | 累计 $193–199M | EVM+BTC/SOL |
| Phantom | 17–20M | – | – | 4.8 | – | – | $79.1M | SOL+EVM+BTC |
| Binance W3W | 17M(年) | – | 母体 300M 注册 | – | – | – | 未披露 | 多链 |
| OKX Wallet | 5–15M | – | 50M+ 下载 | 4.5 | – | – | 未披露 | 100+ |
| Bitget Wallet | 12M+ | – | 80M 用户(宣称) | – | – | – | 未披露 | 70+ |
| TON Wallet | 未披露 | – | 110M+ 激活 | – | – | – | 未披露 | TON |
| Coinbase Wallet | 3.2M* | 2.3M* | 15M+ 安装 | 35 | 68% | – | 未披露 | 多链+Base |
| SafePal | 未披露 | – | 25M+ 用户 | – | – | – | 硬件收入 | 100+ |
| TokenPocket | 未披露 | – | 25M+ 用户 | – | – | – | 未披露 | 多链 |
| *参考组* Rabby | 4.2M 安装 | 140K | – | 5.7 | – | 0.41 | Q3 费用 $2.32M | 122 EVM |
| *参考组* Exodus | 1.5M | – | – | – | – | – | 上市公司财报 | 多链 |
| *参考组* Zerion | 2M | – | – | 6.2 | – | – | – | EVM |
| *参考组* Safe | 1M | 30K | – | – | 70% | 0.03 | – | EVM |

\* Coinbase Wallet 的 MAU 3.2M 与 DAU 2.3M 来自不同来源（CoinLaw vs ratex），两数互相矛盾，见下节。

---

## 五、口径与冲突说明（做数据分析前必读）

1. **Coinbase Wallet MAU**：CoinLaw 3.2M vs ratex 70M。70M 大概率把 Coinbase 主 App（120M 月活用户体系）算了进去。建议采用 3.2M，并把 70M 标记为异常值。
2. **Trust Wallet MAU**：官方系 60M vs ratex 115M。差异可能是"月交互地址"与"月活设备"之别。建议区间处理 [60M, 115M]。
3. **OKX Wallet MAU**：CoinLaw 5M vs ratex 15M。同上，建议区间 [5M, 15M]。
4. **MetaMask 收入**：DefiLlama API 实测累计 $192.9M（2026-08）与 CoinLaw $198.64M 基本一致、相互印证；二手站流传的 $325M"DefiLlama 口径"与实际 API 值矛盾（累计费用不可能随时间缩水），且数值与 Phantom 2025 年协议总收入 $325.89M 高度雷同，疑为张冠李戴，**不应引用**。
5. **Phantom 收入**：$79.1M（净收入）vs $325.89M（协议总收入，含转给 LP/路由方部分）。
6. **Binance 的 95.3% 市场份额**：仅指某监控口径下 top12 钱包的**单日交易量**，且 Alpha 交易量受空投激励驱动，含大量刷量，不能与自然交易量直接对比。
7. **"用户数"三种口径**：累计注册/激活（TON 110M、Bitget 80M）＞累计下载（Trust 200M）＞MAU（真实活跃）。跨钱包对比只能用同口径数据。
8. 行业总量"8.2 亿钱包用户"是地址/账户口径，真实自然人月活估计仅 30–60M——**头部 10 家钱包的 MAU 加总（~1.5 亿）已超过真实人数估计**，进一步证明一人多钱包和口径注水并存。

---

## 六、给数据分析的切入建议

1. **规模 vs 质量矩阵**：X 轴 MAU、Y 轴 ARPU（或 DAU/MAU 粘性）。会看到四个象限：规模+变现（MetaMask）、规模低变现（Trust）、小而美（Rabby/Zerion）、补贴驱动（Binance W3W）。
2. **变现效率**：ARPU 排序 Coinbase($35) > MetaMask($10.8) > Zerion($6.2) > Rabby($5.7) > Phantom($4.8) > OKX($4.5)。合规市场（美国）用户价值 3–7 倍于全球平均。
3. **粘性**：DAU/MAU——Rabby 0.41、Backpack 0.39 远超 MetaMask ~0.03。专业交易用户粘性是普通持币用户的 10 倍量级。
4. **行情 β**：Phantom 收入曲线与 Solana meme 行情、MetaMask 收入与 ETH 行情的相关性，可用 DefiLlama 周度费用数据回归。
5. **渠道类型对比**：独立钱包（MetaMask/Phantom）靠产品与路由变现；交易所系（Binance/OKX/Bitget）靠补贴换规模；社交内嵌（TON）靠零获客成本换激活。三种模式的 LTV/CAC 结构完全不同。
6. **可持续追踪的公开数据源**：DefiLlama（钱包费用/收入，周度）、Dune Wallet Report（MAU/swap 量）、DappRadar（dUAW）、Sensor Tower/AppBrain（下载量）。建议以这四个做时间序列面板。

---

## 七、数据来源

- CoinLaw：[MetaMask](https://coinlaw.io/metamask-wallet-statistics/)、[Phantom](https://coinlaw.io/phantom-wallet-statistics/)、[Trust Wallet](https://coinlaw.io/trust-wallet-statistics/)、[OKX Wallet](https://coinlaw.io/okx-wallet-statistics/)、[Coinbase Wallet](https://coinlaw.io/coinbase-wallet-statistics/)、[Bitget Wallet](https://coinlaw.io/bitget-wallet-statistics/)、[SafePal](https://coinlaw.io/safepal-wallet-statistics/)、[Exodus](https://coinlaw.io/exodus-wallet-statistics/)、[Rabby](https://coinlaw.io/rabby-wallet-statistics/)、[Rainbow](https://coinlaw.io/rainbow-wallet-statistics/)、[Web3 钱包增长](https://coinlaw.io/web3-wallet-user-growth-statistics/)
- ratex.ai：[The Wallet Wars 2025](https://ratex.ai/blog/the-wallet-wars-2025-market-structure-revenue-models-and-user-behavior.3fe/)（MAU/DAU/ARPU/留存对比，部分数字偏高，已标注）
- DefiLlama：[MetaMask 费用与收入](https://defillama.com/protocol/metamask)
- Blockworks：[MetaMask MAU 新高](https://blockworks.co/news/metamask-monthly-active-users-blockaid)
- CNBC：[Telegram 钱包登陆美国](https://www.cnbc.com/2025/07/22/telegram-crypto-wallet-us.html)；TON Wallet 官方：[美国上线公告](https://wallet.tg/news/ton-wallet-launches-in-the-united-states-for-almost-87-m-telegram-users)
- Cryptonomist/Odaily：[Binance Wallet 日交易量破 $50 亿](https://en.cryptonomist.ch/2025/05/30/binance-wallet-surpasses-5-billion-dollars-in-daily-volume-web3-revolution-with-binance-alpha/)；PR Newswire：[Binance 2025 年报](https://www.prnewswire.com/in/news-releases/binances-2025-end-of-year-report-trust-liquidity-and-web3-discovery-302657209.html)
- Business of Apps：[OKX 统计](https://www.businessofapps.com/data/okx-statistics/)、[Coinbase 统计](https://www.businessofapps.com/data/coinbase-statistics/)
- AInvest：[Phantom C 轮](https://www.ainvest.com/news/phantom-wallet-surpasses-15m-users-raises-150m-in-series-c-2502101056503eb1b344c8b3/)
- Trust Wallet 官方：[2025 年报](https://trustwallet.com/blog/company/trust-wallet-in-2025-year-end-wrap-up)
- BCG：[稳定币支付白皮书 2026](https://www.bcg.com/assets/2026/white-paper-stablecoin-payments-truth-behind-numbers.pdf)
- SafePal 官方（[下载中心](https://www.safepal.com/en/download)）、TokenPocket 官方（[下载页](https://www.tokenpocket.pro/en/download/app)）
