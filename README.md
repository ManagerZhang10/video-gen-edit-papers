# 视频生成论文库 2023–2026

> 读者：想快速建立视频生成领域坐标系的人
> 范围：2023-11 → 2026-07，按首次公开时间排序
> 本期：第一期 Top 20（解读待生成）
> 最后核对：2026-08-31

## 怎么选的

**影响力 = 已兑现的引用量 + 尚未兑现的业界关注度。** 两个轴分开看，因为它们经常不一致：
HunyuanVideo 有 1614 次引用但只有 12 个 upvote，Kandinsky 5.0 有 236 个 upvote 却只有 9 次引用。

| 轴 | 数据源 | 核对日期 |
| --- | --- | --- |
| 引用量 | Semantic Scholar Graph API | 2026-08-31 |
| 业界关注度（upvote） | Hugging Face Papers API | 2026-08-31 |

2023–2024 只留仍在支撑 2026 工作的那几篇。AnimateDiff（1672 次引用）、MAGVIT-v2（687）、
Movie Gen（629）、VideoPoet（546）、Lumiere（544）、W.A.L.T（351）、GameNGen（280）
引用量都不低，但技术路线已被取代，不占名额。
新论文按引用速率和 upvote 计入——Seedance 2.0 上线 4 个月 101 次引用（25 次/月），
比多数 2024 年论文的当期速率还快。

## 全量清单

