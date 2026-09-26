# UFWI-142 · SSI-Net: a hybrid physics-constrained deep learning framework for quantitative ultrasound speed-of-sound reconstruction

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Sun Zheng; Jiang Qian; Gao Zhangshuo; Sheng Yangjie
- 年份 / 期刊：2026 / Physics in Medicine & Biology
- 发表类型 / 状态：journal / published
- 研究类型：相邻超声方法 / 硬件
- 主题：深度学习、PDE约束训练、非线性声学、直接学习
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.1088/1361-6560/ae5374](https://doi.org/10.1088/1361-6560/ae5374)
- Europe PMC日期（可能为卷期日；差异见备注）：2026-04-08

## 创新点 / 主要贡献

把可微Westervelt时域求解器嵌入数据到声速网络训练。

## 技术手段

BiGRU编码；U-Net解码；数据/物理残差联合损失；两阶段训练。

## 验证证据

模拟、组织仿体与在体小鼠；摘要报告物理残差降25.6%–57.5%、109.4ms/样本。

## 局限与评估

物理约束在训练阶段，不等同每例迭代FWI；所谓精确求解器仍有离散误差。

## 研究相关性

适合比较带PDE训练约束与纯学习USCT的可靠性。

## 公开来源

- [https://doi.org/10.1088/1361-6560/ae5374](https://doi.org/10.1088/1361-6560/ae5374)
- [https://pubmed.ncbi.nlm.nih.gov/41843981/](https://pubmed.ncbi.nlm.nih.gov/41843981/)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41843981&format=json&resultType=core](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41843981&format=json&resultType=core)

仅核验EuropePMC缓存中完整作者摘要和书目；未全文精读。最早公开2026-04-08；卷期2026 Apr。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
