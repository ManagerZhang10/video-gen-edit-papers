# 视频生成与编辑论文库索引

> 读者：要系统补齐 2023–2026 视频生成技术脉络的人
> 目标：按脉络挑论文，点进任意一篇能直接读完整解读，不用再读原文
> 覆盖：50 项，2023-11 ～ 2026-07
> 最后核对：2026-09-02

[README](../README.md) 是一张按时间排的平表，用来查。本页按技术脉络分组，用来读。
每篇的「一句话」摘自该篇 `解读.md` 第 1 节首句，依据是论文原文，不是另写的导读。

## 任务分布

一篇论文可以同时是生成和编辑——这就是本库按模态而不按任务划分的原因。

| 任务 | 篇数 | 篇目 |
| --- | ---: | --- |
| 生成 | 38 | VDM、Tune-A-Video、Gen-1、Text2Video-Zero、SVD、Animate Anyone、VBench、Sora、Genie、CogVideoX、HunyuanVideo、CausVid、Open-Sora、LTX-Video、Cosmos、VideoReward、Sparse VideoGen、VACE、ReCamMaster、Wan、VBench-2.0、DanceGRPO、MAGI-1、Self Forcing、Seedance 1.0、Chain-of-Frames、EditVerse、LongLive、Self-Forcing++、UniVideo、Cosmos-Predict 2.5、HunyuanVideo 1.5、Kling-Omni、Helios、Matrix-Game 3.0、Seedance 2.0、VidGen-VL、MiniMax H3 |
| 编辑 | 20 | Tune-A-Video、Gen-1、FateZero、Text2Video-Zero、Rerender-A-Video、TokenFlow、InsV2V、Señorita-2M、VideoGrain、VideoPainter、VACE、ReCamMaster、MiniMax-Remover、EditVerse、UniVideo、IVEBench、Ditto、Kling-Omni、LiveEdit、JoyAI-Video-Edit |

## 15 条脉络

### 基座架构（12 篇）

文本到视频的主干怎么搭：潜空间压缩、时空 patch、DiT 规模化，以及各家开源/闭源旗舰的取舍。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2022-04 | [VDM](../papers/2022-04_VDM/解读.md) | Video Diffusion Models | 方法 | 这篇论文解决的是“如何用扩散模型生成时间上连贯的高质量视频”。 |
| 2023-11 | [SVD](../papers/2023-11_SVD/解读.md) | Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets | 方法 | Stable Video Diffusion（SVD）是 Stability AI 提出的潜空间视频扩散模型。 |
| 2024-02 | [Sora](../papers/2024-02_Sora/解读.md) | Video generation models as world simulators | 技术报告 | Sora 解决的是“用一个通用模型从文本、图像或视频生成多时长、多分辨率、多宽高比的高保真视频，并朝物理世界模拟器方向探索”的问题。 |
| 2024-08 | [CogVideoX](../papers/2024-08_CogVideoX/解读.md) | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | 模型 | CogVideoX 是一个基于扩散 Transformer（Diffusion Transformer, DiT）的文本生成视频模型，由清华与智谱 AI 等团队提出。 |
| 2024-12 | [HunyuanVideo](../papers/2024-12_HunyuanVideo/解读.md) | HunyuanVideo: A Systematic Framework For Large Video Generative Models | 技术报告 | HunyuanVideo 是腾讯混元团队在 2024 年 12 月公开的一个 13B 参数开源视频生成基础模型。 |
| 2024-12 | [Open-Sora](../papers/2024-12_Open-Sora/解读.md) | Open-Sora: Democratizing Efficient Video Production for All | 技术报告 | Open-Sora 解决的是高质量开放视频生成问题：用一个空间-时间解耦的扩散 Transformer（STDiT）和一个先在空间、后在时间上压缩的 3D 自编码器，把视频压成紧凑潜变量后做扩散建模。 |
| 2024-12 | [LTX-Video](../papers/2024-12_LTX-Video/解读.md) | LTX-Video: Realtime Video Latent Diffusion | 模型 | 这篇论文解决“视频扩散模型太慢、显存占用高”的问题，采用“极高压缩 Video-VAE + 让 VAE 解码器顺便做最后一步去噪”的方法，把每个 token 对应像素数从常见 1:2048 拉到 1:8192，并用 1.9B 参数的 Transformer 做全时空自注意力。 |
| 2025-03 | [Wan](../papers/2025-03_Wan/解读.md) | Wan: Open and Advanced Large-Scale Video Generative Models | 技术报告 | Wan 是阿里团队于 2025 年 3 月 26 日发布的开源视频基础模型套件，采用主流的 Diffusion Transformer（DiT，扩散变换器）加 Flow Matching（流匹配）范式。 |
| 2025-05 | [MAGI-1](../papers/2025-05_MAGI-1/解读.md) | MAGI-1: Autoregressive Video Generation at Scale | 技术报告 | 这篇论文解决的是“视频生成模型缺乏因果结构、难以流式输出”的问题。 |
| 2025-06 | [Seedance 1.0](../papers/2025-06_Seedance-1.0/解读.md) | Seedance 1.0: Exploring the Boundaries of Video Generation Models | 技术报告 | Seedance 1.0 是字节跳动 Seed 团队于 2025 年 6 月发布的双语视频生成基础模型（video generation foundation model），统一支持文生视频（T2V）和图生视频（I2V）。 |
| 2025-11 | [HunyuanVideo 1.5](../papers/2025-11_HunyuanVideo-1.5/解读.md) | HunyuanVideo 1.5 Technical Report | 技术报告 | HunyuanVideo 1.5 是腾讯混元团队在 2025 年 11 月 24 日公开的 8.3B 参数开源视频生成模型。 |
| 2026-04 | [Seedance 2.0](../papers/2026-04_Seedance-2.0/解读.md) | Seedance 2.0: Advancing Video Generation for World Complexity | 技术报告 | Seedance 2.0 是字节跳动 Seed 团队提出的“原生多模态音频-视频联合生成模型”，不是单纯视频生成器。 |

