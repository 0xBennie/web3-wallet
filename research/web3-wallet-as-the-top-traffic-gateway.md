# 研究报告：Web3 Wallet 为什么是流量的第一入口

> 数据截至 2026 年 8 月，来源见文末。部分数据来自第三方统计站点（CoinLaw、SQ Magazine、Dune、DefiLlama 等），不同口径之间会有出入，文中已尽量注明口径。

---

## 一、核心结论（TL;DR）

1. **规模上**，钱包是 Web3 装机量最大的产品品类：全球活跃加密钱包用户 2025 年超过 **8.2 亿**（约占全球互联网人口 15%），全球加密资产持有者约 **7.41 亿**（同比 +12.4%）。
2. **行为上**，几乎所有链上行为（交易、签名、支付、登录 dApp）都必须经过钱包：2025 年 Q2 dApp 日活独立钱包达 **2430 万，同比 +247%**；约 **48% 的钱包**至少与 dApp 交互过一次。
3. **变现上**，钱包已经证明了"入口即生意"：MetaMask 累计 swap 收入约 **1.99 亿～3.25 亿美元**（不同口径），Phantom 2025 年收入 **7910 万美元**（协议总收入口径高达 3.26 亿美元），估值 **30 亿美元**。
4. **竞争上**，所有巨头都在用真金白银投票：Binance、OKX、Bitget、Coinbase 全部重仓自营钱包，Telegram 直接把 TON 钱包内置进 App（激活用户超 **1.1 亿**）。
5. 钱包之于 Web3，类似浏览器/超级 App 之于 Web2：它同时垄断了**账户（私钥）、路由（默认 swap/跳转）、支付（稳定币/Gas）** 三层，因此是流量的第一入口。

---

## 二、什么叫"流量第一入口"

判断一个产品是不是流量第一入口，看四个标准：

| 标准 | Web2 类比 | Web3 中的钱包 |
|---|---|---|
| 用户必经 | 浏览器 / 应用商店 | 任何链上操作都要钱包签名 |
| 高频打开 | 微信 / 搜索框 | 查资产、转账、签名、连接 dApp |
| 掌握路由 | 默认搜索引擎 | 内置 swap 路由、dApp 浏览器、跳转推荐 |
| 能收"过路费" | 广告 / 分发抽成 | swap 费、跨链费、法币入金抽成、质押抽成 |

下面用数据逐条验证。

---

## 三、数据一：用户规模 —— 钱包是 Web3 装机量最大的品类

### 3.1 行业整体

- 2025 年全球活跃加密钱包用户突破 **8.2 亿**，约占全球互联网人口的 **15%**。
- 全球加密资产持有者 2025 年达到 **7.41 亿**，同比增长 12.4%。
- 区域分布：亚太约 **3.5 亿**（占 43%）、欧洲约 **1.4 亿**、北美约 **1.34 亿**、拉美约 **9200 万**、非洲约 **7500 万**（增速最快）。
- 口径提示：截至 2024 年底，每月活跃的链上地址约 **2.2 亿**，对应真实自然人估计为 **3000 万～6000 万**（一人多钱包现象普遍）。引用数据时需区分"地址数"与"真实用户数"。

### 3.2 头部钱包产品（2025–2026）

| 钱包 | 关键数据 | 备注 |
|---|---|---|
| MetaMask | **MAU 超 3000 万**；累计下载 **1.43 亿** | MAU 从 2025 年 9 月的 1900 万涨到 2026 年 1 月的 3000 万+（4 个月 +55%），接近 2022 年 1 月历史峰值 3170 万；已在评估 IPO |
| Trust Wallet | 累计下载 **2 亿+**（2025.3）；**MAU 约 6000 万**；2025 年底 MAU 市场份额约 **35%** | Binance 系，移动端为主 |
| Phantom | MAU 从年初 **1500 万**涨到年底近 **2000 万**（峰值口径约 1700 万，同比 5 倍） | 2025.1 完成 Sequoia 领投 1.5 亿美元 C 轮，估值 **30 亿美元** |
| Bitget Wallet | 宣称用户 **8000 万**（2025 年中）；**MAU 1200 万+**（2025.8，当月全球下载量第一） | 交易所系 |
| Telegram TON Wallet | 累计激活 **1.1 亿+**（2025）；2025.7 向 **8700 万**美国用户开放 | 内置于 Telegram，TON 生态 Mini App 超 1000 个（较 2025.7 +25%） |

**要点**：单是头部五家钱包的 MAU 合计就超过 1.2 亿，而全球所有 Web3 dApp 的独立 MAU 只有约 500 万～1000 万（网站/前端口径）——**钱包的用户盘子比任何一类 dApp 大一个数量级**，dApp 反而要依附钱包获客。

---

## 四、数据二：使用行为 —— 一切链上行为都从钱包开始

