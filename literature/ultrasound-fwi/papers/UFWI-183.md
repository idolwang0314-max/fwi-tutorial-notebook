# UFWI-183 · Towards elastic bone characterization in transcranial ultrasound

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Patrick Marty; Trevor M. Mitcham; Rehman Ali; Christian Boehm; Nebojsa Duric; Andreas Fichtner
- 年份 / 期刊：2024 / Medical Imaging 2024: Ultrasonic Imaging and Tomography
- 发表类型 / 状态：conference / published
- 研究类型：相邻超声方法 / 硬件
- 主题：离体颅骨、RTM、声弹耦合、源标定、形状梯度
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.1117/12.3006769](https://doi.org/10.1117/12.3006769)
- 增补来源 ID：HIST20261008-M02
- 2026-10-08 分类：historical_backfill

日期冲突处理：

```json
{
  "published": "2024-04-01",
  "basis": "Crossref proceedings publication",
  "event_start": "2024-02-18",
  "event_end": "2024-02-23"
}
```

一手材料阅读范围：作者上传的完整 14 页论文；重点 §2、§3.1–3.4、§4、§5 与 Fig.10。

## 创新点 / 主要贡献

将水槽源标定、RTM 骨界面估计与耦合声弹背景建模串接，改善颅内目标定位，并展示材料/形状敏感度。

## 技术手段

1024 元环阵离体颅骨数据；逐源反卷积标定；RTM 定界；贴合界面网格与 coupled acoustic-viscoelastic SEM；在修正背景重新 RTM。

## 验证证据

水填充/凝胶及包涵体两种离体配置；§4 展示 Vs 梯度与 shape derivatives。

## 局限与评估

§3.4 明确初模尚未经过 FWI 优化；已展示的是 RTM 与梯度，§4–5 的交替 FWI/shape 优化属后续路线；2D、单颅骨，材料多取文献值，残余伪影。

## 研究相关性

防止把 RTM 初模和敏感度图误报成实测定量骨 FWI；也界定 shape/FWI 先例。

## 公开来源

- [https://doi.org/10.1117/12.3006769](https://doi.org/10.1117/12.3006769)
- [https://www.researchgate.net/publication/379501192_Towards_elastic_bone_characterization_in_transcranial_ultrasound](https://www.researchgate.net/publication/379501192_Towards_elastic_bone_characterization_in_transcranial_ultrasound)
- [https://pmarty.ch/publications/](https://pmarty.ch/publications/)

本轮历史机制补漏，不是2026-10-02至10-08新发表。阅读范围：作者上传的完整 14 页论文；重点 §2、§3.1–3.4、§4、§5 与 Fig.10。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