### 少步与因果蒸馏（2 篇）

把双向扩散教师蒸馏成因果学生，换来实时与流式生成。CausVid 是根，Self Forcing 消掉训练-推理落差。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2024-12 | [CausVid](../papers/2024-12_CausVid/解读.md) | From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | 方法 | CausVid 解决视频扩散模型“生成慢、不能流式输出”的问题。 |
| 2025-06 | [Self Forcing](../papers/2025-06_Self-Forcing/解读.md) | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | 方法 | Self Forcing 是 Adobe Research 与 UT Austin 提出的自回归视频扩散模型后训练范式，论文发表于 NeurIPS 2025 (Spotlight)。 |

### 推理效率与稀疏注意力（1 篇）

不改模型结构，只在注意力上省算力。视频的时空冗余比图像大得多，这条线的杠杆也就更大。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-02 | [Sparse VideoGen](../papers/2025-02_Sparse-VideoGen/解读.md) | Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity | 方法 | 这篇论文解决视频扩散 Transformer（Diffusion Transformers, DiTs）推理太慢的问题：3D 全注意力在长上下文下占端到端运行时 80% 以上。 |

### 长视频与实时流式生成（3 篇）

从几秒推到几十秒乃至分钟级，并且要边生成边出画。瓶颈是误差累积和显存，不是画质。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-09 | [LongLive](../papers/2025-09_LongLive/解读.md) | LongLive: Real-time Interactive Long Video Generation | 方法 | 这篇论文解决的是“实时交互式长视频生成”问题：用户一边生成视频一边按时间顺序输入新的提示词，模型需要立即跟随新指令，同时保持画面不跳变、故事不漂移。 |
| 2025-10 | [Self-Forcing++](../papers/2025-10_Self-Forcing++/解读.md) | Self-Forcing++: Towards Minute-Scale High-Quality Video Generation | 方法 | 这篇论文解决自回归长视频生成中“学生模型一旦超过教师模型的训练时长（约5秒）就质量骤降”的问题。 |
| 2026-03 | [Helios](../papers/2026-03_Helios/解读.md) | Helios: Real Real-Time Long Video Generation Model | 模型 | Helios 解决的核心问题是：如何在单张 NVIDIA H100 GPU 上，让一个 14B 参数的大型视频生成模型以可交互速度生成分钟级长视频；论文给出的办法是同时压缩“历史视频”和“待生成噪声”的 token 数，并把 50 步扩散蒸馏到 3 步，代价是分辨率只做到 384×640、部分自动指标与强教师模型打平而非显著超越。 |

