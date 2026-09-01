# 视频生成与编辑论文库 2022–2026

[![papers](https://img.shields.io/badge/papers-50-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-172K_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-2022.04_--_2026.08-e07b39)](#全量清单)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**50 篇视频生成与编辑领域最有影响力的论文，每篇一份中文解读，外加一条核验过的原文直链。**
时间跨度 2022-04 → 2026-08，解读合计 172,110 个汉字。

*50 most influential video generation & editing papers, each with a Chinese reading note and a verified link to the source. 2022-04 – 2026-08.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE) · **最后核对** 2026-09-02
>
> ⚠️ **解读正文由 DeepSeek V4 Pro 依据原文抽取的文字生成**，人定标准、做机器校验，未逐句人工复核。
> 图里的信息模型读不到，公式符号会在 PDF 抽取时丢失。要抠实现细节仍需回原文。

---

## 这个库收什么

**按模态划分，不按生成/编辑划分。** 视频生成与视频编辑放在同一个库里，因为一篇论文
经常同时是两者——VACE 把生成与编辑统一进一个模型，Kling-Omni 也是。硬要按任务拆仓库，
这类论文只能任意归到一边，或者被复制成两份笔记。所以任务是 `papers.json` 里的一个
**可多值**字段，不是目录边界：

| 任务 | 篇数 |
| --- | ---: |
| 生成 | 38 |
| 编辑 | 20 |

其中 8 篇同时是两者（生成/编辑统一的模型）：Tune-A-Video、Gen-1、Text2Video-Zero、VACE、ReCamMaster、EditVerse、UniVideo、Kling-Omni。

图像侧的生成与编辑在另一个库：[image-gen-edit-papers](https://github.com/ManagerYu10/image-gen-edit-papers)。

## 怎么用

拉到[全量清单](#全量清单)，50 行按时间排。每行两列可以点：**简称**去解读，**原文**去 arXiv 或官方页。
按技术脉络分组的视图在 [docs/INDEX.md](docs/INDEX.md)。

原文 PDF 不在仓库里（被 `.gitignore` 挡住）。批量拉到本地：

```bash
python3 scripts/fetch_pdfs.py          # 补齐所有缺的
python3 scripts/fetch_pdfs.py --list   # 只列缺什么
```

生成解读的 prompt 是 [docs/prompt.md](docs/prompt.md)，跟仓库一起提交，别人可以复现。
想公开转载全文翻译先看 [docs/许可清单.md](docs/许可清单.md)——50 篇里只有 4 篇的许可允许公开发布译文。

## 怎么选的

**影响力 = 已兑现的引用量 + 尚未兑现的业界关注度。** 两个轴分开列、不合成单一分数，
因为它们经常打架：HunyuanVideo 有 1,614 次引用但只有 12 个 upvote；CausVid 只有 3 个 upvote，
却是整个 Forcing 家族的根。

| 轴 | 数据源 | 核对日期 |
| --- | --- | --- |
| 引用量 | Semantic Scholar Graph API | 2026-08-31 |
| 业界关注度（upvote） | Hugging Face Papers API | 2026-08-31 |

**技术路线已被取代的不占名额**，无论引用量多高：AnimateDiff（1,672 次引用）、
Make-A-Video（2,154）、Imagen Video（2,140）、Align Your Latents（1,768，潜空间视频扩散
奠基，但库里的 SVD 是它的直接后继）、MAGVIT-v2（687）、Movie Gen（629）、VideoPoet（546）、
Lumiere（544）、W.A.L.T（351）、GameNGen（280）都在这条规则下落选。

2026-09-02 从 20 篇扩到 50 篇，重点是补上视频编辑——改名成「生成与编辑」之后，
原来 20 篇里只有 2 篇沾编辑。这一轮的候选池、双轴快照、以及每一篇被换下来的理由，
见 [docs/清单扩充_2026-09.md](docs/清单扩充_2026-09.md)。

新工作按引用速率和 upvote 计入，不按绝对引用量——Seedance 2.0 上线 4 个月 101 次引用
（25 次/月），比多数 2024 年论文的当期速率还快。两项没有 arXiv 条目的官方技术报告
（Sora、MiniMax H3）没有可比数据，按技术影响单独判断。

## 技术脉络

| 脉络 | 篇数 | 篇目 |
| --- | ---: | --- |
| 基座架构 | 12 | VDM、SVD、Sora、CogVideoX、HunyuanVideo、Open-Sora、LTX-Video、Wan、MAGI-1、Seedance 1.0、HunyuanVideo 1.5、Seedance 2.0 |
| 训练-free 视频编辑 | 6 | Tune-A-Video、FateZero、Text2Video-Zero、Rerender-A-Video、TokenFlow、VideoGrain |
| 视频编辑与统一创作 | 4 | Gen-1、VACE、EditVerse、UniVideo |
| 世界模型与交互环境 | 4 | Genie、Cosmos、Cosmos-Predict 2.5、Matrix-Game 3.0 |
| 指令式视频编辑与数据集 | 3 | InsV2V、Señorita-2M、Ditto |
| 评测 | 3 | VBench、VBench-2.0、IVEBench |
| 长视频与实时流式生成 | 3 | LongLive、Self-Forcing++、Helios |
| 可控生成与运动控制 | 2 | Animate Anyone、ReCamMaster |
| 少步与因果蒸馏 | 2 | CausVid、Self Forcing |
| RL 与对齐 | 2 | VideoReward、DanceGRPO |
| 视频修补与物体移除 | 2 | VideoPainter、MiniMax-Remover |
| 视频模型即通用视觉基座 | 2 | Chain-of-Frames、VidGen-VL |
| 统一多模态 | 2 | Kling-Omni、MiniMax H3 |
| 实时与流式编辑 | 2 | LiveEdit、JoyAI-Video-Edit |
| 推理效率与稀疏注意力 | 1 | Sparse VideoGen |

逐篇归入哪条脉络、每条脉络怎么串起来，见 [docs/INDEX.md](docs/INDEX.md)。

## 全量清单

| # | 时间 | 简称（→ 解读） | 论文标题 | 发表 | 机构 | 任务 | 原文 | 解读字数 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| 1 | 2022-04-07 | [VDM](papers/2022-04_VDM/解读.md) | Video Diffusion Models | NeurIPS 2022 | 谷歌 | 生成 | [arXiv](https://arxiv.org/abs/2204.03458) | 3,239 |
| 2 | 2022-12-22 | [Tune-A-Video](papers/2022-12_Tune-A-Video/解读.md) | Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation | ICCV 2023 | 新加坡国立大学 Show Lab / 腾讯 PCG ARC Lab | 生成+编辑 | [arXiv](https://arxiv.org/abs/2212.11565) | 3,120 |
| 3 | 2023-02-06 | [Gen-1](papers/2023-02_Gen-1/解读.md) | Structure and Content-Guided Video Synthesis with Diffusion Models | ICCV 2023 | Runway | 生成+编辑 | [arXiv](https://arxiv.org/abs/2302.03011) | 3,720 |
| 4 | 2023-03-16 | [FateZero](papers/2023-03_FateZero/解读.md) | FateZero: Fusing Attentions for Zero-shot Text-based Video Editing | ICCV 2023 (Oral) | 香港科技大学 / 腾讯 AI Lab / 中国科学院香港创新研究院 | 编辑 | [arXiv](https://arxiv.org/abs/2303.09535) | 3,653 |
| 5 | 2023-03-23 | [Text2Video-Zero](papers/2023-03_Text2Video-Zero/解读.md) | Text2Video-Zero: Text-to-Image Diffusion Models are Zero-Shot Video Generators | ICCV 2023 | Picsart AI Research (PAIR) / 得克萨斯大学奥斯汀分校 / 俄勒冈大学 等 4 家 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2303.13439) | 3,415 |
| 6 | 2023-06-13 | [Rerender-A-Video](papers/2023-06_Rerender-A-Video/解读.md) | Rerender A Video: Zero-Shot Text-Guided Video-to-Video Translation | SIGGRAPH Asia 2023 | 南洋理工大学 S-Lab | 编辑 | [arXiv](https://arxiv.org/abs/2306.07954) | 3,692 |
| 7 | 2023-07-19 | [TokenFlow](papers/2023-07_TokenFlow/解读.md) | TokenFlow: Consistent Diffusion Features for Consistent Video Editing | ICLR（年份未核） | 魏茨曼科学研究所 | 编辑 | [arXiv](https://arxiv.org/abs/2307.10373) | 3,867 |
| 8 | 2023-11-01 | [InsV2V](papers/2023-11_InsV2V/解读.md) | Consistent Video-to-Video Transfer Using Synthetic Dataset | ICLR 2024 | 亚马逊云科技上海人工智能实验室 | 编辑 | [arXiv](https://arxiv.org/abs/2311.00213) | 3,145 |
| 9 | 2023-11-25 | [SVD](papers/2023-11_SVD/解读.md) | Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets | arXiv 预印本 | Stability AI | 生成 | [arXiv](https://arxiv.org/abs/2311.15127) | 3,325 |
| 10 | 2023-11-28 | [Animate Anyone](papers/2023-11_Animate-Anyone/解读.md) | Animate Anyone: Consistent and Controllable Image-to-Video Synthesis for Character Animation | CVPR 2024 | 阿里巴巴智能计算研究院 | 生成 | [arXiv](https://arxiv.org/abs/2311.17117) | 3,036 |
| 11 | 2023-11-29 | [VBench](papers/2023-11_VBench/解读.md) | VBench: Comprehensive Benchmark Suite for Video Generative Models | CVPR 2024 | 南洋理工大学 S-Lab / 上海人工智能实验室 / 香港中文大学 等 4 家 | 生成 | [arXiv](https://arxiv.org/abs/2311.17982) | 3,790 |
| 12 | 2024-02-15 | [Sora](papers/2024-02_Sora/解读.md) | Video generation models as world simulators | OpenAI 技术报告（无同行评审） | OpenAI | 生成 | [官方页](https://openai.com/index/video-generation-models-as-world-simulators/) | 4,072 |
| 13 | 2024-02-23 | [Genie](papers/2024-02_Genie/解读.md) | Genie: Generative Interactive Environments | ICML 2024 | Google DeepMind | 生成 | [arXiv](https://arxiv.org/abs/2402.15391) | 3,522 |
| 14 | 2024-08-12 | [CogVideoX](papers/2024-08_CogVideoX/解读.md) | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | ICLR 2025 | 清华大学 / 智谱AI | 生成 | [arXiv](https://arxiv.org/abs/2408.06072) | 4,048 |
| 15 | 2024-12-03 | [HunyuanVideo](papers/2024-12_HunyuanVideo/解读.md) | HunyuanVideo: A Systematic Framework For Large Video Generative Models | arXiv 预印本 | 腾讯混元 | 生成 | [arXiv](https://arxiv.org/abs/2412.03603) | 3,576 |
| 16 | 2024-12-10 | [CausVid](papers/2024-12_CausVid/解读.md) | From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | CVPR 2025 | 麻省理工学院 / Adobe | 生成 | [arXiv](https://arxiv.org/abs/2412.07772) | 3,893 |
| 17 | 2024-12-29 | [Open-Sora](papers/2024-12_Open-Sora/解读.md) | Open-Sora: Democratizing Efficient Video Production for All | arXiv 预印本 | HPC-AI Tech | 生成 | [arXiv](https://arxiv.org/abs/2412.20404) | 3,259 |
| 18 | 2024-12-30 | [LTX-Video](papers/2024-12_LTX-Video/解读.md) | LTX-Video: Realtime Video Latent Diffusion | arXiv 预印本 | Lightricks | 生成 | [arXiv](https://arxiv.org/abs/2501.00103) | 3,510 |
| 19 | 2025-01-07 | [Cosmos](papers/2025-01_Cosmos/解读.md) | Cosmos World Foundation Model Platform for Physical AI | arXiv 预印本 | NVIDIA | 生成 | [arXiv](https://arxiv.org/abs/2501.03575) | 3,379 |
| 20 | 2025-01-23 | [VideoReward](papers/2025-01_VideoReward/解读.md) | Improving Video Generation with Human Feedback | NeurIPS（年份未核） | 香港中文大学 MMLab / 清华大学 / 快手 Kling 团队 等 5 家 | 生成 | [arXiv](https://arxiv.org/abs/2501.13918) | 3,548 |
| 21 | 2025-02-03 | [Sparse VideoGen](papers/2025-02_Sparse-VideoGen/解读.md) | Sparse VideoGen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity | ICML（年份未核） | 加州大学伯克利分校 / 麻省理工学院 / 英伟达 等 4 家 | 生成 | [arXiv](https://arxiv.org/abs/2502.01776) | 3,190 |
| 22 | 2025-02-10 | [Señorita-2M](papers/2025-02_Señorita-2M/解读.md) | Señorita-2M: A High-Quality Instruction-based Dataset for General Video Editing by Video Specialists | NeurIPS（年份未核） | 香港中文大学 / 香港理工大学 / 清华大学 等 5 家 | 编辑 | [arXiv](https://arxiv.org/abs/2502.06734) | 3,151 |
| 23 | 2025-02-24 | [VideoGrain](papers/2025-02_VideoGrain/解读.md) | VideoGrain: Modulating Space-Time Attention for Multi-grained Video Editing | ICLR 2025 | 悉尼科技大学 / 浙江大学 | 编辑 | [arXiv](https://arxiv.org/abs/2502.17258) | 3,737 |
| 24 | 2025-03-07 | [VideoPainter](papers/2025-03_VideoPainter/解读.md) | VideoPainter: Any-length Video Inpainting and Editing with Plug-and-Play Context Control | SIGGRAPH（年份未核） | 香港中文大学 / 腾讯 ARC Lab / 东京大学 等 4 家 | 编辑 | [arXiv](https://arxiv.org/abs/2503.05639) | 3,157 |
| 25 | 2025-03-10 | [VACE](papers/2025-03_VACE/解读.md) | VACE: All-in-One Video Creation and Editing | ICCV 2025 | 阿里巴巴通义实验室 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2503.07598) | 3,042 |
| 26 | 2025-03-14 | [ReCamMaster](papers/2025-03_ReCamMaster/解读.md) | ReCamMaster: Camera-Controlled Generative Rendering from A Single Video | ICCV 2025 | 浙江大学 / 快手可灵团队 / 香港中文大学 等 4 家 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2503.11647) | 3,669 |
| 27 | 2025-03-26 | [Wan](papers/2025-03_Wan/解读.md) | Wan: Open and Advanced Large-Scale Video Generative Models | arXiv 预印本 | 阿里巴巴通义实验室 | 生成 | [arXiv](https://arxiv.org/abs/2503.20314) | 3,259 |
| 28 | 2025-03-27 | [VBench-2.0](papers/2025-03_VBench-2.0/解读.md) | VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness | arXiv 预印本 | 上海人工智能实验室 / 南洋理工大学 / 中山大学 等 4 家 | 生成 | [arXiv](https://arxiv.org/abs/2503.21755) | 3,009 |
| 29 | 2025-05-12 | [DanceGRPO](papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | arXiv 预印本 | 字节跳动 Seed / 香港大学 | 生成 | [arXiv](https://arxiv.org/abs/2505.07818) | 3,697 |
| 30 | 2025-05-19 | [MAGI-1](papers/2025-05_MAGI-1/解读.md) | MAGI-1: Autoregressive Video Generation at Scale | arXiv 预印本 | Sand AI | 生成 | [arXiv](https://arxiv.org/abs/2505.13211) | 3,834 |
| 31 | 2025-05-30 | [MiniMax-Remover](papers/2025-05_MiniMax-Remover/解读.md) | MiniMax-Remover: Taming Bad Noise Helps Video Object Removal | NeurIPS 2025 | 香港中文大学 / 深圳大学 / IntelliFusion Inc. 等 5 家 | 编辑 | [arXiv](https://arxiv.org/abs/2505.24873) | 3,565 |
| 32 | 2025-06-09 | [Self Forcing](papers/2025-06_Self-Forcing/解读.md) | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | NeurIPS 2025 (Spotlight) | Adobe Research / 德克萨斯大学奥斯汀分校 | 生成 | [arXiv](https://arxiv.org/abs/2506.08009) | 3,493 |
| 33 | 2025-06-10 | [Seedance 1.0](papers/2025-06_Seedance-1.0/解读.md) | Seedance 1.0: Exploring the Boundaries of Video Generation Models | 字节跳动 Seed 技术报告 | 字节跳动 Seed | 生成 | [arXiv](https://arxiv.org/abs/2506.09113) | 3,861 |
| 34 | 2025-09-24 | [Chain-of-Frames](papers/2025-09_Chain-of-Frames/解读.md) | Video models are zero-shot learners and reasoners | arXiv 预印本 | Google DeepMind | 生成 | [arXiv](https://arxiv.org/abs/2509.20328) | 3,243 |
| 35 | 2025-09-24 | [EditVerse](papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | arXiv 预印本 | Adobe Research / 香港中文大学 / 约翰斯·霍普金斯大学 等 4 家 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2509.20360) | 3,456 |
| 36 | 2025-09-26 | [LongLive](papers/2025-09_LongLive/解读.md) | LongLive: Real-time Interactive Long Video Generation | arXiv 预印本 | 英伟达 / 香港科技大学（广州） / 香港大学 等 5 家 | 生成 | [arXiv](https://arxiv.org/abs/2509.22622) | 3,679 |
| 37 | 2025-10-02 | [Self-Forcing++](papers/2025-10_Self-Forcing++/解读.md) | Self-Forcing++: Towards Minute-Scale High-Quality Video Generation | arXiv 预印本 | 加州大学洛杉矶分校 / 字节跳动 Seed / 中佛罗里达大学 | 生成 | [arXiv](https://arxiv.org/abs/2510.02283) | 3,728 |
| 38 | 2025-10-09 | [UniVideo](papers/2025-10_UniVideo/解读.md) | UniVideo: Unified Understanding, Generation, and Editing for Videos | arXiv 预印本 | 滑铁卢大学 / 快手科技 Kling 团队 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2510.08377) | 3,017 |
| 39 | 2025-10-13 | [IVEBench](papers/2025-10_IVEBench/解读.md) | IVEBench: Modern Benchmark Suite for Instruction-Guided Video Editing Assessment | ICLR 2026 | 浙江大学 / 腾讯优图实验室 / 上海交通大学 等 5 家 | 编辑 | [arXiv](https://arxiv.org/abs/2510.11647) | 3,684 |
| 40 | 2025-10-17 | [Ditto](papers/2025-10_Ditto/解读.md) | Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset | arXiv 预印本 | 香港科技大学 / 蚂蚁集团 / 浙江大学 等 4 家 | 编辑 | [arXiv](https://arxiv.org/abs/2510.15742) | 3,085 |
| 41 | 2025-10-28 | [Cosmos-Predict 2.5](papers/2025-10_Cosmos-Predict-2.5/解读.md) | World Simulation with Video Foundation Models for Physical AI | arXiv 预印本 | 英伟达 | 生成 | [arXiv](https://arxiv.org/abs/2511.00062) | 3,573 |
| 42 | 2025-11-24 | [HunyuanVideo 1.5](papers/2025-11_HunyuanVideo-1.5/解读.md) | HunyuanVideo 1.5 Technical Report | 腾讯混元技术报告 | 腾讯混元 | 生成 | [arXiv](https://arxiv.org/abs/2511.18870) | 3,204 |
| 43 | 2025-12-18 | [Kling-Omni](papers/2025-12_Kling-Omni/解读.md) | Kling-Omni Technical Report | 快手可灵技术报告 | 快手可灵 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2512.16776) | 3,105 |
| 44 | 2026-03-04 | [Helios](papers/2026-03_Helios/解读.md) | Helios: Real Real-Time Long Video Generation Model | arXiv 预印本 | 北京大学 / 字节跳动（中国） / Canva可画 等 4 家 | 生成 | [arXiv](https://arxiv.org/abs/2603.04379) | 3,142 |
| 45 | 2026-04-10 | [Matrix-Game 3.0](papers/2026-04_Matrix-Game-3.0/解读.md) | Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory | arXiv 预印本 | Skywork AI | 生成 | [arXiv](https://arxiv.org/abs/2604.08995) | 4,183 |
| 46 | 2026-04-15 | [Seedance 2.0](papers/2026-04_Seedance-2.0/解读.md) | Seedance 2.0: Advancing Video Generation for World Complexity | 字节跳动 Seed Model Card | 字节跳动 Seed | 生成 | [arXiv](https://arxiv.org/abs/2604.14148) | 3,070 |
| 47 | 2026-06-25 | [LiveEdit](papers/2026-06_LiveEdit/解读.md) | LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing | ECCV 2026 | 清华大学 / 香港科技大学 | 编辑 | [arXiv](https://arxiv.org/abs/2606.26740) | 3,181 |
| 48 | 2026-07-10 | [VidGen-VL](papers/2026-07_VidGen-VL/解读.md) | Video Generation Models are General-Purpose Vision Learners | ECCV 2026 | 谷歌DeepMind / 多伦多大学 / 伦敦大学学院 等 5 家 | 生成 | [arXiv](https://arxiv.org/abs/2607.09024) | 3,153 |
| 49 | 2026-07-31 | [MiniMax H3](papers/2026-07_MiniMax-H3/解读.md) | MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities | MiniMax 官方技术报告（完整版未发布） | MiniMax | 生成 | [官方页](https://www.minimax.io/blog/minimax-h3) | 3,024 |
| 50 | 2026-08-04 | [JoyAI-Video-Edit](papers/2026-08_JoyAI-Video-Edit/解读.md) | JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion | arXiv 预印本 | 京东 Joy Future Academy | 编辑 | [arXiv](https://arxiv.org/abs/2608.03974) | 3,110 |

## 凭什么进这 50 个

引用量与 upvote 是选文判据，不进主表。核对日期 2026-08-31。

| 简称 | 类型 | 引用 | upvote | 理由 |
| --- | --- | ---: | ---: | --- |
| VDM | 方法 | 2,834 | 5 | 视频扩散的原始论文，2834 次引用（53.7 次/月，全库最高绝对量）；3D U-Net + 梯度法联合条件采样是后续所有视频扩散工作的共同起点 |
| Tune-A-Video | 方法 | 1,201 | 3 | 1201 次引用（27.1 次/月）；单视频一次调优就能改内容，「拿图像扩散模型当视频编辑器」这条线的根，2023 年几乎所有编辑方法都以它为基线 |
| Gen-1 | 方法 | 766 | 1 | 766 次引用（17.9 次/月）；Runway Gen-1 的论文，第一个商业化的 video-to-video 模型，把结构与内容解耦成两路条件 |
| FateZero | 方法 | 565 | 1 | 565 次引用；第一篇专做零样本文本视频编辑的论文，反演期存注意力图、编辑期融合，training-free 编辑的注意力操控范式从这里定型 |
| Text2Video-Zero | 方法 | 872 | 6 | 872 次引用（21.1 次/月）；不训练、不微调，只改潜码运动与跨帧注意力就把 SD 变成视频模型，也是最早接 ControlNet / InstructPix2Pix 做条件编辑的工作 |
| Rerender-A-Video | 方法 | 340 | 113 | 113 upvote 是全部视频编辑论文里最高的一档；关键帧翻译 + 光流传播的两段式结构被后续大量长视频编辑工作沿用 |
| TokenFlow | 方法 | 509 | 58 | 509 次引用、58 upvote；发现扩散特征本身就带帧间对应关系，据此显式强制特征一致，是「一致性从哪来」这个问题的标准答案 |
| InsV2V | 方法 | 75 | 1 | 引用只有 75 次，但是指令式视频编辑这条线的根：先用 Prompt-to-Prompt 合成成对视频数据，再训一个不需要逐视频微调的编辑模型，Señorita-2M / Ditto / OpenVE-3M 全在这条路上 |
| SVD | 方法 | 2,856 | 15 | 至今引用量最高的视频生成论文；数据策展流程被后续几乎所有工作沿用 |
| Animate Anyone | 方法 | 861 | 6 | 861 次引用（26.0 次/月）；ReferenceNet + 姿态引导，人物动画这条商业化最深的支线的根，直通 OmniHuman / Wan-Animate |
| VBench | 基准 | 1,842 | 9 | 2026 年的论文仍默认报 VBench 分数，是唯一活下来的评测口径 |
| Sora | 技术报告 | — | — | 确立 DiT + 时空 patch + 规模化的范式，此后所有基座模型都在这条线上 |
| Genie | 方法 | 773 | 72 | world model 这条线的源头，直通 Genie 3 与 2026-01 上线的 Project Genie |
| CogVideoX | 模型 | 2,309 | 37 | 第一个真正可用的开源 DiT 视频模型，3D VAE + expert transformer 成为开源默认结构 |
| HunyuanVideo | 技术报告 | 1,614 | 12 | 13B 开源权重，把开源与闭源的差距第一次压到可比 |
| CausVid | 方法 | 387 | 3 | 引用量不高但是整个 Forcing 家族的根：双向教师蒸馏成因果学生，实时视频生成从这里开始 |
| Open-Sora | 技术报告 | 786 | 1 | 786 次引用、39.2 次/月，是 2024 年论文里引用速率第二高的（仅次于 Wan）；完整开源的 Sora 复现路线，训练成本与配方全公开 |
| LTX-Video | 模型 | 543 | 51 | 543 次引用（27.1 次/月）、51 upvote；1:192 高压缩 VAE 把生成拉进实时区间，2B 规模是消费级显卡上第一个能跑的开源 DiT 视频模型 |
| Cosmos | 技术报告 | 817 | 84 | 把视频生成明确定位成机器人与自动驾驶的数据引擎，开辟 physical AI 应用面 |
| VideoReward | 奖励与 RL | 251 | 55 | 251 次引用（13.1 次/月）、55 upvote；多维人类偏好数据集 + VideoReward 奖励模型 + 三种 flow 对齐算法，是 DanceGRPO 之后 RL 后训练的奖励侧事实标准 |
| Sparse VideoGen | 方法 | 200 | 3 | 200 次引用（10.6 次/月）；把 3D 全注意力头分成空间头与时间头再在线稀疏化，training-free 加速 2 倍以上，是 2025–2026 稀疏注意力加速（含 HunyuanVideo 1.5 的 SSTA）这条线的起点 |
| Señorita-2M | 数据集 | 62 | 1 | 把编辑数据规模一次拉到 200 万对，用一组编辑专家模型而非通用模型造数据；2025 年之后的指令编辑模型基本都在它或它的后继数据集上训 |
| VideoGrain | 方法 | 60 | 79 | 79 upvote 是 2025 年 training-free 编辑里最高的；把编辑粒度显式拆到类别 / 实例 / 部件三级，解决多主体编辑互相污染的问题 |
| VideoPainter | 方法 | 84 | 29 | 84 次引用（4.7 次/月）、29 upvote；即插即用的上下文编码器接在 DiT 上做任意长度视频修补，把 inpainting 从 UNet 时代搬进 DiT 时代 |
| VACE | 方法 | 472 | 58 | 生成与编辑统一进一个模型，是 ComfyUI 生态里被实际接得最多的可控方案 |
| ReCamMaster | 方法 | 277 | 148 | 277 次引用（15.8 次/月）、148 upvote，两轴都在 2025 年前列；给定单段已有视频重打相机轨迹，是「视频重拍」这类相机级编辑的代表 |
| Wan | 技术报告 | 2,414 | 71 | 17 个月 2414 次引用（142 次/月，全表最高）；2026 年绝大多数开源二次开发的底座 |
| VBench-2.0 | 基准 | 250 | 33 | 250 次引用（14.6 次/月）；VBench 的直接后继，从表观质量转向内在忠实度（物理常识、常识推理、可控性），2026 年的报告开始双榜同报 |
| DanceGRPO | 奖励与 RL | 352 | 34 | 把 GRPO 搬到视觉生成，RL 后训练从此成为视频基座的标配环节 |
| MAGI-1 | 技术报告 | 250 | 5 | 250 次引用（16.2 次/月）；24B、按 chunk 自回归去噪，峰值显存与视频长度无关，是开源阵营里 chunk 级自回归路线最完整的一份报告 |
| MiniMax-Remover | 方法 | 41 | 4 | 两阶段极简架构 + 「坏噪声」分析，6 步就能做视频物体擦除；是 ComfyUI 生态里实际被接得最多的开源 removal 方案 |
| Self Forcing | 方法 | 519 | 32 | 用学生自 rollout 消掉训练-推理落差，单卡亚秒延迟；衍生出 Rolling / Causal / Sparse / Light Forcing 一整族 |
| Seedance 1.0 | 技术报告 | 242 | 109 | 闭源阵营里少见地把训练与推理加速细节写清楚的报告，1080p/5s 仅 41.4 秒 |
| Chain-of-Frames | 方法 | 203 | 101 | 用 Veo 3 在 62 个未训练任务上验证零样本能力，提出 chain-of-frames；把视频模型重新定义为通用视觉基座 |
| EditVerse | 方法 | 50 | 18 | 50 次引用（4.5 次/月）；把文本 / 图像 / 视频统一成一条 token 序列靠自注意力做 in-context 学习，并自建 232K 视频编辑样本补数据缺口 |
| LongLive | 方法 | 211 | 190 | 211 次引用（19.0 次/月）+ 190 upvote，两轴都是 2025 年下半年最高档；帧级自回归 + 流式换 prompt，把长视频从「离线批量」变成「实时可交互」 |
| Self-Forcing++ | 方法 | 167 | 98 | 167 次引用（15.3 次/月）、98 upvote；不需要长视频教师也不需要长视频数据，把 Self Forcing 从秒级推到分钟级，是 Forcing 家族当前的长时基线 |
| UniVideo | 模型 | 84 | 81 | 84 次引用（7.8 次/月）、81 upvote；MLLM 读指令 + MMDiT 出视频的双流设计，把理解、生成、编辑放进一次联合训练，是「视频侧统一模型」目前最完整的一篇 |
| IVEBench | 基准 | 26 | 5 | 全库唯一一条视频编辑评测口径；600 段源视频 / 8 类编辑任务 / 三维度指标，补上「编辑好不好没法量」这个空缺 |
| Ditto | 数据集 | 71 | 52 | 71 次引用（6.8 次/月）、52 upvote；图像编辑器 + in-context 视频生成器融合造数据，再用 agent 筛指令，是当前规模最大的合成编辑数据管线 |
| Cosmos-Predict 2.5 | 技术报告 | 170 | 47 | 170 次引用（16.9 次/月）、47 upvote；Cosmos 的下一代，Text2World / Image2World / Video2World 合一并接入 Cosmos-Reason1 做文本 grounding，2 亿视频片段训练 + RL 后训练 |
| HunyuanVideo 1.5 | 技术报告 | 107 | 29 | 8.3B 跑消费级显卡，SSTA 稀疏注意力；把开源视频生成拉回个人可负担区间 |
| Kling-Omni | 技术报告 | 50 | 173 | 173 upvote 是 2025 年底最高热度；生成/编辑/推理统一进一个框架，音画原生同步 |
| Helios | 模型 | 42 | 190 | 190 upvote；14B 在单张 H100 上跑 19.5 FPS 且支持分钟级，且明确不用 self-forcing / KV-cache / 稀疏注意力等既有加速手段，是 2026 年实时长视频的另一条解法 |
| Matrix-Game 3.0 | 方法 | 52 | 51 | 实时流式可交互 + 长程记忆，开源阵营对标 Genie 3 的最近位置 |
| Seedance 2.0 | 技术报告 | 101 | 170 | 4 个月 101 次引用（25 次/月，新论文里最快）；Artificial Analysis 视频竞技场第一，全模态条件输入 |
| LiveEdit | 方法 | 8 | 82 | 82 upvote；三段式蒸馏把双向编辑模型压成单向流式编辑器，是「流式生成」的方法迁到「流式编辑」的第一批工作 |
| VidGen-VL | 方法 | 5 | 88 | 上线一个月 88 upvote；把 chain-of-frames 那条线推到「视频生成模型即通用视觉学习器」 |
| MiniMax H3 | 技术报告 | — | — | 33B 稠密单流 omni transformer，H3-VAE 把有效序列长度拉到 4 倍以支撑原生 2K；8-03 开源权重后成为首个登顶 Artificial Analysis 全球视频榜的开源模型，压过全部闭源 |
| JoyAI-Video-Edit | 模型 | 1 | 104 | 104 upvote 是 2026-08 视频编辑最高热度；16B 自回归扩散，两步生成 + 源锚定 DMD，720p 实时开放式编辑，京东开源 |

## 仓库长什么样

```
video-gen-edit-papers/
├── README.md              ← 本文件。收什么 + 怎么用 + 全量清单
├── LICENSE                ← CC BY 4.0
├── docs/
│   ├── prompt.md          ← 生成解读用的 prompt（原样作为 system prompt）
│   ├── INDEX.md           ← 按技术脉络与任务分组的索引
│   ├── 清单扩充_2026-09.md ← 20 → 50 篇那一轮的选法、双轴快照与备选池
│   └── 许可清单.md         ← 逐篇原文许可，判断能不能公开转载译文
├── scripts/
│   ├── papers.json        ← 元数据唯一事实来源，README 与 INDEX 由它生成
│   ├── fetch_pdfs.py      ← 拉原文，arXiv 节流 3 秒/份
│   ├── extract_text.py    ← pypdf 抽文字
│   ├── generate_notes.py  ← DeepSeek V4 Pro 生成解读，字数不达标自动重生成
│   ├── verify_venues.py   ← arXiv / DBLP / OpenAlex 交叉核发表信息
│   ├── build_readme.py    ← 渲染本文件
│   └── build_index.py     ← 渲染 docs/INDEX.md
└── papers/
    └── YYYY-MM_简称/
        ├── meta.json      ← 单篇元数据 + 核验记录
        ├── paper.pdf      ← .gitignore 挡住，不进仓库
        └── 解读.md
```

`translations/` 目录里有 10 份全文翻译，**刻意没有提交**：arXiv 的永久非独占许可
没有把演绎权授给第三方，公开发布译文需要作者授权。逐篇许可见 docs/许可清单.md。

## 已知没核到的

| 项 | 状态 |
| --- | --- |
| 机构 | 50 篇全部核过。机构只认 PDF 首页作者块——**没用 OpenAlex 补**，它对 arXiv 预印本几乎没有机构字段，且已知会误配（把 HunyuanVideo 配给 "Applied GeoSolutions"）。 |
| 发表信息只有会议名、没有年份的 5 篇 | TokenFlow、VideoReward、Sparse VideoGen、Señorita-2M、VideoPainter。Semantic Scholar 的 `year` 字段是论文年份不是会议年份，拼上去就是造一个假事实；DBLP 在产出这批时连不上。宁可只写会议名 |
| Genie 的 ICML 2024 Best Paper | 会议名经 Semantic Scholar 确认，**最佳论文这一项未核**，表中只写 ICML 2024 |
| Sora 报告与 MiniMax H3 的引用量 | 均非 arXiv 条目，Semantic Scholar 与 HF 都无记录，不编数字 |
| MiniMax H3 的完整技术报告 | 官方页写明「完整报告即将发布」，当前只有博客级描述 |
| Sora 解读的事实来源 | 不是 PDF。这份报告只发在 OpenAI 官网，且 openai.com 拒绝脚本请求（HTTP 403），正文取自 Internet Archive 2026-08-27 的官方页快照。快照 URL 与抽取文本的 sha256 记在 `papers/2024-02_Sora/meta.json` |
| 解读正文 | 机器生成，未逐句人工复核。数字与结论以原文为准 |
| 视频编辑覆盖度 | 2026-09-02 扩到 50 篇时补上，编辑侧从 2 篇到 20 篇。**但 2024 年是空的**——InsV2V（2023-11）之后直到 Señorita-2M（2025-02），中间 15 个月没有编辑论文入选。唯一够格的补位是 AnyV2V（2024-03），本轮按 50 篇名额没放进来 |
| 原文许可 | 逐篇读 arXiv abs 页的许可声明，见 [docs/许可清单.md](docs/许可清单.md)。受限的是「公开再分发翻译」，不是翻译本身 |
| 无论文的重要产品 | Veo 3.1、Kling 3.0、Genie 3 / Project Genie、Runway Gen-4、LTX-2.5、FLUX 3 Video 均无独立论文，按「只收 Paper / 技术报告」的口径不进表 |

arXiv ID、标题、首次公开日期已全部经 arXiv API 逐条核对，与官方元数据一致。
发表会议经 Semantic Scholar 与 arXiv comment 字段双源确认。
