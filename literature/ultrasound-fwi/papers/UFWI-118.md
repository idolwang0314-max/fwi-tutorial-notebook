# UFWI-118 · Stabilized adaptive waveform inversion for enhanced robustness in Gaussian penalty matrix parameterization and transcranial ultrasound imaging

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Jun-Jie Zhao; Shan-Mu Jin; Yue-Kun Wang; Yu Wang; Ya-Hui Peng
- 年份 / 期刊：2025 / Chinese Physics B
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：AWI、Wiener滤波、经颅、稳定性
- 核验程度：一手全文/相关段落
- 优先级：P1
- DOI：[10.1088/1674-1056/add4f3](https://doi.org/10.1088/1674-1056/add4f3)
- 2026-10-08 分类：existing_fulltext_reverification

日期冲突处理：

```json
{
  "accepted_manuscript_online": "2025-05-07",
  "accepted_manuscript_online_source": "正式PDF首页（封面后，084301-1）",
  "issue_date": "2025-08-01",
  "publisher_html_available_online": "2025-08-01",
  "crossref_published_print": "2025-08-01",
  "crossref_created": "2025-05-07T06:47:41Z",
  "first_publication_interpretation": "May7由正式PDF明确支持为accepted-manuscript上线；Aug1为正式期/现网站标签，不抹去May7。"
}
```

2026-10-08 复核备注：全文边界复核：本轮重读正式 PDF 首页、期刊 HTML §2.2–2.6、§3.2–3.5、§4；继承并复核 2026-09-27 医学 AWI 审计相同位置。

一手材料阅读范围：本轮重读正式 PDF 首页、期刊 HTML §2.2–2.6、§3.2–3.5、§4；继承并复核 2026-09-27 医学 AWI 审计相同位置。

## 创新点 / 主要贡献

通过观测零填充改变 Wiener filter 的零 lag 位置：先边缘 zero-lag 构造初模，再居中 zero-lag 常规 AWI 精修，改善特定 Gaussian penalty 参数下稳定性。

## 技术手段

预测→观测的正则 Wiener filter，Gaussian 加权归一化能量最大化；edge→center AWI 两阶段。经颅 50 kHz 低通 pre/post 各128迭代，再100 kHz 低通 AWI256迭代；block 对照使用0–100 kHz→100–200 kHz。

## 验证证据

全部二维声学数值：128点换能器，正演含密度、仅更新声速；最终精修仍为 AWI，L2-FWI 为独立对照。

## 局限与评估

500 kHz 为三周期 tone-burst 源中心，不是最低反演频率；经颅验证依赖50/100 kHz低通，未验证严格≥0.5 MHz数据。无实测/黏弹性验证；首阶段初始声速场、固定密度取值及逐实验 λ 未充分披露。高频 block 阶段 FWI 的 MSE 可更低；SAWI未消除 polarity ambiguity。

## 研究相关性

与AWI机理研究高度相关，适合直接复核匹配滤波器和惩罚参数作用。

## 公开来源

- [https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/add4f3](https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/add4f3)
- [https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/add4f3.pdf](https://cpb.iphy.ac.cn/en/article/pdf/preview/10.1088/1674-1056/add4f3.pdf)
- [https://api.crossref.org/works/10.1088/1674-1056/add4f3](https://api.crossref.org/works/10.1088/1674-1056/add4f3)

Chin. Phys. B 34(8)084301。正式PDF写 accepted manuscript online 2025-05-07；期刊当前HTML Available Online与Crossref published-print为2025-08-01。保留两个日期含义，不能据Crossref created独立判定首发。非李玉冰团队。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