### 可控生成与运动控制（2 篇）

除了文本，还能塞什么进去：参考人物、相机轨迹、运动轨迹。商业化最深的支线在这里。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-11 | [Animate Anyone](../papers/2023-11_Animate-Anyone/解读.md) | Animate Anyone: Consistent and Controllable Image-to-Video Synthesis for Character Animation | 方法 | 本文解决从单张角色参考图像和姿态序列生成外观一致、姿态可控的角色动画视频。 |
| 2025-03 | [ReCamMaster](../papers/2025-03_ReCamMaster/解读.md) | ReCamMaster: Camera-Controlled Generative Rendering from A Single Video | 方法 | ReCamMaster 解决的是：给定一段真实视频和一条新的相机轨迹，如何重新渲染出同一动态场景在新视角下、且与源视频保持外观一致和时间同步的视频。 |

### 统一多模态（2 篇）

生成、编辑、理解、音画同步进一个模型，输入输出都不再单一。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-12 | [Kling-Omni](../papers/2025-12_Kling-Omni/解读.md) | Kling-Omni Technical Report | 技术报告 | Kling-Omni 是快手可灵团队提出的通用视频生成框架，论文定位为“从多模态视觉语言输入直接合成高保真视频”的端到端系统。 |
| 2026-07 | [MiniMax H3](../papers/2026-07_MiniMax-H3/解读.md) | MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities | 技术报告 | MiniMax H3 是 MiniMax 官方在 2026-07-31 发布的一款通用多模态生成模型。 |

### 视频模型即通用视觉基座（2 篇）

不训练也能做未见过的视觉任务——把视频生成模型当成视觉领域的 GPT-3 时刻来验证。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-09 | [Chain-of-Frames](../papers/2025-09_Chain-of-Frames/解读.md) | Video models are zero-shot learners and reasoners | 方法 | 本文《Video models are zero-shot learners and reasoners》用 Google DeepMind 的商用视频生成模型 Veo 3 做零样本视觉任务实验，核心论点是：视频模型正在走 LLM 从“任务专用模型”到“通用基础模型”的老路。 |
| 2026-07 | [VidGen-VL](../papers/2026-07_VidGen-VL/解读.md) | Video Generation Models are General-Purpose Vision Learners | 方法 | 这篇论文提出 **GenCeption**：一个把预训练文本到视频扩散模型（基于 WAN 2.1）改造为单步前馈的通用视觉感知模型。 |

### 世界模型与交互环境（4 篇）

视频模型当可交互环境用：接受动作输入、保持长程记忆，服务机器人、自动驾驶和游戏。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2024-02 | [Genie](../papers/2024-02_Genie/解读.md) | Genie: Generative Interactive Environments | 方法 | Genie 是一个生成式交互环境（generative interactive environments）模型，由 Google DeepMind 提出，发表于 ICML 2024。 |
| 2025-01 | [Cosmos](../papers/2025-01_Cosmos/解读.md) | Cosmos World Foundation Model Platform for Physical AI | 技术报告 | 这篇论文（arXiv:2501.03575，2025年1月公开）是 NVIDIA 提出的 Cosmos 世界基础模型平台，面向 Physical AI（具备传感器与执行器的 AI 系统）。 |
| 2025-10 | [Cosmos-Predict 2.5](../papers/2025-10_Cosmos-Predict-2.5/解读.md) | World Simulation with Video Foundation Models for Physical AI | 技术报告 | 这篇论文解决的是 Physical AI 系统缺一个高保真世界模拟器的问题：机器人、自动驾驶、机械臂直接实机训练慢、贵且危险，可以用视频世界模型在硅基环境里安全试错。 |
| 2026-04 | [Matrix-Game 3.0](../papers/2026-04_Matrix-Game-3.0/解读.md) | Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory | 方法 | Matrix-Game 3.0 是 Skywork AI 提出的交互式世界模型（interactive world model），目标是同时解决两个此前难以兼得的能力：分钟级长时记忆一致性，以及 720p 分辨率下的实时生成。 |

### 训练-free 视频编辑（6 篇）

