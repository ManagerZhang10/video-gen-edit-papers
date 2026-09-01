# 视频生成与编辑论文库索引

> 读者：要系统补齐 2023–2026 视频生成技术脉络的人
> 目标：按脉络挑论文，点进任意一篇能直接读完整解读，不用再读原文
> 覆盖：20 项，2023-11 ～ 2026-07
> 最后核对：2026-09-01

[README](../README.md) 是一张按时间排的平表，用来查。本页按技术脉络分组，用来读。
每篇的「一句话」摘自该篇 `解读.md` 第 1 节首句，依据是论文原文，不是另写的导读。

## 任务分布

一篇论文可以同时是生成和编辑——这就是本库按模态而不按任务划分的原因。

| 任务 | 篇数 | 篇目 |
| --- | ---: | --- |
| 生成 | 20 | SVD、VBench、Sora、Genie、CogVideoX、HunyuanVideo、CausVid、Cosmos、VACE、Wan、DanceGRPO、Self Forcing、Seedance 1.0、Chain-of-Frames、HunyuanVideo 1.5、Kling-Omni、Matrix-Game 3.0、Seedance 2.0、VidGen-VL、MiniMax H3 |
| 编辑 | 2 | VACE、Kling-Omni |

## 8 条脉络

### 基座架构（8 篇）

文本到视频的主干怎么搭：潜空间压缩、时空 patch、DiT 规模化，以及各家开源/闭源旗舰的取舍。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-11 | [SVD](../papers/2023-11_SVD/解读.md) | Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets | 方法 | Stable Video Diffusion（SVD）是 Stability AI 提出的潜空间视频扩散模型。 |
| 2024-02 | [Sora](../papers/2024-02_Sora/解读.md) | Video generation models as world simulators | 技术报告 | Sora 解决的是“用一个通用模型从文本、图像或视频生成多时长、多分辨率、多宽高比的高保真视频，并朝物理世界模拟器方向探索”的问题。 |
| 2024-08 | [CogVideoX](../papers/2024-08_CogVideoX/解读.md) | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | 模型 | CogVideoX 是一个基于扩散 Transformer（Diffusion Transformer, DiT）的文本生成视频模型，由清华与智谱 AI 等团队提出。 |
| 2024-12 | [HunyuanVideo](../papers/2024-12_HunyuanVideo/解读.md) | HunyuanVideo: A Systematic Framework For Large Video Generative Models | 技术报告 | HunyuanVideo 是腾讯混元团队在 2024 年 12 月公开的一个 13B 参数开源视频生成基础模型。 |
| 2025-03 | [Wan](../papers/2025-03_Wan/解读.md) | Wan: Open and Advanced Large-Scale Video Generative Models | 技术报告 | Wan 是阿里团队于 2025 年 3 月 26 日发布的开源视频基础模型套件，采用主流的 Diffusion Transformer（DiT，扩散变换器）加 Flow Matching（流匹配）范式。 |
| 2025-06 | [Seedance 1.0](../papers/2025-06_Seedance-1.0/解读.md) | Seedance 1.0: Exploring the Boundaries of Video Generation Models | 技术报告 | Seedance 1.0 是字节跳动 Seed 团队于 2025 年 6 月发布的双语视频生成基础模型（video generation foundation model），统一支持文生视频（T2V）和图生视频（I2V）。 |
| 2025-11 | [HunyuanVideo 1.5](../papers/2025-11_HunyuanVideo-1.5/解读.md) | HunyuanVideo 1.5 Technical Report | 技术报告 | HunyuanVideo 1.5 是腾讯混元团队在 2025 年 11 月 24 日公开的 8.3B 参数开源视频生成模型。 |
| 2026-04 | [Seedance 2.0](../papers/2026-04_Seedance-2.0/解读.md) | Seedance 2.0: Advancing Video Generation for World Complexity | 技术报告 | Seedance 2.0 是字节跳动 Seed 团队提出的“原生多模态音频-视频联合生成模型”，不是单纯视频生成器。 |

### 少步与因果蒸馏（2 篇）

