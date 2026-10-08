# 最值得精读的论文：排序与阅读路线

主榜保留 2026-09-26 的 26 篇次序。当前主题阅读另见 [2026-10-08 十二篇专题顺序](PROJECT_READING_20261008.md)，不是主榜重排。

这是围绕环阵超声FWI、三维重建、AWI和声源校准的阅读优先级，不是影响因子/引用量榜。主榜按相关性、可辨识的技术贡献、实测验证、可复用方法综合人工判断；具体理由逐篇列出，避免给尚未深读的文章伪精确分数。2020年前奠基论文另列；新预印本单列前沿观察。

| 顺序 | 论文 | 核心贡献 | 为什么排在这里 |
|---|---|---|---|
| 1 | [2-D Slicewise Waveform Inversion of Sound Speed and Acoustic Attenuation for Ring Array Ultrasound Tomography Based on a Block LU Solver](papers/UFWI-013.md)（2024，IEEE Transactions on Medical Imaging） | 给出透明可复现的环阵声速/衰减频域反演实现，并用临床乳腺示例验证。 | 最适合先建立可复现环阵频域FWI基线：公式、代码、声速/衰减及人体案例俱全，也坦陈二维和绝对衰减局限。 |
| 2 | [Spatial response identification enables robust experimental ultrasound computed tomography](papers/UFWI-035.md)（2022，IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control (TUFFC)） | 扩展SRI，把位置、朝向与脉冲响应的影响一并吸收到有效换能器模型。 | 实验失配常来自换能器；SRI直接改变有效前向模型，对实验声源校准比单纯换loss更基础。 |
| 3 | [High resolution 3D ultrasonic breast imaging by time-domain full waveform inversion](papers/UFWI-025.md)（2022，Inverse Problems） | 整合时间反演梯度、随机源编码和多尺度策略，使高分辨率三维乳腺FWI在适度GPU资源上可计算。 | 真三维时域FWI计算路线的系统参考：源编码、梯度存储与多尺度；虽仅仿真，方法价值很高。 |
| 4 | [Optimal transport assisted full waveform inversion for multiparameter imaging of soft tissues in ultrasound computed tomography](papers/UFWI-104.md)（2025，Ultrasonics） | graph-space OT缓解皮肤超临界反射造成的局部极小，重建声速与阻抗。 | 重点作者线与Ultrasonics直接交汇：OT、强反射和声速/阻抗多参数；有离体实验。 |
| 5 | [Frequency-differencing strategy to kickstart full-waveform inversion without cycle skipping](papers/UFWI-097.md)（2025，JASA Express Letters） | 利用高频之间的差频内容构建低频起始信息，为常规FWI提供可用初模。 | 直接应对缺低频，且已从会议发展为有实验的正式期刊文；与频域AWI研究直接相关。 |
| 6 | [Quantitative in-vivo full-waveform ultrasound tomography workflow integrating reflection imaging and resolution analysis](papers/UFWI-040.md)（2026，Physics in Medicine & Biology） | 将有效源估计、graph-space OT及局部分辨率分析组织为在体FWI工作流。 | 2026新工作把源估计、GSOT、反射像与分辨率评价组成在体流程；动物证据明确，便于设计完整验证链。 |
| 7 | [Full-waveform inversion imaging of the human brain](papers/UFWI-124.md)（2020，npj Digital Medicine） | 展示脑部超声定量 FWI 潜力：二维无颅骨先验 AWI→FWI，与已有真实颅骨初模的三维高分辨 FWI 分别验证。 | Imperial超声FWI跨领域里程碑，值得读其数值验证和颅骨建模条件，避免把题名误解为临床已实现。 |
| 8 | [Localized adaptive waveform inversion: theory and numerical verification](papers/UFWI-007.md)（2023，Geophysical Journal International） | 用局部时频反卷积处理不同事件不同时间偏移，针对全道AWI的非平稳失配。 | AWI研究最关键的方法补课之一：多到时非平稳性为何使全局滤波失效，以及局部化如何补救。 |
| 9 | [Localized adaptive waveform inversion: regularizations for Gabor deconvolution and 3-D field data application](papers/UFWI-008.md)（2023，Geophysical Journal International） | 比较零型与delta型滤波器先验，并把LAWI用于三维北海实测。 | 接续理论篇看滤波器先验与三维实测；正则项如何影响稳定性和分辨率与AWI研究直接相关。 |
| 10 | [Ultrasound computed tomography based on full waveform inversion with source directivity calibration](papers/UFWI-037.md)（2023，Ultrasonics） | 用无目标水槽FMC自检换能器方向性，再以加权虚拟点阵表示源。 | 水槽校准与虚拟点源权重有明确实现路径和环阵实测，是声源方向性建模的实用对照。 |
| 11 | [Hybrid three-dimensional full-view multi-wavelength photoacoustic and ultrasound breast tomography](papers/UFWI-029.md)（2026，Photoacoustics） | PAM3将完整三维FWI声速成像与多波长全视角光声系统结合，用声速图校正光声非均匀传播。 | 真正三维波动反演结合健康志愿者乳腺数据，是近期验证层级较强的系统进展；区分PAT与FWI指标。 |
| 12 | [Frequency-domain full-waveform inversion-based musculoskeletal ultrasound computed tomography](papers/UFWI-069.md)（2023，The Journal of the Acoustical Society of America） | 为含骨高对比度FDFWI提出水参考标定与起始频率准则。 | 李玉冰团队肌骨频域FWI代表路线，与含骨环阵反演问题直接相关。 |
| 13 | [Quantitative Sound Speed Imaging of Cortical Bone and Soft Tissue: Results From Observational Data Sets](papers/UFWI-152.md)（2022，IEEE Transactions on Medical Imaging） | 结合level-set和走时约束，改善骨/软组织联合声速重建及未知剪切波造成的误差。 | 骨与软组织离体实测，并结合level-set和走时正则；对含骨环阵的物理失配和独立验证比只看仿真更有参照意义。 |
| 14 | [On cycle-skipping and misfit function modification for full-wave inversion: Comparison of five recent approaches](papers/UFWI-011.md)（2021，Geophysics） | 用统一案例揭示五种抗周跳目标函数的能力和失效，而非再提出一种万能目标。 | 用于选择公平baseline和构造反例；比堆叠一串loss名称更能识别可写成论文的贡献。 |
| 15 | [A Forward Model Incorporating Elevation-Focused Transducer Properties for 3-D Full-Waveform Inversion in Ultrasound Computed Tomography](papers/UFWI-026.md)（2023，IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control (TUFFC)） | 把环阵俯仰聚焦性质同时写进发射和接收正演模型。 | 三维阵元俯仰聚焦和接收模型必须正确，否则三维算法优势可能被算子失配淹没。 |
| 16 | [3D Frequency-Domain Full Waveform Inversion for Whole-Breast Imaging With a Multi-Row Ring Array](papers/UFWI-014.md)（2025，IEEE Open Journal of Ultrasonics, Ferroelectrics, and Frequency Control） | 以多排环阵和圆柱波发射实现完整三维反演，减少逐层重建面外分辨率损失。 | 三维频域、多排环阵和Born求解器的紧凑前沿参照；明确仅数值验证，不与临床成果混排。 |
| 17 | [Cross-correlation adjustment full-waveform inversion with source encoding in ultrasound computed tomography](papers/UFWI-019.md)（2024，Ultrasonics） | 用互相关走时生成中间目标信号，并间歇更新以兼容源编码。 | 互相关校正与源编码结合，有模拟和实验；适合作为抗周跳与效率两方面的超声baseline。 |
| 18 | [Transcranial ultrasound tomography for brain imaging: Ex vivo results and potential for stroke imaging](papers/UFWI-127.md)（2025，Medical Physics） | 从简单体模推进到含血液仿体、离体猕猴脑及完整离体人脑的解剖验证。 | 2025离体脑及出血仿体验证增强了脑FWI可行性证据；需清楚真实颅骨和活体条件尚未闭合。 |
| 19 | [Frequency-Domain Reconstruction of the Speed of Sound in Ring-Array Ultrasound Computed Tomography With Stochastic Phase Encoding](papers/UFWI-034.md)（2026，IEEE Transactions on Ultrasonics (TUSON)） | 把多super-shot随机集合优化落实到频域环阵声速FWI。 | 新刊TUSON中频域随机相位编码结合患者数据，对当前多炮频域成本有直接参考价值。 |
| 20 | [Sobolev space norm regularized full waveform inversion for ultrasound computed tomography](papers/UFWI-031.md)（2025，Chinese Physics B） | 把Sobolev范数先验引入多尺度频域FWI，并按正则/数据项比例动态调整权重。 | 国内重点作者线的正则化工作，数值与离体数据都可作为对照；可比较Sobolev和TV的结构偏好。 |
| 21 | [A probabilistic approach to tomography and adjoint state methods, with an application to full waveform inversion in medical ultrasound](papers/UFWI-125.md)（2022，Inverse Problems） | 在常见近似下，以几乎不增加FWI计算量的方式估计逐像素声速方差。 | 把不确定性加入FWI质量评价，避免只看图像或loss；需理解mean-field近似限制。 |
| 22 | [Automatic Skull-Template Alignment Without a Guidance Image](papers/UFWI-134.md)（2026，Ultrasound in Medicine & Biology） | MOFI直接通过超声RF数据配准颅骨模板，去掉同步MRI指导配准需求。 | MOFI以RF波形直接优化模板旋转平移，与几何参数反演高度相关；仍需已有模板。 |
| 23 | [Dual-Probe Transcranial Full-Waveform Inversion: A Brain Phantom Feasibility Study](papers/UFWI-039.md)（2023，Ultrasound in Medicine & Biology） | 用可获得的双探头与旋转采集探索低成本经颅FWI实验路径。 | Imperial透颅双探头实体体模验证，帮助区分大孔径理论理想化与受限采集的实际难度。 |
| 24 | [Quantitative ultrasound brain imaging with multiscale deconvolutional waveform inversion](papers/UFWI-113.md)（2023，Chinese Physics B） | 以有限长度 Wiener filter 的 lag 支撑递减实现四阶段 MDWI，由大尺度到细节完成同一目标家族的重建，无需末尾改为 L2-FWI。 | 李玉冰团队解卷积波形反演与AWI最接近的必查先行工作，创新定位不能跳过。 |
| 25 | [Waveform inversion of sound speed and acoustic attenuation for ring-array ultrasound tomography based on optimal transport framework](papers/UFWI-099.md)（2026，Ultrasonics） | 将Sigmoid数据映射与2-Wasserstein目标结合，同时重建声速和衰减。 | 2026声速/衰减OT工作值得关注，但摘要与Highlights的对照方式不一致，阅读时需审原始实验细节。 |
| 26 | [Quantitative comparison of the total focusing method, reverse time migration, and full waveform inversion for ultrasonic imaging](papers/UFWI-100.md)（2025，Ultrasonics） | 用统一样本和分割指标量化TFM、RTM与两阶段FWI性能。 | NDT方向优先读这一实测对比，用统一定量指标判断FWI相比TFM/RTM的收益，而非只看好看的图。 |

