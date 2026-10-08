# UFWI-165 · Radon–full-waveform inversion for suppressing scalp reverberation and skull-induced aberration in transcranial photoacoustic computed tomography

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Jiawen Zhang; Han Yang; Jintao Ma; Bangxu Fan; Tong Shi; Xiaoyan Zheng; Songqing Xie; Zhuojun Xie; Shuai Na
- 年份 / 期刊：2026 / Photoacoustics
- 发表类型 / 状态：journal / published
- 研究类型：相邻超声方法 / 硬件
- 主题：光声初始压力反演、弹性传播、Radon预处理、正则化
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.1016/j.pacs.2026.100833](https://doi.org/10.1016/j.pacs.2026.100833)
- 作者列表：不完整，引用前请从出版社导出完整书目。
- 增补来源 ID：WL20261008-N08
- 2026-10-08 分类：earlier_supplement
- 已记录首次公开日期：2026-04-29

公开来源原始日期字段（冲突时采用上方处理说明）：

```json
{
  "online": "2026-04-29",
  "issue": "2026-06"
}
```

## 创新点 / 主要贡献

Radon分离头皮多次波，并将其导出的掩膜进入后续初始光声压反演。

## 技术手段

高分辨linear Radon预处理；逆变换cleaned data；elastic FDTD+adjoint+FISTA；p0≥0、L1和scalp波场能量惩罚。

## 验证证据

2D模拟、acrylic phantom、ex-vivo human skull；已核全文Eq13、Fig2、Sec2.3/3.1。

## 局限与评估

反演变量是初始声压p0；vp/vs/ρ来自先验，Fig2声速由X-ray CT辅助。不是声速FWI，不是Radon域matching-filter损失。

## 研究相关性

头骨Radon-FWI邻近先例，必须防止与环阵USCT声速方法混同。

## 公开来源

- [https://www.sciencedirect.com/science/article/pii/S221359792600039X](https://www.sciencedirect.com/science/article/pii/S221359792600039X)
- [https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13156777/fullTextXML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13156777/fullTextXML)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC13156777/](https://pmc.ncbi.nlm.nih.gov/articles/PMC13156777/)



核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
