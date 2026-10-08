# 2026-10-08 专题阅读：12 篇优先顺序

围绕几何与 level-set、源与换能器校准、Radon matching、抗周期跳跃和三维计算安排阅读。此表是方法主题优先级，不是影响因子榜，也不替换 [26 篇历史主榜](READING_RANKING.md)。只讨论公开论文与一般评价建议，不代表完成了对应方法复现。

[本周综述](WEEKLY_REVIEW_CN.md) · [总索引](INDEX.md) · [来源 ID 映射](ID_MAP_20261008.json)

| 顺序 | 论文 | 为什么现在读 | 证据等级 |
|---:|---|---|---|
| 1 | [Quantitative Sound Speed Imaging of Cortical Bone and Soft Tissue: Results From Observational Data Sets](papers/UFWI-152.md) | 骨与软组织 level-set FWI 的离体先例；结合独立声速与 MRI 验证理解几何约束的贡献。 | primary_abstract |
| 2 | [Quantitative Characterisation of Defects in Pipes Using Guided Wave Testing with Geometrical Full Waveform Inversion](papers/UFWI-178.md) | Imperial 几何 FWI 的会议近邻；管道 NDT 证据与骨 USCT 的适用范围须分开。 | primary_abstract |
| 3 | [Ultrasound computed tomography based on full waveform inversion with source directivity calibration](papers/UFWI-037.md) | 理解换能器指向性与点源假设的偏差，以及独立水槽校准的作用。 | primary_abstract |
| 4 | [Reconstructing effective ultrasound transducer models via distributed source inversion](papers/UFWI-043.md) | 分布式源反演与系统模型误差的近邻；区分源标定验证和成像验证。 | primary_abstract |
| 5 | [Spatial Response Identification for Flexible and Accurate Ultrasound Transducer Calibration and its Application to Brain Imaging](papers/UFWI-036.md) | SRI 发射与接收校准的经典对照；理解物理校准与自由逐道拟合的差别。 | primary_abstract |
| 6 | [Robust full-waveform inversion with Radon-domain matching filter](papers/UFWI-163.md) | Radon-domain matching 的原始方法；核对匹配方向、归一化和局部 Radon 假设。 | primary_abstract |
| 7 | [A comprehensive review of strategies to mitigate non-convexity in full waveform inversion](papers/UFWI-164.md) | 2026 非凸性综述：联系模型、源、波场和接收器扩展，比较各自假设。 | primary_fulltext |
| 8 | [Adaptive Waveform Inversion with Source Estimation for Ultrasound Tomography](papers/UFWI-170.md) | AWI 联合源估计已用于医学 USCT 会议工作；当前只有摘要级仿真证据。 | primary_abstract |
| 9 | [Impact of Windowing on Full-Waveform Inversion for Ultrasound Tomography](papers/UFWI-171.md) | 理解首波窗口如何改变有效频谱与反演问题，审查缺低频实验的处理约定。 | primary_abstract |
| 10 | [2-D Slicewise Waveform Inversion of Sound Speed and Acoustic Attenuation for Ring Array Ultrasound Tomography Based on a Block LU Solver](papers/UFWI-013.md) | 可复现环阵 USCT 基线，兼看声速/衰减耦合与二维模型失配。 | primary_fulltext |
| 11 | [Towards 3D fully randomized frequency-domain reconstruction of the speed of sound in breast ultrasound computed tomography](papers/UFWI-162.md) | 三维随机频域计算进展；300 kHz 起步、约 14 h + 24 h 的条件须与比较方法对齐。 | primary_fulltext |
| 12 | [Hybrid Full Waveform Inversion Assisted by Rytov Approximation for Musculoskeletal Ultrasound Computed Tomography](papers/UFWI-114.md) | 李玉冰团队肌骨 HFWI 近邻；分开评价低频初始化和后续较高频率精化。 | primary_abstract |

会议摘要、预印本与正式论文的证据层级分别保留；“优先读”不表示方法已优于其它路线。几何/level-set、AWI 联合源估计、源变量投影均已有先例。建议阅读时同时审查初始模型、频率范围、源模型自由度、独立验证及总计算成本。