不训练，只在推理时动注意力和特征对应。视频编辑最早成形的问题形态，核心矛盾从头到尾是帧间一致性。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2022-12 | [Tune-A-Video](../papers/2022-12_Tune-A-Video/解读.md) | Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation | 方法 | Tune-A-Video 解决的是：给定一段带文字描述的源视频，只用一个“文本-视频”对，把预训练文本到图像（Text-to-Image, T2I）扩散模型改造成能按新提示生成视频的模型，且尽量保留源视频的运动和结构。 |
| 2023-03 | [FateZero](../papers/2023-03_FateZero/解读.md) | FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | 方法 | FateZero 解决零样本文本驱动视频编辑问题：给定真实视频、源提示和目标提示，在不针对每个目标提示做训练、也不给用户掩码的情况下，把视频中的物体属性、全局风格或物体形状改成目标提示描述的内容。 |
| 2023-03 | [Text2Video-Zero](../papers/2023-03_Text2Video-Zero/解读.md) | Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators | 方法 | 这篇论文解决的是“零样本文本到视频生成”：给定一句文本，不训练、不微调任何模型，直接用预训练 Stable Diffusion 生成一段有时间一致性的视频。 |
| 2023-06 | [Rerender-A-Video](../papers/2023-06_Rerender-A-Video/解读.md) | Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation | 方法 | 这篇论文解决「用文字描述给输入视频换风格时，帧与帧之间会闪烁、纹理不一致」的问题。 |
| 2023-07 | [TokenFlow](../papers/2023-07_TokenFlow/解读.md) | TokenFlow: Consistent Diffusion Features for Consistent Video Editing | 方法 | TokenFlow 解决文本驱动视频编辑中“逐帧编辑后帧间不一致”的问题。 |
| 2025-02 | [VideoGrain](../papers/2025-02_VideoGrain/解读.md) | VideoGrain: Modulating Space-Time Attention for Multi-grained Video Editing | 方法 | 这篇论文解决多粒度视频编辑（multi-grained video editing）问题，即对同一视频中的不同对象或部位按文本提示分别编辑，包括类级（同一类全部改）、实例级（不同实例改成不同对象）和部分级（给实例加配件或改属性）。 |

### 视频编辑与统一创作（4 篇）

生成与编辑同一个模型。这条线上的论文同时属于两个任务，也正是本库按模态而不按任务分仓的原因。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-02 | [Gen-1](../papers/2023-02_Gen-1/解读.md) | Structure and Content-Guided Video Synthesis with Diffusion Models | 方法 | 这篇论文解决的是：对一段已有视频，用文本或参考图像指定新内容，生成一段保留原视频结构与运动、但外观或语义被编辑的新视频。 |
| 2025-03 | [VACE](../papers/2025-03_VACE/解读.md) | VACE: All-in-One Video Creation and Editing | 方法 | VACE 是阿里通义实验室提出的统一视频生成与编辑模型，发表于 ICCV 2025（首次公开 2025/03/10）。 |
| 2025-09 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | 方法 | EditVerse 解决的是视频编辑与生成长期碎片化的问题：用一个统一的 2B 稠密 Transformer，把文本、图像、视频都表示成一维 token 序列，靠全自注意力（full self-attention）做上下文学习（in-context learning），从而用图像域的数据补足视频编辑数据不足。 |
| 2025-10 | [UniVideo](../papers/2025-10_UniVideo/解读.md) | UniVideo: Unified Understanding, Generation, and Editing for Videos | 模型 | 这篇论文要解决的是：视频域里理解、生成、编辑仍被多个单任务模型割裂，缺少一个能读多模态指令并直接生成或编辑视频的统一系统。 |

### 视频修补与物体移除（2 篇）

只改一块区域：补全遮挡、擦掉物体。评价标准和「按指令改内容」完全不同——这里要的是看不出改过。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-03 | [VideoPainter](../papers/2025-03_VideoPainter/解读.md) | VideoPainter: Any-length Video Inpainting and Editing with Plug-and-Play Context Control | 方法 | VideoPainter 解决视频修复与编辑中“全掩码对象生成、背景保持、长视频身份一致”三者难以兼得的问题。 |
| 2025-05 | [MiniMax-Remover](../papers/2025-05_MiniMax-Remover/解读.md) | MiniMax-Remover: Taming Bad Noise Helps Video Object Removal | 方法 | 这篇论文解决视频物体移除（video object removal）中出现的伪影、幻觉物体和推理速度慢的问题。 |

