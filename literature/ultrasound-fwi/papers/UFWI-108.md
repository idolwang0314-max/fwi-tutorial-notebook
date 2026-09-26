# UFWI-108 · Full waveform inversion guided wave tomography with a recurrent neural network

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Zijian Wang; Jingyi Xiao; Dan Li; Boyi Li; JianQiu Zhang; Dean Ta
- 年份 / 期刊：2023 / Ultrasonics
- 发表类型 / 状态：journal / published
- 研究类型：超声 NDT / 导波 FWI
- 主题：NDT、导波、自动微分、最优传输
- 核验程度：一手摘要
- 优先级：P1
- DOI：[10.1016/j.ultras.2023.107043](https://doi.org/10.1016/j.ultras.2023.107043)
- Europe PMC日期（可能为卷期日；差异见备注）：2023-05-14

## 创新点 / 主要贡献

把声学传播写为循环计算图，并结合W2和DIP改善导波厚度反演。

## 技术手段

RNN正演；自动微分；Adam；U-Net deep image prior；色散转换厚度。

## 验证证据

数值及实测优于常规时域FWI的收敛、初模和鲁棒性。

## 局限与评估

RNN在此主要实现PDE迭代，不宜误称完全学习的无模型反演；各组件贡献需消融。

## 研究相关性

研究DIP、优化器与损失函数复合方法时很值得读。

## 公开来源

- [https://doi.org/10.1016/j.ultras.2023.107043](https://doi.org/10.1016/j.ultras.2023.107043)
- [https://pubmed.ncbi.nlm.nih.gov/37216858/](https://pubmed.ncbi.nlm.nih.gov/37216858/)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37216858&format=json&resultType=core](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37216858&format=json&resultType=core)

核验作者原始摘要（出版社页面或PubMed/EuropePMC原文摘要）；非全文精读。最早公开日 2023-05-14；正式卷期 2023 Aug。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
