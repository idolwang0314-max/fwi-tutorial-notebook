# 作者与团队路线索引

本库重点追踪 **李玉冰（Yubing Li / Yu-Bing Li，中科院声学所）**。作者身份依据：[UCAS官方主页](https://people.ucas.edu.cn/~yubing.li)、[CPB中文署名](https://cpb.iphy.ac.cn/EN/10.1088/1674-1056/ac6dad)。

## 李玉冰主线

建议顺序：多尺度解卷积脑FWI → 方向性校准 → 频域肌骨 → graph-space OT声速/阻抗 → Sobolev正则 → 黏声Born求解器 → Rytov混合和首波分割预印本。APINN与生成神经物理另作计算分支。Fu Li（Anastasio线）及其他Li姓作者不凭姓氏并入。

- [Optimal transport assisted full waveform inversion for multiparameter imaging of soft tissues in ultrasound computed tomography](papers/UFWI-104.md)（2025，Ultrasonics，published）
- [Ultrasound computed tomography based on full waveform inversion with source directivity calibration](papers/UFWI-037.md)（2023，Ultrasonics，published）
- [On cycle-skipping and misfit function modification for full-wave inversion: Comparison of five recent approaches](papers/UFWI-011.md)（2021，Geophysics，published）
- [Sobolev space norm regularized full waveform inversion for ultrasound computed tomography](papers/UFWI-031.md)（2025，Chinese Physics B，published）
- [Quantitative ultrasound brain imaging with multiscale deconvolutional waveform inversion](papers/UFWI-113.md)（2023，Chinese Physics B，published）
- [Hybrid Full Waveform Inversion Assisted by Rytov Approximation for Musculoskeletal Ultrasound Computed Tomography](papers/UFWI-114.md)（2026，arXiv，preprint）
- [Simulation-to-Real First-Break Segmentation for Efficient Inversion in Musculoskeletal Ultrasound Tomography](papers/UFWI-115.md)（2026，arXiv，preprint）
- [A viscoacoustic wave equation solver using modified Born series](papers/UFWI-056.md)（2025，The Journal of the Acoustical Society of America，published）
- [Agent-Physics-Informed Neural Network solving frequency-domain Helmholtz equation related forward and inverse problems](papers/UFWI-055.md)（2025，Wave Motion，published）
- [Ultrasound Tomography of Musculoskeletal Tissues with Generative Neural Physics](papers/UFWI-116.md)（2025，arXiv，preprint）
- [Neural Born Series Operator for Biomedical Ultrasound Computed Tomography](papers/UFWI-117.md)（2023，arXiv，withdrawn）

## Imperial College：Guasch / Warner / Cueto / Bates / Robins等

AWI源于地球物理，随后连接脑/乳腺FWI、仪器响应、低频采集、概率估计和模板几何优化。按论文发表时单位及作者署名追踪，不能把所有英国或国际USCT论文都写为Imperial团队。

- [Adaptive waveform inversion: Theory](papers/UFWI-010.md)
- [Adaptive waveform inversion: Practice](papers/UFWI-006.md)
- [Full-waveform inversion imaging of the human brain](papers/UFWI-124.md)
- [Spatial Response Identification for Flexible and Accurate Ultrasound Transducer Calibration and its Application to Brain Imaging](papers/UFWI-036.md)
- [Spatial response identification enables robust experimental ultrasound computed tomography](papers/UFWI-035.md)
- [Stride: A flexible software platform for high-performance ultrasound computed tomography](papers/UFWI-041.md)
- [A probabilistic approach to tomography and adjoint state methods, with an application to full waveform inversion in medical ultrasound](papers/UFWI-125.md)
- [Design and Construction of a Low-Frequency Ultrasound Acquisition Device for 2-D Brain Imaging Using Full-Waveform Inversion](papers/UFWI-126.md)
- [Dual-Probe Transcranial Full-Waveform Inversion: A Brain Phantom Feasibility Study](papers/UFWI-039.md)
- [Automatic Skull-Template Alignment Without a Guidance Image](papers/UFWI-134.md)

## 其他值得并读的团队路线

- Rochester / Ali / Duric：二维block-LU开源、差频初始化、多排环阵三维、离体脑。
- Lucka / Treeby及合作者：三维时域计算、声源编码、可复现实现。
- Twente / Dantuma等：三维FWI与光声系统结合及人体在体。
- Anastasio / Fu Li等：三维收发仰角响应建模、学习FWI与任务损失。
- Grenoble / Brossier / Métivier / Yong / Pladys：AWI/OT系统对照、LAWI、三维地震实测。
- Fudan / Ta等：骨及剪切波/涡旋编码等方向；逐篇以实际署名为准。
- NDT / Bürchner等：TFM、RTM、FWI基准、网络参数化与非规则几何。

本表用于导航，不是穷尽作者履历或认定当前单位。完整作者与官方来源见单篇卡片。


## 2026-10-08 路线更新

- Imperial：增加 [Rabbat 与 Huthwaite 的几何 FWI 会议摘要](papers/UFWI-178.md)，保持管道导波与骨 USCT 的应用区别。
- 李玉冰团队：更新现有 [HFWI](papers/UFWI-114.md)、[首波分割](papers/UFWI-115.md)、[Generative Neural Physics](papers/UFWI-116.md) 的 arXiv 版本复核备注；本周未发现新版本，未新增重复条目。[OpenBreastUS](papers/UFWI-168.md) 为不同文章，作为早期补漏。
- 医学 AWI：增加 [Klaben 等源估计会议摘要](papers/UFWI-170.md)；作者以当前官方日程为准，证据仅为摘要中的模拟。

本次完整主题顺序见 [12 篇专题阅读](PROJECT_READING_20261008.md)。
