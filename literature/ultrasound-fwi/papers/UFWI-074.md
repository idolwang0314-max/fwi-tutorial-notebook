# UFWI-074 · Deep-Learning-Driven Full-Waveform Inversion for Ultrasound Breast Imaging

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Thomas Robins; Jorge Camacho; Oscar Calderon Agudo; Joaquin L Herraiz; Lluís Guasch
- 年份 / 期刊：2021 / Sensors
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：低频外推、深度学习、Imperial、低频补全、乳腺、实测体模
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.3390/s21134570](https://doi.org/10.3390/s21134570)
- Europe PMC日期（可能为卷期日；差异见备注）：2021-07-03

## 创新点 / 主要贡献

用学习外推缺失低频，改善窄带超声数据引发的FWI初值问题。

## 技术手段

U-Net CNN从窄带RF数据预测低频，再交给多尺度FWI。

## 验证证据

MUST2019数值数据及CIRS物理乳腺体模，含CT参照。

## 局限与评估

网络外推依赖训练分布；恢复低频的可信度与真实测量频率不同。

## 研究相关性

与AWI/FDWI比较时需区分数据外推与目标函数修改。

## 公开来源

- [https://doi.org/10.3390/s21134570](https://doi.org/10.3390/s21134570)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC8272012/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8272012/)

检索核验日期2026-09-26。正式2021-07-03。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
