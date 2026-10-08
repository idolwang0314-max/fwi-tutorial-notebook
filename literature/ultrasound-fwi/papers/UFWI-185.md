# UFWI-185 · Elastic Full-Waveform Inversion for Transcranial Ultrasound Computed Tomography using Optimal Transport

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Patrick Marty; Christian Boehm; Andreas Fichtner
- 年份 / 期刊：2022 / 2022 IEEE International Ultrasonics Symposium (IUS)
- 发表类型 / 状态：conference / published
- 研究类型：医学超声 FWI
- 主题：弹性FWI、经颅、graph-space optimal transport、源编码、固定颅骨先验
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.1109/ius54386.2022.9957394](https://doi.org/10.1109/ius54386.2022.9957394)
- 增补来源 ID：HIST20261008-M04
- 2026-10-08 分类：historical_backfill

日期冲突处理：

```json
{
  "published": "2022-10-10",
  "basis": "Crossref published-print (proceedings date)",
  "crossref_created": "2022-12-01T20:54:16Z",
  "event_start": "2022-10-10",
  "event_end": "2022-10-13",
  "note": "不将 DOI 登记时间误作首次公开日；未另核 Xplore 首次上线日。"
}
```

一手材料阅读范围：作者上传完整 4 页；重点 §II、§III-A–C、Fig.3 与结论。

## 创新点 / 主要贡献

在耦合声弹经颅 FWI 中使用 graph-space optimal transport 缓解相位失配，并利用源编码减少正演。

## 技术手段

Salvus SEM/贴体全四边形网格；RTM 构造颅骨轮廓；graph-space OT；500 kHz Ricker、多尺度低通、梯度平滑和 OT 最大时移递减；512 源编码为16个 supersources。

## 验证证据

MIDA 派生二维合成脑模型；实际执行脑内参数 FWI。

## 局限与评估

§III-C 和 Fig.3 明确固定头皮/颅骨材料与颅骨形状，仅更新脑内部；非骨参数联合恢复、非实测验证，不能据此证明未知颅骨条件下稳健。

## 研究相关性

最直接的经颅 elastic FWI+OT 方法先例；用于拆分物理准确性与强结构先验。

## 公开来源

- [https://doi.org/10.1109/IUS54386.2022.9957394](https://doi.org/10.1109/IUS54386.2022.9957394)
- [https://ieeexplore.ieee.org/document/9957394/](https://ieeexplore.ieee.org/document/9957394/)
- [https://www.researchgate.net/publication/365942138_Elastic_Full-Waveform_Inversion_for_Transcranial_Ultrasound_Computed_Tomography_using_Optimal_Transport](https://www.researchgate.net/publication/365942138_Elastic_Full-Waveform_Inversion_for_Transcranial_Ultrasound_Computed_Tomography_using_Optimal_Transport)
- [https://pmarty.ch/publications/](https://pmarty.ch/publications/)

本轮历史机制补漏，不是2026-10-02至10-08新发表。阅读范围：作者上传完整 4 页；重点 §II、§III-A–C、Fig.3 与结论。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
