# UFWI-113 · Quantitative ultrasound brain imaging with multiscale deconvolutional waveform inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Yu-Bing Li; Jian Wang; Chang Su; Wei-Jun Lin; Xiu-Ming Wang; Yi Luo
- 年份 / 期刊：2023 / Chinese Physics B
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：解卷积、AWI相关、经颅、多尺度
- 核验程度：一手全文/相关段落
- 优先级：P0；精读第 24 篇
- DOI：[10.1088/1674-1056/ac6dad](https://doi.org/10.1088/1674-1056/ac6dad)
- 2026-10-08 分类：existing_fulltext_reverification

2026-10-08 复核备注：全文边界复核：本轮重读既有正式 PDF 提取文本 pp.014303-5/6/9/10（§2.3、§3.1、§3.5），核期刊作者/摘要页；2026-09-27 原 PDF 视觉审阅已排除 HTML 多余字符，不声称本轮再次视觉检查。

一手材料阅读范围：本轮重读既有正式 PDF 提取文本 pp.014303-5/6/9/10（§2.3、§3.1、§3.5），核期刊作者/摘要页；2026-09-27 原 PDF 视觉审阅已排除 HTML 多余字符，不声称本轮再次视觉检查。

## 创新点 / 主要贡献

以有限长度 Wiener filter 的 lag 支撑递减实现四阶段 MDWI，由大尺度到细节完成同一目标家族的重建，无需末尾改为 L2-FWI。

## 技术手段

二维常密度声学；观测→预测反卷积；目标分子为 T(τ)w²、T=|τ|/τmax；四阶段各100迭代，均用100–300 kHz；源峰200 kHz，均匀水速1500 m/s初模，反演逐源估波形。

## 验证证据

两张 CT 派生二维脑模型的合成超声实验；48源/288接收；§3.5明确不需换目标精化。

## 局限与评估

非超声实测或3D/弹性验证；CT来源不使超声重建变为在体验证。PDF014303-5同时写初始lag5μs、四阶段25/12.5/5/2.5μs及每阶段减半，三者不一致，不能擅自选一组当复现参数。有限长度求解/稳定化披露仍不足；频带100–300 kHz不能外推到严格≥0.5 MHz。

## 研究相关性

与AWI机理研究直接相关，是李玉冰方法主线必读。

## 排序理由

李玉冰团队解卷积波形反演与AWI最接近的必查先行工作，创新定位不能跳过。

## 公开来源

- [https://cpb.iphy.ac.cn/en/article/doi/10.1088/1674-1056/ac6dad](https://cpb.iphy.ac.cn/en/article/doi/10.1088/1674-1056/ac6dad)
- [https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/ac6dad.pdf](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/ac6dad.pdf)

正式Chin. Phys. B32(1)014303为2023；online2022-05-07保留原记录。本轮新增全文方法/局限核验，未另改日期。§3.5为MDWI-only，不能归为AWI→L2。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
