# UFWI-037 · Ultrasound computed tomography based on full waveform inversion with source directivity calibration

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Xiaoqing Wu; Yubing Li; Chang Su; Panpan Li; Xiangda Wang; Weijun Lin
- 年份 / 期刊：2023 / Ultrasonics
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：三维加速专题、D/C；2D simulation 与 experiment、源校准、时域、实验
- 核验程度：一手摘要
- 优先级：P0；精读第 10 篇
- DOI：[10.1016/j.ultras.2023.107004](https://doi.org/10.1016/j.ultras.2023.107004)
- Europe PMC日期（可能为卷期日；差异见备注）：2023-04-12
- 2026-10-08 分类：existing_reviewed
- 2026-10-08 专题阅读：第 3 篇，见 [专题顺序](../PROJECT_READING_20261008.md)；不改变历史主榜。

2026-10-08 复核备注：本轮重新读出版商摘要/引言：target-free water FMC、weighted virtual source、解析均匀介质求梯度；外部水校准，不同于在目标数据中无约束自由源。

2026-10-08 专题阅读理由：理解换能器指向性与点源假设的偏差，以及独立水槽校准的作用。

## 创新点 / 主要贡献

用无目标水槽FMC自检换能器方向性，再以加权虚拟点阵表示源。

## 技术手段

解析传播求权重；局部梯度优化；时域有限差分FWI。

## 验证证据

数值偶极/四极源及512元环阵实测表明校准减少点源失配伪影。

## 局限与评估

主要为发射方向性校准，不能据此认为位置/接收/三维响应均已解决。

## 研究相关性

李玉冰主线实验落地必读，源误差可能比新目标函数更先限制重建。

## 排序理由

水槽校准与虚拟点源权重有明确实现路径和环阵实测，是声源方向性建模的实用对照。

## 公开来源

- [https://doi.org/10.1016/j.ultras.2023.107004](https://doi.org/10.1016/j.ultras.2023.107004)
- [https://pubmed.ncbi.nlm.nih.gov/37071945/](https://pubmed.ncbi.nlm.nih.gov/37071945/)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37071945&format=json&resultType=core](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37071945&format=json&resultType=core)

核验作者原始摘要（出版社页面或PubMed/EuropePMC原文摘要）；非全文精读。最早公开日 2023-04-12；正式卷期 2023 Jul。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