## 分主题阅读顺序

- AWI / 缺低频：Warner & Guasch 2016 → Guasch 2019 → Pladys 2021 → Yong 2023两篇 → Ali 2025 FDWI → OT/SAWI新工作。
- 真三维与可复现基线：Lucka 2022 → Li 2023 elevation-focused → Ali 2024二维开源 → Ali 2025多行环阵 → Dantuma 2026在体。
- 换能器与实验误差：Cueto 2021/2022 SRI → Wu 2023指向性 → 2026分布式声源 → 在体工作流的联合标定。
- 骨与透颅：Guasch 2020 → Robins 2023 → Li 2023肌骨 → Mitcham 2025离体 → 2026 Rytov / 神经物理预印本。
- 计算与稀疏采样：Lucka 2022 → source encoding / vortex → Louboutin 2023波场压缩 → Mercier 2025联合设计 → Forte 2026 phase encoding。

## 奠基论文与前沿观察

奠基论文应先读其基本假设，再对照近期失效案例；前沿观察的预印本不能视为已经独立验证。

- [Hybrid Full Waveform Inversion Assisted by Rytov Approximation for Musculoskeletal Ultrasound Computed Tomography](papers/UFWI-114.md)（2026，preprint）：2026李玉冰主线最值得关注的新方法，可与CCAFWI/AWI/OT公平比较。
- [Simulation-to-Real First-Break Segmentation for Efficient Inversion in Musculoskeletal Ultrasound Tomography](papers/UFWI-115.md)（2026，preprint）：关注真实系统弱信号及初模构建，属于算法链条而非单一损失函数创新。
- [Towards 3D fully randomized frequency-domain reconstruction of the speed of sound in breast ultrasound computed tomography](papers/UFWI-162.md)（2026，preprint）：直接医学 FWI 的三维计算预印本，用于研究随机编码及源几何边界。
- [Ultrasonic Medical Tissue Imaging Using Probabilistic Inversion: Leveraging Variational Inference for Speed Reconstruction and Uncertainty Quantification](papers/UFWI-131.md)（2025，preprint）：与Bates2022 mean-field SVI构成直接方法比较。
- [Ultrasound Tomography of Musculoskeletal Tissues with Generative Neural Physics](papers/UFWI-116.md)（2025，preprint）：李玉冰团队最新重点观察项，建议与Rytov物理FWI并列看而分开证据级别。
- [Adaptive waveform inversion for transmitted wave data](papers/UFWI-187.md)（2024，preprint）：优先阅读以解释多到达下逐道匹配目标的适用条件；仅提供机制假说，不能诊断某一具体实验失败原因。
- [Adaptive traveltime inversion](papers/UFWI-003.md)（2019，journal）：保留原AWI/USCT知识链供新检索对照。
- [Adaptive waveform inversion: Practice](papers/UFWI-006.md)（2019，journal）：设计独立于训练misfit的质量指标；避免误把损失下降当成正确成像。
- [Improving full-waveform inversion by wavefield reconstruction with the alternating direction method of multipliers](papers/UFWI-093.md)（2019，journal）：缺低频与强对比USCT的备选框架，先与更便宜目标修改比较。
- [Retrieving Low-Wavenumber Information in FWI: An Efficient Solution for Cycle Skipping](papers/UFWI-012.md)（2019，journal）：保留原AWI/USCT知识链供新检索对照。
- [Robust full-waveform inversion with Radon-domain matching filter](papers/UFWI-163.md)（2019，journal）：Radon-domain matching 的直接方法先例，宜连同几何、频带和结构验证条件阅读。
- [The application of an optimal transport to a preconditioned data matching function for robust waveform inversion](papers/UFWI-009.md)（2019，journal）：保留原AWI/USCT知识链供新检索对照。
- [Automated Salt-Model Building Using Constrained FWI](papers/UFWI-005.md)（2018，conference）：保留原AWI/USCT知识链供新检索对照。
- [3-D Nonlinear Acoustic Inverse Scattering: Algorithm and Quantitative Results](papers/UFWI-028.md)（2017，journal）：说明“近似 3D forward + 频率递进”可在真实大体积数据上形成定量结果；如果目标是先改善 z 连续性，可以把 paraxial/phase-screen 作为低成本 3D baseline，而不是一开始就全带宽精确 FDTD。
- [Salt Reconstruction in Full-Waveform Inversion with a Parametric Level-Set Method](papers/UFWI-154.md)（2017，journal）：几何先验与 level-set 参数化的地球物理基线；应与医学骨先例成对阅读。
- [Time domain reconstruction of sound speed and attenuation in ultrasound computed tomography using full wave inversion](papers/UFWI-073.md)（2017，journal）：多参数FWI及黏声正演的基础参考。
- [Adaptive waveform inversion: Theory](papers/UFWI-010.md)（2016，journal）：AWI理论根文献；应在LAWI和FDWI之前建立公式与归一化约定。
- [Building good starting models for full-waveform inversion using adaptive matching filtering misfit](papers/UFWI-001.md)（2016，journal）：保留原AWI/USCT知识链供新检索对照。
- [Waveform inversion with source encoding for breast sound speed reconstruction in ultrasound computed tomography](papers/UFWI-030.md)（2015，journal）：源编码主线的奠基必读，供2025涡旋和2026频域编码溯源。
- [The variable projection method for waveform inversion with an unknown source function](papers/UFWI-156.md)（2013，journal）：未知源波形消元的数学基线，用于分析介质和源的耦合。
- [Coarse-to-fine multi-resolution hash encoding for implicit full waveform inversion](papers/UFWI-166.md)（2026，preprint）：模型参数化渐进策略近邻；不能把粗到细神经参数化单独当原创。
- [Physics Informed Deep Unfolded Full Waveform Inversion for Edema Detection](papers/UFWI-130.md)（2026，preprint）：扩展应用从乳腺/脑转向常规探头低对比定量成像。
- [Robust Ensemble Guidance for Scientific Inverse Problems](papers/UFWI-161.md)（2026，preprint）：跟踪生成式反演的鲁棒数据校正；评估完整正演成本与先验依赖。
- [Structure-dependent failure modes of neural priors in acoustic full-waveform inversion](papers/UFWI-169.md)（2026，preprint）：支持同时报告留出预测、结构误差、等预算对照与负结果；不是 USCT 实测。
- [TV-Regularized Frequency-Domain Full-Waveform Inversion for Single-Sided Linear Ultrasound Array Data](papers/UFWI-129.md)（2026，preprint）：有限孔径研究新入口，需与2020–2024既有线阵方法对照。
- [OpenBreastUS: Benchmarking Neural Operators for Wave Imaging Using Breast Ultrasound Computed Tomography](papers/UFWI-168.md)（2025，preprint）：李玉冰团队此前漏项；数据方法库可收，非本周更新。
- [Seismic Full-Waveform Inversion Using Deep Learning Tools and Techniques](papers/UFWI-053.md)（2018，preprint）：补齐原始文献清单；是否优先阅读按直接FWI相关性与证据评定。