- 2025 年 Q2，dApp 的**日活独立钱包（dUAW）达 2430 万，较 2024 年增长 247%**——每一个 dApp 活跃用户，本质上都是先打开了一次钱包。
- 约 **48% 的钱包**至少与一个 dApp 交互过。
- **72% 的用户偏好移动端钱包**，浏览器插件钱包只占约 12% 的使用量——移动钱包 App（自带 dApp 浏览器、内置交易）正在成为主导形态，钱包因此更像"超级 App"而不是"插件工具"。
- 转化漏斗数据：一个协议网站每 **200 个访客中约 10 人连接钱包、仅 1 人完成交易**（约 0.5% 转化）。反过来看：**"连接钱包"是整个 Web3 获客漏斗中最窄的一环，谁掌握钱包，谁就掌握漏斗的咽喉**。
- 钱包正在从"通道"变成"目的地"：主流钱包已内置 swap、跨链桥、质押、行情、dApp 商店，用户可以不离开钱包完成大部分链上操作（详见第五节的交易量数据）。

---

## 五、数据三：钱包截流了交易量与收入 —— 入口价值的变现证明

"第一入口"不是概念，头部钱包已经把入口位置变成了现金流：

### 5.1 MetaMask

- 内置 swap 费率 **0.875%**，ETH 质押抽成 **10%**。
- 累计收入：约 **1.9864 亿美元**（CoinLaw 口径）；DefiLlama 口径的累计 swap 收入约 **3.25 亿美元**，其中以太坊链贡献约 1.4 亿美元、BSC 约 2930 万、Arbitrum 约 747 万、Polygon 约 717 万。
- 单用户年化收入约 **10.8 美元**，几乎全部来自 swap 抽成——一个"免费工具"靠入口位置做成了持续现金流业务。
- 2025.10 上线**最高 40 倍杠杆的永续合约**；同时推出原生稳定币 **mUSD** 和 **MetaMask Card**（链上资产直接线下消费）——钱包在向"交易所 + 银行账户"扩张。

### 5.2 Phantom

- 2025 年收入 **7910 万美元**（周峰值收入曾达 4414 万美元的口径亦有报道）；更宽的"协议总收入"口径为 **3.2589 亿美元**。
- 内置 swap 周交易笔数峰值 **1000 万笔**，2025 年 1 月单月 swap 交易量 **57 亿美元**。
- 峰值时期，Phantom 内置 swap 占 **Solana 全网转账量的 10%以上**，2024 年末数周曾达 **20%**——单个钱包就吃掉了一条公链五分之一的交易流。

### 5.3 其他

- Ronin Wallet 2025 年初周 swap 交易量峰值超 **5500 万美元**。
- 行业趋势：钱包普遍内置 1inch、LI.FI 等聚合路由，**钱包决定用户的交易走哪个 DEX**——这正是 Web2 中"浏览器决定默认搜索引擎"的翻版，而 Google 每年为这个默认位置向 Apple 支付 200 亿美元量级的费用。

---

## 六、数据四：巨头的行为投票 —— 所有大厂都在抢钱包

- **交易所全员下场**：Binance（Trust Wallet + Binance Web3 Wallet）、OKX（OKX Wallet）、Bitget（Bitget Wallet，8000 万用户）、Coinbase（Coinbase Wallet + Base 链）。交易所做钱包的逻辑很直白：中心化交易是存量生意，链上流量入口是增量生意，且钱包能把用户导回自家链（BSC、Base）形成闭环。
- **Telegram 把钱包做成系统级功能**：TON Wallet 累计激活超 **1.1 亿**，2025 年 7 月向 8700 万美国用户开放，内置转账、swap、质押、MoonPay 零费入金，并直连 1000+ Mini App——这是"超级 App 内嵌钱包"路线的最大实验。
- **稳定币支付把钱包推向主流**：2025 年零售稳定币交易规模**增长约 10 倍**（The Paypers）；BCG 2026 白皮书指出，目前约 **2/3 的消费者对商户（C2M）稳定币支付仍从交易所账户发起**——这说明支付入口之争尚未定局，也正是钱包厂商发稳定币（如 MetaMask mUSD）、发卡（MetaMask Card）猛攻的原因：**谁赢下稳定币支付的默认发起端，谁就是下一个支付宝级入口**。

---

## 七、机制分析：为什么偏偏是钱包

1. **账户层垄断（身份）**：私钥即账户。Web2 的账户体系分散在各平台手里，Web3 的账户天然只在钱包里，dApp 无法绕过。"Connect Wallet" 是 Web3 唯一的通用登录按钮。
2. **高频刚需（打开率）**：查余额、收付款、签名授权是加密用户的日常动作，频次远高于任何单一 dApp，钱包因此获得类似 IM/浏览器的打开频率。
3. **路由权（分发）**：内置 swap 聚合、dApp 商店、行情页和推荐位，让钱包决定"用户下一步去哪"。Phantom 吃掉 Solana 10–20% 转账量、MetaMask 单用户年收 $10.8，都是路由权的直接变现。
4. **支付终局（现金流）**：稳定币 + 钱包 + 卡组织的组合正在打通"链上资产—现实消费"，钱包是唯一同时握有用户私钥和支付通道的角色。
5. **超级 App 化（生态位扩张）**：从工具 → 聚合平台 → 交易所化（perp）→ 银行化（稳定币、卡）。钱包在复刻微信/支付宝"从工具到操作系统"的路径。