把双向扩散教师蒸馏成因果学生，换来实时与流式生成。CausVid 是根，Self Forcing 消掉训练-推理落差。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2024-12 | [CausVid](../papers/2024-12_CausVid/解读.md) | From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | 方法 | CausVid 解决视频扩散模型“生成慢、不能流式输出”的问题。 |
| 2025-06 | [Self Forcing](../papers/2025-06_Self-Forcing/解读.md) | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | 方法 | Self Forcing 是 Adobe Research 与 UT Austin 提出的自回归视频扩散模型后训练范式，论文发表于 NeurIPS 2025 (Spotlight)。 |

### 统一多模态（2 篇）

生成、编辑、理解、音画同步进一个模型，输入输出都不再单一。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-12 | [Kling-Omni](../papers/2025-12_Kling-Omni/解读.md) | Kling-Omni Technical Report | 技术报告 | Kling-Omni 是快手可灵团队提出的通用视频生成框架，论文定位为“从多模态视觉语言输入直接合成高保真视频”的端到端系统。 |
| 2026-07 | [MiniMax H3](../papers/2026-07_MiniMax-H3/解读.md) | MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities | 技术报告 | MiniMax H3 是 MiniMax 官方在 2026-07-31 发布的一款通用多模态生成模型。 |

### 世界模型与交互环境（3 篇）

视频模型当可交互环境用：接受动作输入、保持长程记忆，服务机器人、自动驾驶和游戏。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2024-02 | [Genie](../papers/2024-02_Genie/解读.md) | Genie: Generative Interactive Environments | 方法 | Genie 是一个生成式交互环境（generative interactive environments）模型，由 Google DeepMind 提出，发表于 ICML 2024。 |
| 2025-01 | [Cosmos](../papers/2025-01_Cosmos/解读.md) | Cosmos World Foundation Model Platform for Physical AI | 技术报告 | 这篇论文（arXiv:2501.03575，2025年1月公开）是 NVIDIA 提出的 Cosmos 世界基础模型平台，面向 Physical AI（具备传感器与执行器的 AI 系统）。 |
| 2026-04 | [Matrix-Game 3.0](../papers/2026-04_Matrix-Game-3.0/解读.md) | Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory | 方法 | Matrix-Game 3.0 是 Skywork AI 提出的交互式世界模型（interactive world model），目标是同时解决两个此前难以兼得的能力：分钟级长时记忆一致性，以及 720p 分辨率下的实时生成。 |

### 视频模型即通用视觉基座（2 篇）

不训练也能做未见过的视觉任务——把视频生成模型当成视觉领域的 GPT-3 时刻来验证。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-09 | [Chain-of-Frames](../papers/2025-09_Chain-of-Frames/解读.md) | Video models are zero-shot learners and reasoners | 方法 | 本文《Video models are zero-shot learners and reasoners》用 Google DeepMind 的商用视频生成模型 Veo 3 做零样本视觉任务实验，核心论点是：视频模型正在走 LLM 从“任务专用模型”到“通用基础模型”的老路。 |
| 2026-07 | [VidGen-VL](../papers/2026-07_VidGen-VL/解读.md) | Video Generation Models are General-Purpose Vision Learners | 方法 | 这篇论文提出 **GenCeption**：一个把预训练文本到视频扩散模型（基于 WAN 2.1）改造为单步前馈的通用视觉感知模型。 |

### 视频编辑与统一创作（1 篇）

输入已有视频并改动它。当前只有生成/编辑统一的工作，专门的视频编辑论文尚未收。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-03 | [VACE](../papers/2025-03_VACE/解读.md) | VACE: All-in-One Video Creation and Editing | 方法 | VACE 是阿里通义实验室提出的统一视频生成与编辑模型，发表于 ICCV 2025（首次公开 2025/03/10）。 |

### RL 与对齐（1 篇）

生成质量与人类偏好对齐：把 GRPO 一类的策略优化搬到视觉生成上。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2025-05 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | 奖励与 RL | DanceGRPO 是字节跳动 Seed 与香港大学合作的 arXiv 预印本，核心工作是把大语言模型强化学习中的 GRPO（Group Relative Policy Optimization，组相对策略优化）迁移到视觉生成。 |

### 评测（1 篇）

怎么量一个视频模型的好坏。VBench 是这个领域唯一活下来的通用口径。

