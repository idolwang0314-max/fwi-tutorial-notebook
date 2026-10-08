# UFWI-189 · Level Set–Based Shape Optimization Approach for Sharp-Interface Reconstructions in Time-Domain Full Waveform Inversion

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Yuri F. Albuquerque; Antoine Laurain; Irwin Yousept
- 年份 / 期刊：2021 / SIAM Journal on Applied Mathematics
- 发表类型 / 状态：journal / published
- 研究类型：地球物理及可迁移方法
- 主题：level-set、shape derivative、已知分区材料、地球物理可迁移方法
- 核验程度：一手全文/相关段落
- 优先级：P2
- DOI：[10.1137/20m1378090](https://doi.org/10.1137/20m1378090)
- 增补来源 ID：HIST20261008-P02
- 2026-10-08 分类：historical_backfill

日期冲突处理：

```json
{
  "published_online": "2021-05-20",
  "basis": "正式论文首页明确published electronically May 20, 2021；期刊81(3):939–964。",
  "accepted": "2021-01-21",
  "received": "2020-11-03",
  "note": "本次Crossref单条请求返回429；作者名/DOI/卷页/日期由正式PDF直接核验，未将该请求记为核验成功。"
}
```

一手材料阅读范围：作者机构托管全文的首页、§1、§6、§7；关键公式/算例段核对，未对§2–5全部证明逐行精读。

## 创新点 / 主要贡献

为含不连续系数的时域声学FWI建立形状优化框架，以distributed shape derivative和level-set恢复尖锐界面，避免一般平滑正则对界面的过度平滑。

## 技术手段

已知分区常声速的声学波动方程；distributed shape derivative；H1椭圆问题求平滑下降向量场；level-set演化。数值示例使用10shots、80receivers、200×130网格。

## 验证证据

作者机构托管正式全文已核首页、引言及§6–7方法/算例；1/2/3盐体分别从1/2/3初始体开始。正文将声速区域值设为已知，不是材料常数与界面的联合恢复证据。

## 局限与评估

只部分阅读全文，未逐行审定理证明或复现数值。地震声学合成例；已知分区材料且初始体数对应真值体数，不能用这些例子声称未知拓扑搜索、骨材料联合恢复或医学实测有效。

## 研究相关性

时域level-set形状FWI及平滑形状下降方向已有直接方法先例；后续研究可比较有限预算路径与先验失效边界，但复杂度递进不能被包装为首个形状/level-set FWI。

## 公开来源

- [https://doi.org/10.1137/20M1378090](https://doi.org/10.1137/20M1378090)
- [https://www.uni-due.de/imperia/md/content/mathematik/agyousept/siap_aly2021.pdf](https://www.uni-due.de/imperia/md/content/mathematik/agyousept/siap_aly2021.pdf)

历史方法先例补漏，不计入2026-10-02至10-08首次发表。阅读范围：作者机构托管全文的首页、§1、§6、§7；关键公式/算例段核对，未对§2–5全部证明逐行精读。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
