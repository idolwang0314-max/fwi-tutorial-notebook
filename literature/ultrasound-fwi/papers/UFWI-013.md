# UFWI-013 · 2-D Slicewise Waveform Inversion of Sound Speed and Acoustic Attenuation for Ring Array Ultrasound Tomography Based on a Block LU Solver

[总索引](../INDEX.md) · [可筛选网页](../index.html) · [阅读排序](../READING_RANKING.md)

- 作者：Rehman Ali; Trevor M Mitcham; Thurston Brevett; Òscar Calderón Agudo; Cristina Durán Martinez; Cuiping Li; Marvin M Doyley; Nebojsa Duric
- 年份 / 期刊：2024 / IEEE Transactions on Medical Imaging
- 发表类型 / 状态：journal / published
- 研究类型：医学超声 FWI
- 主题：旧库深读、医学FWI、乳腺、频域FWI、多参数、开源软件、在体
- 核验程度：一手全文/相关段落
- 优先级：P0；精读第 1 篇
- DOI：[10.1109/tmi.2024.3383816](https://doi.org/10.1109/tmi.2024.3383816)

## 创新点 / 主要贡献

给出透明可复现的环阵声速/衰减频域反演实现，并用临床乳腺示例验证。

## 技术手段

GPU block-LU Helmholtz求解；源复幅度/相位校准；第一轮仅声速，第二轮交替声速/衰减更新；频率递增。

## 验证证据

simulation + physical phantom + human in vivo；公开代码/样例数据；包含乳腺囊肿与恶性病灶。

## 局限与评估

二维面外效应使衰减偏差明显；源幅值与介质衰减非唯一，因此绝对衰减不能保证；block-LU三维内存扩展困难。

## 研究相关性

最适合作为实测FWI和复现baseline的高优先级论文。

## 排序理由

最适合先建立可复现环阵频域FWI基线：公式、代码、声速/衰减及人体案例俱全，也坦陈二维和绝对衰减局限。

## 公开来源

- [https://doi.org/10.1109/TMI.2024.3383816](https://doi.org/10.1109/TMI.2024.3383816)
- [https://doi.org/10.1109/tmi.2024.3383816](https://doi.org/10.1109/tmi.2024.3383816)
- [https://pmc.ncbi.nlm.nih.gov/articles/PMC11294001/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11294001/)
- [https://github.com/rehmanali1994/WaveformInversionUST](https://github.com/rehmanali1994/WaveformInversionUST)
- [https://pubmed.ncbi.nlm.nih.gov/38564345/](https://pubmed.ncbi.nlm.nih.gov/38564345/)

检索核验日期2026-09-26。2024-08卷43(8):2988–3000；已读讨论及作者代码说明；不是实时三维方法。

核验程度表示本轮查阅证据，不代表已复现实验。局限和研究价值包含整理者评估；不把贡献概括等同于全球首创。