| 时间 | 简称 | 论文标题 | 类型 | 一句话 |
| --- | --- | --- | --- | --- |
| 2023-11 | [VBench](../papers/2023-11_VBench/解读.md) | VBench: Comprehensive Benchmark Suite for Video Generative Models | 基准 | VBench 是一个面向文本到视频生成模型（T2V）的综合评测基准套件。 |

## 按时间的全量清单

带发表、机构、引用、upvote 的完整版在 [README](../README.md#全量清单)。

| 时间 | 简称 | 脉络 | 任务 | 解读字数 |
| --- | --- | --- | --- | ---: |
| 2023-11-25 | [SVD](../papers/2023-11_SVD/解读.md) | 基座架构 | 生成 | 3,325 |
| 2023-11-29 | [VBench](../papers/2023-11_VBench/解读.md) | 评测 | 生成 | 3,790 |
| 2024-02-15 | [Sora](../papers/2024-02_Sora/解读.md) | 基座架构 | 生成 | 4,072 |
| 2024-02-23 | [Genie](../papers/2024-02_Genie/解读.md) | 世界模型与交互环境 | 生成 | 3,522 |
| 2024-08-12 | [CogVideoX](../papers/2024-08_CogVideoX/解读.md) | 基座架构 | 生成 | 4,048 |
| 2024-12-03 | [HunyuanVideo](../papers/2024-12_HunyuanVideo/解读.md) | 基座架构 | 生成 | 3,576 |
| 2024-12-10 | [CausVid](../papers/2024-12_CausVid/解读.md) | 少步与因果蒸馏 | 生成 | 3,893 |
| 2025-01-07 | [Cosmos](../papers/2025-01_Cosmos/解读.md) | 世界模型与交互环境 | 生成 | 3,379 |
| 2025-03-10 | [VACE](../papers/2025-03_VACE/解读.md) | 视频编辑与统一创作 | 生成+编辑 | 3,042 |
| 2025-03-26 | [Wan](../papers/2025-03_Wan/解读.md) | 基座架构 | 生成 | 3,259 |
| 2025-05-12 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | RL 与对齐 | 生成 | 3,697 |
| 2025-06-09 | [Self Forcing](../papers/2025-06_Self-Forcing/解读.md) | 少步与因果蒸馏 | 生成 | 3,493 |
| 2025-06-10 | [Seedance 1.0](../papers/2025-06_Seedance-1.0/解读.md) | 基座架构 | 生成 | 3,861 |
| 2025-09-24 | [Chain-of-Frames](../papers/2025-09_Chain-of-Frames/解读.md) | 视频模型即通用视觉基座 | 生成 | 3,243 |
| 2025-11-24 | [HunyuanVideo 1.5](../papers/2025-11_HunyuanVideo-1.5/解读.md) | 基座架构 | 生成 | 3,204 |
| 2025-12-18 | [Kling-Omni](../papers/2025-12_Kling-Omni/解读.md) | 统一多模态 | 生成+编辑 | 3,105 |
| 2026-04-10 | [Matrix-Game 3.0](../papers/2026-04_Matrix-Game-3.0/解读.md) | 世界模型与交互环境 | 生成 | 4,183 |
| 2026-04-15 | [Seedance 2.0](../papers/2026-04_Seedance-2.0/解读.md) | 基座架构 | 生成 | 3,070 |
| 2026-07-10 | [VidGen-VL](../papers/2026-07_VidGen-VL/解读.md) | 视频模型即通用视觉基座 | 生成 | 3,153 |
| 2026-07-31 | [MiniMax H3](../papers/2026-07_MiniMax-H3/解读.md) | 统一多模态 | 生成 | 3,024 |

## 可信度边界

解读正文由 DeepSeek V4 Pro 依据原文抽取的文字生成，人定标准、做机器校验（8 节齐全、
3000～5000 汉字、证据表至少 4 行），**未逐句人工复核**。图里的信息模型读不到，
公式符号会在 PDF 抽取时丢失。数字与结论以原文为准。

Sora 那篇的事实来源不是 PDF：报告只发在 OpenAI 官网，且该站拒绝脚本请求（HTTP 403），
正文取自 Internet Archive 2026-08-27 的官方页快照，快照 URL 与抽取文本的 sha256
记在 `papers/2024-02_Sora/meta.json`。

机构一列标 **（未核）** 的，是 OpenAlex 无机构字段、也没回 PDF 首页逐条核过的。

