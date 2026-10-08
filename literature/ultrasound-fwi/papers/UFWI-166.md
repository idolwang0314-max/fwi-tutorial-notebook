# UFWI-166 · Coarse-to-fine multi-resolution hash encoding for implicit full waveform inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Linrong Wang; Shaowen Wang; Fan Min; Tariq Alkhalifah
- 年份 / 期刊：2026 / arXiv
- 发表类型 / 状态：preprint / preprint
- 研究类型：地球物理及可迁移方法
- 主题：地球物理方法、preprint、earlier_supplement
- 核验程度：一手摘要
- 优先级：P2
- DOI：[10.48550/arxiv.2610.01081](https://doi.org/10.48550/arxiv.2610.01081)
- 作者列表：不完整，引用前请从出版社导出完整书目。
- 增补来源 ID：WL20261008-N09
- 2026-10-08 分类：earlier_supplement
- 本次日期窗判定日：2026-10-01
- 日期依据：arXiv v1 submission history; exact first announcement timestamp not independently verified

公开来源原始日期字段（冲突时采用上方处理说明）：

```json
{
  "submitted_utc": "2026-10-01T05:24:48Z",
  "submitted_beijing": "2026-10-01T13:24:48+08:00"
}
```

## 创新点 / 主要贡献

逐步激活hash resolution levels并平滑fade-in，约束早期高波数。

## 技术手段

coarse-to-fine IFWI；未激活level零梯度；随迭代增长模型容量而不增参数。

## 验证证据

Overthrust/BP2004模拟+Viking marine field；摘要已核。

## 局限与评估

尚未核全文预算；地震，不是超声；model capacity schedule不等于实测低频。

## 研究相关性

模型参数化渐进策略近邻；不能把粗到细神经参数化单独当原创。

## 公开来源

- [https://arxiv.org/abs/2610.01081](https://arxiv.org/abs/2610.01081)



核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