---

## 八、反方观点与风险（做研究必须诚实）

- **真实用户远小于地址数**：8.2 亿是"钱包/地址"口径，真实月活自然人估计仅 3000 万～6000 万。讲"第一入口"时规模没有 Web2 超级 App 大，但增速和垄断性成立。
- **交易所仍是最大对手**：2/3 的稳定币消费支付仍从交易所账户发起；对多数新用户，第一入口其实是 CEX App，自托管钱包是第二站。
- **转化效率低**：0.5% 的访客-交易转化率说明入口虽窄但漏损巨大，钱包的商业价值依赖行情周期（Phantom 收入与 Solana meme 行情高度相关）。
- **同质化与费率压力**：swap 抽成 0.875% 在聚合器竞争下长期承压；MEV、免费路由（如交易所钱包零费补贴）都可能侵蚀钱包的"过路费"模式。

---

## 九、结论

Web3 钱包同时占住了**账户、路由、支付**三个卡口，装机规模比所有 dApp 大一个数量级，且已被 MetaMask/Phantom 的收入数据证明可以规模化变现，被 Binance/Coinbase/Telegram 的战略投入证明是共识级赛道。因此：**钱包是 Web3 流量的第一入口，其地位相当于 Web2 时代的浏览器 + 应用商店 + 支付账户三合一。** 下一阶段的胜负手在稳定币支付的默认发起端和移动端超级 App 化。

---

## 十、数据来源

- CoinLaw — [MetaMask Wallet Statistics](https://coinlaw.io/metamask-wallet-statistics/) / [Phantom Wallet Statistics](https://coinlaw.io/phantom-wallet-statistics/) / [Web3 Wallet User Growth Statistics](https://coinlaw.io/web3-wallet-user-growth-statistics/) / [Crypto Wallet Market Share Statistics](https://coinlaw.io/crypto-wallet-market-share-statistics/) / [Trust Wallet Statistics](https://coinlaw.io/trust-wallet-statistics/) / [Bitget Wallet Statistics](https://coinlaw.io/bitget-wallet-statistics/)
- SQ Magazine — [MetaMask Statistics](https://sqmagazine.co.uk/metamask-wallet-statistics/) / [Phantom Statistics](https://sqmagazine.co.uk/phantom-wallet-statistics/) / [Trust Wallet Statistics](https://sqmagazine.co.uk/trust-wallet-statistics/) / [Cryptocurrency Wallet Adoption Statistics](https://sqmagazine.co.uk/cryptocurrency-wallet-adoption-statistics/)
- Blockworks — [MetaMask monthly active users nears all-time high](https://blockworks.co/news/metamask-monthly-active-users-blockaid)
- Bitcoin Magazine — [MetaMask Launches Native Bitcoin Integration For 30 Million Active Users](https://bitcoinmagazine.com/business/metamask-launches-native-bitcoin-integration-for-30-million-active-users)
- DefiLlama — [MetaMask Fees & Revenue](https://defillama.com/protocol/metamask)
- Dune Analytics — [Wallet Report v2](https://dune.com/blog/wallet-report-v2)
- CNBC — [Telegram's crypto wallet goes live to its 87 million U.S. users](https://www.cnbc.com/2025/07/22/telegram-crypto-wallet-us.html)
- TON Wallet — [TON Wallet launches in the United States](https://wallet.tg/news/ton-wallet-launches-in-the-united-states-for-almost-87-m-telegram-users)
- AInvest — [Phantom Wallet Surpasses 15M Users, Raises $150M Series C](https://www.ainvest.com/news/phantom-wallet-surpasses-15m-users-raises-150m-in-series-c-2502101056503eb1b344c8b3/)
- Trust Wallet — [Trust Wallet in 2025: Year-End Wrap Up](https://trustwallet.com/blog/company/trust-wallet-in-2025-year-end-wrap-up)
- BCG — [Stablecoin Payments: The Truth Behind the Numbers (2026 White Paper)](https://www.bcg.com/assets/2026/white-paper-stablecoin-payments-truth-behind-numbers.pdf)
- The Paypers — [Retail stablecoin transactions scale tenfold in 2025](https://thepaypers.com/crypto-web3-and-cbdc/news/retail-stablecoin-transactions-surge-tenfold-in-2025)
- PatentPC — [Web3 User Stats: Wallet Connections, dApp Retention & Growth](https://patentpc.com/blog/web3-user-stats-wallet-connections-dapp-retention-growth)
- Medium/Coinmonks — [Beyond Custody: How Wallets Are Becoming the Super Entry Point of Web3](https://medium.com/coinmonks/ddc-insights-beyond-custody-how-wallets-are-becoming-the-super-entry-point-of-web3-71b928c2e622)
