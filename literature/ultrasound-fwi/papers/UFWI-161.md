# UFWI-161 · Robust Ensemble Guidance for Scientific Inverse Problems

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Zixiang Li; Wei Wang; Yunchao Wei; Yao Zhao; Yue Song
- 年份 / 期刊：2026 / arXiv
- 发表类型 / 状态：preprint / preprint
- 研究类型：地球物理及可迁移方法
- 主题：地球物理方法、preprint、weekly_new_publication
- 核验程度：一手摘要
- 优先级：P2
- DOI：[10.48550/arxiv.2610.05371](https://doi.org/10.48550/arxiv.2610.05371)
- 增补来源 ID：WL20261008-N04
- 2026-10-08 分类：weekly_new_publication
- 本次日期窗判定日：2026-10-05
- 日期依据：arXiv v1 submission history; exact first announcement timestamp not independently verified
- arXiv 提交 UTC：2026-10-04T16:54:37+00:00
- arXiv 提交北京时间：2026-10-05T00:54:37+08:00

公开来源原始日期字段（冲突时采用上方处理说明）：

```json
{
  "submitted_utc": "2026-10-04T16:54:37Z",
  "submitted_beijing": "2026-10-05T00:54:37+08:00"
}
```

## 创新点 / 主要贡献

对ensemble guidance做预测离散度加权与标准化残差自适应裁剪。

## 技术手段

预训练diffusion prior+黑盒正演；复用已有粒子与预测；线性Gaussian局部风险分析。

## 验证证据

Navier–Stokes、黑洞、acoustic FWI数值任务；摘要已核。

## 局限与评估

依赖预训练扩散与ensemble；不因两项校正无额外正演就认为整个反演廉价；无USCT证据。

## 研究相关性

跟踪生成式反演的鲁棒数据校正；评估完整正演成本与先验依赖。

## 公开来源

- [https://arxiv.org/abs/2610.05371](https://arxiv.org/abs/2610.05371)

；本周/边界分类依arXiv v1提交记录，北京时间已换算；未将精确提交时刻冒充首次公告时刻。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