| # | 时间 | 简称 | 论文标题 | 发表 | 机构 | 引用 | upvote | 原文 |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- |
| 1 | 2023-11-25 | SVD | Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets | arXiv 预印本 | Stability AI | 2856 | 15 | [arXiv](https://arxiv.org/abs/2311.15127) |
| 2 | 2023-11-29 | VBench | VBench: Comprehensive Benchmark Suite for Video Generative Models | CVPR 2024 | 南洋理工大学 S-Lab / 上海人工智能实验室（未核） | 1842 | 9 | [arXiv](https://arxiv.org/abs/2311.17982) |
| 3 | 2024-02-15 | Sora | Video generation models as world simulators | OpenAI 技术报告（无同行评审） | OpenAI | — | — | [官方页](https://openai.com/index/video-generation-models-as-world-simulators/) |
| 4 | 2024-02-23 | Genie | Genie: Generative Interactive Environments | ICML 2024 | Google DeepMind | 773 | 72 | [arXiv](https://arxiv.org/abs/2402.15391) |
| 5 | 2024-08-12 | CogVideoX | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | ICLR 2025 | 智谱 AI / 清华大学（未核） | 2309 | 37 | [arXiv](https://arxiv.org/abs/2408.06072) |
| 6 | 2024-12-03 | HunyuanVideo | HunyuanVideo: A Systematic Framework For Large Video Generative Models | arXiv 预印本 | 腾讯混元 | 1614 | 12 | [arXiv](https://arxiv.org/abs/2412.03603) |
| 7 | 2024-12-10 | CausVid | From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | CVPR 2025 | MIT / Adobe Research（未核） | 387 | 3 | [arXiv](https://arxiv.org/abs/2412.07772) |
| 8 | 2025-01-07 | Cosmos | Cosmos World Foundation Model Platform for Physical AI | arXiv 预印本 | NVIDIA | 817 | 84 | [arXiv](https://arxiv.org/abs/2501.03575) |
| 9 | 2025-03-10 | VACE | VACE: All-in-One Video Creation and Editing | ICCV 2025 | 阿里巴巴通义实验室 | 472 | 58 | [arXiv](https://arxiv.org/abs/2503.07598) |
| 10 | 2025-03-26 | Wan | Wan: Open and Advanced Large-Scale Video Generative Models | arXiv 预印本 | 阿里巴巴通义实验室 | 2414 | 71 | [arXiv](https://arxiv.org/abs/2503.20314) |
| 11 | 2025-05-12 | DanceGRPO | DanceGRPO: Unleashing GRPO on Visual Generation | arXiv 预印本 | 字节跳动 / 香港大学（未核） | 352 | 34 | [arXiv](https://arxiv.org/abs/2505.07818) |
| 12 | 2025-06-09 | Self Forcing | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | NeurIPS 2025 (Spotlight) | Adobe Research / 德州大学奥斯汀分校（未核） | 519 | 32 | [arXiv](https://arxiv.org/abs/2506.08009) |
| 13 | 2025-06-10 | Seedance 1.0 | Seedance 1.0: Exploring the Boundaries of Video Generation Models | 字节跳动 Seed 技术报告 | 字节跳动 Seed | 242 | 109 | [arXiv](https://arxiv.org/abs/2506.09113) |
| 14 | 2025-09-24 | Chain-of-Frames | Video models are zero-shot learners and reasoners | arXiv 预印本 | Google DeepMind | 203 | 101 | [arXiv](https://arxiv.org/abs/2509.20328) |
| 15 | 2025-11-24 | HunyuanVideo 1.5 | HunyuanVideo 1.5 Technical Report | 腾讯混元技术报告 | 腾讯混元 | 107 | 29 | [arXiv](https://arxiv.org/abs/2511.18870) |
| 16 | 2025-12-18 | Kling-Omni | Kling-Omni Technical Report | 快手可灵技术报告 | 快手可灵 | 50 | 173 | [arXiv](https://arxiv.org/abs/2512.16776) |
| 17 | 2026-02-25 | SkyReels-V4 | SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model | 昆仑万维技术报告 | 昆仑万维 SkyReels（未核） | 10 | 55 | [arXiv](https://arxiv.org/abs/2602.21818) |
| 18 | 2026-04-10 | Matrix-Game 3.0 | Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory | arXiv 预印本 | 昆仑万维 Skywork（未核） | 52 | 51 | [arXiv](https://arxiv.org/abs/2604.08995) |
| 19 | 2026-04-15 | Seedance 2.0 | Seedance 2.0: Advancing Video Generation for World Complexity | 字节跳动 Seed Model Card | 字节跳动 Seed | 101 | 170 | [arXiv](https://arxiv.org/abs/2604.14148) |
| 20 | 2026-07-10 | VidGen-VL | Video Generation Models are General-Purpose Vision Learners | ECCV 2026 | 未核 | 5 | 88 | [arXiv](https://arxiv.org/abs/2607.09024) |

## 凭什么进这 20 个

| 简称 | 理由 |
| --- | --- |
| SVD | 至今引用量最高的视频生成论文；数据策展流程被后续几乎所有工作沿用 |
| VBench | 2026 年的论文仍默认报 VBench 分数，是唯一活下来的评测口径 |
| Sora | 确立 DiT + 时空 patch + 规模化的范式，此后所有基座模型都在这条线上 |
| Genie | world model 这条线的源头，直通 Genie 3 与 2026-01 上线的 Project Genie |
| CogVideoX | 第一个真正可用的开源 DiT 视频模型，3D VAE + expert transformer 成为开源默认结构 |
| HunyuanVideo | 13B 开源权重，把开源与闭源的差距第一次压到可比 |
| CausVid | 引用量不高但是整个 Forcing 家族的根：双向教师蒸馏成因果学生，实时视频生成从这里开始 |
| Cosmos | 把视频生成明确定位成机器人与自动驾驶的数据引擎，开辟 physical AI 应用面 |
| VACE | 生成与编辑统一进一个模型，是 ComfyUI 生态里被实际接得最多的可控方案 |
| Wan | 17 个月 2414 次引用（142 次/月，全表最高）；2026 年绝大多数开源二次开发的底座 |
| DanceGRPO | 把 GRPO 搬到视觉生成，RL 后训练从此成为视频基座的标配环节 |
| Self Forcing | 用学生自 rollout 消掉训练-推理落差，单卡亚秒延迟；衍生出 Rolling / Causal / Sparse / Light Forcing 一整族 |
| Seedance 1.0 | 闭源阵营里少见地把训练与推理加速细节写清楚的报告，1080p/5s 仅 41.4 秒 |
| Chain-of-Frames | 用 Veo 3 在 62 个未训练任务上验证零样本能力，提出 chain-of-frames；把视频模型重新定义为通用视觉基座 |
| HunyuanVideo 1.5 | 8.3B 跑消费级显卡，SSTA 稀疏注意力；把开源视频生成拉回个人可负担区间 |
| Kling-Omni | 173 upvote 是 2025 年底最高热度；生成/编辑/推理统一进一个框架，音画原生同步 |
| SkyReels-V4 | 双流 MMDiT 一支出画一支出音，音画联合的开源代表；2026 年原生音频比画质更能拉开差距 |
| Matrix-Game 3.0 | 实时流式可交互 + 长程记忆，开源阵营对标 Genie 3 的最近位置 |
| Seedance 2.0 | 4 个月 101 次引用（25 次/月，新论文里最快）；Artificial Analysis 视频竞技场第一，全模态条件输入 |
| VidGen-VL | 上线一个月 88 upvote；把 chain-of-frames 那条线推到「视频生成模型即通用视觉学习器」 |

## 已知没核到的

| 项 | 状态 |
| --- | --- |
| 标 **（未核）** 的机构 | OpenAlex 对 arXiv 预印本没有机构字段，且会误配（把 HunyuanVideo 配给 "Applied GeoSolutions"）。可靠来源只有 PDF 首页作者块，尚未拉取 |
| Genie 的 ICML 2024 Best Paper | 会议名经 Semantic Scholar 确认，**最佳论文这一项未核**，故表中只写 ICML 2024 |
| Sora 报告的引用量 | 非 arXiv 条目，Semantic Scholar 与 HF 都无记录，无法给数字 |
| 2026-05 之后的工作 | 只覆盖到 2026-07；最近几个月的新论文可能还没进入检索视野 |

arXiv ID、标题、首次公开日期已全部经 arXiv API 逐条核对，与官方元数据一致。
发表会议经 Semantic Scholar 与 arXiv comment 字段双源确认。
