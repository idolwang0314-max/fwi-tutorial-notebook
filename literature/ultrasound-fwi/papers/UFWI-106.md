# UFWI-106 · A multi-task neural network for full waveform ultrasonic bone imaging

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Peiwen Li; Tianyu Liu; Heyu Ma; Dan Li; Chengcheng Liu; Dean Ta
- 年份 / 期刊：2025 / Computer Methods and Programs in Biomedicine
- 发表类型 / 状态：journal / published
- 研究类型：相邻超声方法 / 硬件
- 主题：深度学习、骨、相邻方法
- 核验程度：一手摘要
- 优先级：P2
- DOI：[10.1016/j.cmpb.2025.108807](https://doi.org/10.1016/j.cmpb.2025.108807)
- Europe PMC日期（可能为卷期日；差异见备注）：2025-04-25

## 创新点 / 主要贡献

双解码器联合预测骨声速和骨/软组织边界。

## 技术手段

CEDD-Unet；ConvLSTM；多尺度注意力；边界辅助任务。

## 验证证据

人/鼠骨模型数据集报告SSIM0.9702/0.9550，含网络消融。

## 局限与评估

摘要未足够区分真实采集与模拟数据；属于监督直接反演，不能等同物理迭代FWI。

## 研究相关性

提供边界任务作为先验的思路，但阅读优先低于有实验的物理FWI。

## 公开来源

- [https://doi.org/10.1016/j.cmpb.2025.108807](https://doi.org/10.1016/j.cmpb.2025.108807)
- [https://pubmed.ncbi.nlm.nih.gov/40311439/](https://pubmed.ncbi.nlm.nih.gov/40311439/)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40311439&format=json&resultType=core](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40311439&format=json&resultType=core)

核验作者原始摘要（出版社页面或PubMed/EuropePMC原文摘要）；非全文精读。最早公开日 2025-04-25；正式卷期 2025 Jul。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
