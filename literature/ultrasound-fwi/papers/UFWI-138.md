# UFWI-138 · High-fidelity three-dimensional reconstruction of musculoskeletal tissues via diffusion based ultrasonic computed tomography

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Tianyu Liu; Heyu Ma; Peiwen Li; Aiduo Wang; Wenming Chen; Chengcheng Liu; Boyi Li; Dean Ta
- 年份 / 期刊：2026 / Medical Image Analysis
- 发表类型 / 状态：journal / published
- 研究类型：相邻超声方法 / 硬件
- 主题：扩散模型、肌骨、切片三维显示、直接学习
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.1016/j.media.2026.104141](https://doi.org/10.1016/j.media.2026.104141)
- Europe PMC日期（可能为卷期日；差异见备注）：2026-05-23

## 创新点 / 主要贡献

结合注意力特征提取与扩散精化实现快速肌骨参数切片重建。

## 技术手段

DiffUCT两阶段架构；10步扩散采样；逐片结果形成体积显示。

## 验证证据

下肢数据集报告PSNR37.78dB/SSIM0.9734/LPIPS0.0097，0.126秒/片，较选定FWI约4000倍。

## 局限与评估

切片重建不是三维PDE-FWI；训练成本、真实参数真值和分布外可靠性需全文核验。

## 研究相关性

最新快速USCT替代路线，与生成神经物理2508.12226为不同论文不可误合并。

## 公开来源

- [https://doi.org/10.1016/j.media.2026.104141](https://doi.org/10.1016/j.media.2026.104141)
- [https://pubmed.ncbi.nlm.nih.gov/42214247/](https://pubmed.ncbi.nlm.nih.gov/42214247/)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42214247&format=json&resultType=core](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42214247&format=json&resultType=core)

仅核验EuropePMC缓存中完整作者摘要和书目；未全文精读。最早公开2026-05-23；卷期2026 Jul。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