### 实时与流式编辑（2 篇）

编辑也要边看边改。把双向编辑器压成单向流式，是 2026 年才成形的方向。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2026-06 | [LiveEdit](../papers/2026-06_LiveEdit/解读.md) | LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing | 方法 | 这篇论文解决的是流式视频编辑（streaming video editing）中因果逐块处理带来的两个问题：背景/未编辑区域不稳定，以及实时交互所需低延迟无法满足。 |
| 2026-08 | [JoyAI-Video-Edit](../papers/2026-08_JoyAI-Video-Edit/解读.md) | JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion | 模型 | 这篇论文解决的是：在未知时长、不断到达的视频流上，以低延迟和接近实时的速度做指令驱动的视频编辑，同时尽量保持源视频保真度和长时一致性。 |

### 指令式视频编辑与数据集（3 篇）

说人话改视频，以及三元组数据从哪来。和图像侧一样，这条线的瓶颈是数据不是方法。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-11 | [InsV2V](../papers/2023-11_InsV2V/解读.md) | Consistent Video-to-Video Transfer Using Synthetic Dataset | 方法 | 这篇论文解决的是文本驱动视频编辑中的三个痛点：逐视频微调太贵、用户必须同时描述原视频和目标视频、长视频跨片段不一致。 |
| 2025-02 | [Señorita-2M](../papers/2025-02_Señorita-2M/解读.md) | Señorita-2M: A High-Quality Instruction-based Dataset for General Video Editing by Video Specialists | 数据集 | 这篇论文解决的是端到端视频编辑模型缺高质量训练数据的问题。 |
| 2025-10 | [Ditto](../papers/2025-10_Ditto/解读.md) | Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset | 数据集 | Ditto 要解决的是指令式视频编辑训练数据稀缺、质量与多样性不足的问题。 |

### RL 与对齐（2 篇）

生成质量与人类偏好对齐：奖励模型 + 把 GRPO 一类的策略优化搬到视觉生成上。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-01 | [VideoReward](../papers/2025-01_VideoReward/解读.md) | Improving Video Generation with Human Feedback | 奖励与 RL | 这篇论文解决视频生成模型“运动不顺滑、文本-视频不对齐、不符合人类偏好”的问题。 |
| 2025-05 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | 奖励与 RL | DanceGRPO 是字节跳动 Seed 与香港大学合作的 arXiv 预印本，核心工作是把大语言模型强化学习中的 GRPO（Group Relative Policy Optimization，组相对策略优化）迁移到视觉生成。 |

### 评测（3 篇）

怎么量一个视频模型的好坏。VBench 是通用口径，IVEBench 是目前唯一一条视频编辑口径。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-11 | [VBench](../papers/2023-11_VBench/解读.md) | VBench: Comprehensive Benchmark Suite for Video Generative Models | 基准 | VBench 是一个面向文本到视频生成模型（T2V）的综合评测基准套件。 |
| 2025-03 | [VBench-2.0](../papers/2025-03_VBench-2.0/解读.md) | VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness | 基准 | VBench-2.0 解决现有视频生成评估只覆盖表面保真度、无法衡量物理规律、常识推理、解剖正确性和组合完整性等内在保真度的问题，提出五维度十八子能力的基准，用视觉语言模型（VLM）和大语言模型（LLM）做通用判断、用专家异常检测器补足视觉弱点，输出 0 到 1 的维度分数；代价是需要为每个维度构建约七十条提示、进行大规模人类偏好标注，并对四个模型重复生成视频。 |
| 2025-10 | [IVEBench](../papers/2025-10_IVEBench/解读.md) | IVEBench: Modern Benchmark Suite for Instruction-Guided Video Editing Assessment | 基准 | 这篇论文解决的是“指令引导视频编辑（Instruction-guided Video Editing, IVE）缺少适配基准”的问题。 |

## 按时间的全量清单

带发表、机构、引用、upvote 的完整版在 [README](../README.md#全量清单)。

| 时间 | 简称 | 脉络 | 任务 | 解读字数 |
| --- | --- | --- | --- | ---: |
| 2022-04-07 | [VDM](../papers/2022-04_VDM/解读.md) | 基座架构 | 生成 | 3,239 |
| 2022-12-22 | [Tune-A-Video](../papers/2022-12_Tune-A-Video/解读.md) | 训练-free 视频编辑 | 生成+编辑 | 3,120 |
| 2023-02-06 | [Gen-1](../papers/2023-02_Gen-1/解读.md) | 视频编辑与统一创作 | 生成+编辑 | 3,720 |
| 2023-03-16 | [FateZero](../papers/2023-03_FateZero/解读.md) | 训练-free 视频编辑 | 编辑 | 3,653 |
| 2023-03-23 | [Text2Video-Zero](../papers/2023-03_Text2Video-Zero/解读.md) | 训练-free 视频编辑 | 生成+编辑 | 3,415 |
| 2023-06-13 | [Rerender-A-Video](../papers/2023-06_Rerender-A-Video/解读.md) | 训练-free 视频编辑 | 编辑 | 3,692 |
| 2023-07-19 | [TokenFlow](../papers/2023-07_TokenFlow/解读.md) | 训练-free 视频编辑 | 编辑 | 3,867 |
| 2023-11-01 | [InsV2V](../papers/2023-11_InsV2V/解读.md) | 指令式视频编辑与数据集 | 编辑 | 3,145 |
| 2023-11-25 | [SVD](../papers/2023-11_SVD/解读.md) | 基座架构 | 生成 | 3,325 |
| 2023-11-28 | [Animate Anyone](../papers/2023-11_Animate-Anyone/解读.md) | 可控生成与运动控制 | 生成 | 3,036 |
| 2023-11-29 | [VBench](../papers/2023-11_VBench/解读.md) | 评测 | 生成 | 3,790 |
| 2024-02-15 | [Sora](../papers/2024-02_Sora/解读.md) | 基座架构 | 生成 | 4,072 |
| 2024-02-23 | [Genie](../papers/2024-02_Genie/解读.md) | 世界模型与交互环境 | 生成 | 3,522 |
| 2024-08-12 | [CogVideoX](../papers/2024-08_CogVideoX/解读.md) | 基座架构 | 生成 | 4,048 |
| 2024-12-03 | [HunyuanVideo](../papers/2024-12_HunyuanVideo/解读.md) | 基座架构 | 生成 | 3,576 |
| 2024-12-10 | [CausVid](../papers/2024-12_CausVid/解读.md) | 少步与因果蒸馏 | 生成 | 3,893 |
| 2024-12-29 | [Open-Sora](../papers/2024-12_Open-Sora/解读.md) | 基座架构 | 生成 | 3,259 |
| 2024-12-30 | [LTX-Video](../papers/2024-12_LTX-Video/解读.md) | 基座架构 | 生成 | 3,510 |
| 2025-01-07 | [Cosmos](../papers/2025-01_Cosmos/解读.md) | 世界模型与交互环境 | 生成 | 3,379 |
| 2025-01-23 | [VideoReward](../papers/2025-01_VideoReward/解读.md) | RL 与对齐 | 生成 | 3,548 |
| 2025-02-03 | [Sparse VideoGen](../papers/2025-02_Sparse-VideoGen/解读.md) | 推理效率与稀疏注意力 | 生成 | 3,190 |
| 2025-02-10 | [Señorita-2M](../papers/2025-02_Señorita-2M/解读.md) | 指令式视频编辑与数据集 | 编辑 | 3,151 |
| 2025-02-24 | [VideoGrain](../papers/2025-02_VideoGrain/解读.md) | 训练-free 视频编辑 | 编辑 | 3,737 |
| 2025-03-07 | [VideoPainter](../papers/2025-03_VideoPainter/解读.md) | 视频修补与物体移除 | 编辑 | 3,157 |
| 2025-03-10 | [VACE](../papers/2025-03_VACE/解读.md) | 视频编辑与统一创作 | 生成+编辑 | 3,042 |
| 2025-03-14 | [ReCamMaster](../papers/2025-03_ReCamMaster/解读.md) | 可控生成与运动控制 | 生成+编辑 | 3,669 |
| 2025-03-26 | [Wan](../papers/2025-03_Wan/解读.md) | 基座架构 | 生成 | 3,259 |
| 2025-03-27 | [VBench-2.0](../papers/2025-03_VBench-2.0/解读.md) | 评测 | 生成 | 3,009 |
| 2025-05-12 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | RL 与对齐 | 生成 | 3,697 |
| 2025-05-19 | [MAGI-1](../papers/2025-05_MAGI-1/解读.md) | 基座架构 | 生成 | 3,834 |
| 2025-05-30 | [MiniMax-Remover](../papers/2025-05_MiniMax-Remover/解读.md) | 视频修补与物体移除 | 编辑 | 3,565 |
| 2025-06-09 | [Self Forcing](../papers/2025-06_Self-Forcing/解读.md) | 少步与因果蒸馏 | 生成 | 3,493 |
| 2025-06-10 | [Seedance 1.0](../papers/2025-06_Seedance-1.0/解读.md) | 基座架构 | 生成 | 3,861 |
| 2025-09-24 | [Chain-of-Frames](../papers/2025-09_Chain-of-Frames/解读.md) | 视频模型即通用视觉基座 | 生成 | 3,243 |
| 2025-09-24 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | 视频编辑与统一创作 | 生成+编辑 | 3,456 |
| 2025-09-26 | [LongLive](../papers/2025-09_LongLive/解读.md) | 长视频与实时流式生成 | 生成 | 3,679 |
| 2025-10-02 | [Self-Forcing++](../papers/2025-10_Self-Forcing++/解读.md) | 长视频与实时流式生成 | 生成 | 3,728 |
| 2025-10-09 | [UniVideo](../papers/2025-10_UniVideo/解读.md) | 视频编辑与统一创作 | 生成+编辑 | 3,017 |
| 2025-10-13 | [IVEBench](../papers/2025-10_IVEBench/解读.md) | 评测 | 编辑 | 3,684 |
| 2025-10-17 | [Ditto](../papers/2025-10_Ditto/解读.md) | 指令式视频编辑与数据集 | 编辑 | 3,085 |
| 2025-10-28 | [Cosmos-Predict 2.5](../papers/2025-10_Cosmos-Predict-2.5/解读.md) | 世界模型与交互环境 | 生成 | 3,573 |
| 2025-11-24 | [HunyuanVideo 1.5](../papers/2025-11_HunyuanVideo-1.5/解读.md) | 基座架构 | 生成 | 3,204 |
| 2025-12-18 | [Kling-Omni](../papers/2025-12_Kling-Omni/解读.md) | 统一多模态 | 生成+编辑 | 3,105 |
| 2026-03-04 | [Helios](../papers/2026-03_Helios/解读.md) | 长视频与实时流式生成 | 生成 | 3,142 |
| 2026-04-10 | [Matrix-Game 3.0](../papers/2026-04_Matrix-Game-3.0/解读.md) | 世界模型与交互环境 | 生成 | 4,183 |
| 2026-04-15 | [Seedance 2.0](../papers/2026-04_Seedance-2.0/解读.md) | 基座架构 | 生成 | 3,070 |
| 2026-06-25 | [LiveEdit](../papers/2026-06_LiveEdit/解读.md) | 实时与流式编辑 | 编辑 | 3,181 |
| 2026-07-10 | [VidGen-VL](../papers/2026-07_VidGen-VL/解读.md) | 视频模型即通用视觉基座 | 生成 | 3,153 |
| 2026-07-31 | [MiniMax H3](../papers/2026-07_MiniMax-H3/解读.md) | 统一多模态 | 生成 | 3,024 |
| 2026-08-04 | [JoyAI-Video-Edit](../papers/2026-08_JoyAI-Video-Edit/解读.md) | 实时与流式编辑 | 编辑 | 3,110 |

## 可信度边界

解读正文由 DeepSeek V4 Pro 依据原文抽取的文字生成，人定标准、做机器校验（8 节齐全、
3000～5000 汉字、证据表至少 4 行），**未逐句人工复核**。图里的信息模型读不到，
公式符号会在 PDF 抽取时丢失。数字与结论以原文为准。

Sora 那篇的事实来源不是 PDF：报告只发在 OpenAI 官网，且该站拒绝脚本请求（HTTP 403），
正文取自 Internet Archive 2026-08-27 的官方页快照，快照 URL 与抽取文本的 sha256
记在 `papers/2024-02_Sora/meta.json`。

机构一列标 **（未核）** 的，是 OpenAlex 无机构字段、也没回 PDF 首页逐条核过的。

