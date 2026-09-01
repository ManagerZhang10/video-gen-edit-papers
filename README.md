# 视频生成与编辑论文库 2023–2026

[![papers](https://img.shields.io/badge/papers-20-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-69K_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-2023.11_--_2026.07-e07b39)](#全量清单)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**20 篇视频生成与编辑领域最有影响力的论文，每篇一份中文解读，外加一条核验过的原文直链。**
时间跨度 2023-11 → 2026-07，解读合计 69,939 个汉字。

*20 most influential video generation & editing papers, each with a Chinese reading note and a verified link to the source. Nov 2023 – Jul 2026.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE) · **最后核对** 2026-09-01
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
| 生成 | 20 |
| 编辑 | 2 |

⚠️ **当前这一期以生成为主，编辑只有 2 篇**（VACE、Kling-Omni，都是生成/编辑
统一的工作）。专门做视频编辑的论文是下一期的补充方向，现在不假装已经覆盖。
图像侧的生成与编辑在另一个库：[image-gen-edit-papers](https://github.com/ManagerYu10/image-gen-edit-papers)。

## 怎么用

拉到[全量清单](#全量清单)，20 行按时间排。每行两列可以点：**简称**去解读，**原文**去 arXiv 或官方页。
按技术脉络分组的视图在 [docs/INDEX.md](docs/INDEX.md)。

原文 PDF 不在仓库里（被 `.gitignore` 挡住）。批量拉到本地：

```bash
python3 scripts/fetch_pdfs.py          # 补齐所有缺的
python3 scripts/fetch_pdfs.py --list   # 只列缺什么
```

生成解读的 prompt 是 [docs/prompt.md](docs/prompt.md)，跟仓库一起提交，别人可以复现。
想公开转载全文翻译先看 [docs/许可清单.md](docs/许可清单.md)——20 篇里只有 4 篇的许可允许公开发布译文。

## 怎么选的

**影响力 = 已兑现的引用量 + 尚未兑现的业界关注度。** 两个轴分开列、不合成单一分数，
因为它们经常打架：HunyuanVideo 有 1,614 次引用但只有 12 个 upvote；CausVid 只有 3 个 upvote，
却是整个 Forcing 家族的根。

| 轴 | 数据源 | 核对日期 |
| --- | --- | --- |
| 引用量 | Semantic Scholar Graph API | 2026-08-31 |
| 业界关注度（upvote） | Hugging Face Papers API | 2026-08-31 |

2023–2024 只留仍在支撑 2026 工作的那几篇。AnimateDiff（1,672 次引用）、MAGVIT-v2（687）、
Movie Gen（629）、VideoPoet（546）、Lumiere（544）、W.A.L.T（351）、GameNGen（280）
引用量都不低，但技术路线已被取代，不占名额。

新工作按引用速率和 upvote 计入，不按绝对引用量——Seedance 2.0 上线 4 个月 101 次引用
（25 次/月），比多数 2024 年论文的当期速率还快。两项没有 arXiv 条目的官方技术报告
（Sora、MiniMax H3）没有可比数据，按技术影响单独判断。

## 技术脉络

| 脉络 | 篇数 | 篇目 |
| --- | ---: | --- |
| 基座架构 | 8 | SVD、Sora、CogVideoX、HunyuanVideo、Wan、Seedance 1.0、HunyuanVideo 1.5、Seedance 2.0 |
| 世界模型与交互环境 | 3 | Genie、Cosmos、Matrix-Game 3.0 |
| 少步与因果蒸馏 | 2 | CausVid、Self Forcing |
| 视频模型即通用视觉基座 | 2 | Chain-of-Frames、VidGen-VL |
| 统一多模态 | 2 | Kling-Omni、MiniMax H3 |
| 评测 | 1 | VBench |
| 视频编辑与统一创作 | 1 | VACE |
| RL 与对齐 | 1 | DanceGRPO |

逐篇归入哪条脉络、每条脉络怎么串起来，见 [docs/INDEX.md](docs/INDEX.md)。

## 全量清单

| # | 时间 | 简称（→ 解读） | 论文标题 | 发表 | 机构 | 任务 | 原文 | 解读字数 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| 1 | 2023-11-25 | [SVD](papers/2023-11_SVD/解读.md) | Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets | arXiv 预印本 | Stability AI | 生成 | [arXiv](https://arxiv.org/abs/2311.15127) | 3,325 |
| 2 | 2023-11-29 | [VBench](papers/2023-11_VBench/解读.md) | VBench: Comprehensive Benchmark Suite for Video Generative Models | CVPR 2024 | 南洋理工大学 S-Lab / 上海人工智能实验室（未核） | 生成 | [arXiv](https://arxiv.org/abs/2311.17982) | 3,790 |
| 3 | 2024-02-15 | [Sora](papers/2024-02_Sora/解读.md) | Video generation models as world simulators | OpenAI 技术报告（无同行评审） | OpenAI | 生成 | [官方页](https://openai.com/index/video-generation-models-as-world-simulators/) | 4,072 |
| 4 | 2024-02-23 | [Genie](papers/2024-02_Genie/解读.md) | Genie: Generative Interactive Environments | ICML 2024 | Google DeepMind | 生成 | [arXiv](https://arxiv.org/abs/2402.15391) | 3,522 |
| 5 | 2024-08-12 | [CogVideoX](papers/2024-08_CogVideoX/解读.md) | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | ICLR 2025 | 智谱 AI / 清华大学（未核） | 生成 | [arXiv](https://arxiv.org/abs/2408.06072) | 4,048 |
| 6 | 2024-12-03 | [HunyuanVideo](papers/2024-12_HunyuanVideo/解读.md) | HunyuanVideo: A Systematic Framework For Large Video Generative Models | arXiv 预印本 | 腾讯混元 | 生成 | [arXiv](https://arxiv.org/abs/2412.03603) | 3,576 |
| 7 | 2024-12-10 | [CausVid](papers/2024-12_CausVid/解读.md) | From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | CVPR 2025 | MIT / Adobe Research（未核） | 生成 | [arXiv](https://arxiv.org/abs/2412.07772) | 3,893 |
| 8 | 2025-01-07 | [Cosmos](papers/2025-01_Cosmos/解读.md) | Cosmos World Foundation Model Platform for Physical AI | arXiv 预印本 | NVIDIA | 生成 | [arXiv](https://arxiv.org/abs/2501.03575) | 3,379 |
| 9 | 2025-03-10 | [VACE](papers/2025-03_VACE/解读.md) | VACE: All-in-One Video Creation and Editing | ICCV 2025 | 阿里巴巴通义实验室 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2503.07598) | 3,042 |
| 10 | 2025-03-26 | [Wan](papers/2025-03_Wan/解读.md) | Wan: Open and Advanced Large-Scale Video Generative Models | arXiv 预印本 | 阿里巴巴通义实验室 | 生成 | [arXiv](https://arxiv.org/abs/2503.20314) | 3,259 |
| 11 | 2025-05-12 | [DanceGRPO](papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | arXiv 预印本 | 字节跳动 / 香港大学（未核） | 生成 | [arXiv](https://arxiv.org/abs/2505.07818) | 3,697 |
| 12 | 2025-06-09 | [Self Forcing](papers/2025-06_Self-Forcing/解读.md) | Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion | NeurIPS 2025 (Spotlight) | Adobe Research / 德州大学奥斯汀分校（未核） | 生成 | [arXiv](https://arxiv.org/abs/2506.08009) | 3,493 |
| 13 | 2025-06-10 | [Seedance 1.0](papers/2025-06_Seedance-1.0/解读.md) | Seedance 1.0: Exploring the Boundaries of Video Generation Models | 字节跳动 Seed 技术报告 | 字节跳动 Seed | 生成 | [arXiv](https://arxiv.org/abs/2506.09113) | 3,861 |
| 14 | 2025-09-24 | [Chain-of-Frames](papers/2025-09_Chain-of-Frames/解读.md) | Video models are zero-shot learners and reasoners | arXiv 预印本 | Google DeepMind | 生成 | [arXiv](https://arxiv.org/abs/2509.20328) | 3,243 |
| 15 | 2025-11-24 | [HunyuanVideo 1.5](papers/2025-11_HunyuanVideo-1.5/解读.md) | HunyuanVideo 1.5 Technical Report | 腾讯混元技术报告 | 腾讯混元 | 生成 | [arXiv](https://arxiv.org/abs/2511.18870) | 3,204 |
| 16 | 2025-12-18 | [Kling-Omni](papers/2025-12_Kling-Omni/解读.md) | Kling-Omni Technical Report | 快手可灵技术报告 | 快手可灵 | 生成+编辑 | [arXiv](https://arxiv.org/abs/2512.16776) | 3,105 |
| 17 | 2026-04-10 | [Matrix-Game 3.0](papers/2026-04_Matrix-Game-3.0/解读.md) | Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory | arXiv 预印本 | 昆仑万维 Skywork（未核） | 生成 | [arXiv](https://arxiv.org/abs/2604.08995) | 4,183 |
| 18 | 2026-04-15 | [Seedance 2.0](papers/2026-04_Seedance-2.0/解读.md) | Seedance 2.0: Advancing Video Generation for World Complexity | 字节跳动 Seed Model Card | 字节跳动 Seed | 生成 | [arXiv](https://arxiv.org/abs/2604.14148) | 3,070 |
| 19 | 2026-07-10 | [VidGen-VL](papers/2026-07_VidGen-VL/解读.md) | Video Generation Models are General-Purpose Vision Learners | ECCV 2026 | 未核 | 生成 | [arXiv](https://arxiv.org/abs/2607.09024) | 3,153 |
| 20 | 2026-07-31 | [MiniMax H3](papers/2026-07_MiniMax-H3/解读.md) | MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities | MiniMax 官方技术报告（完整版未发布） | MiniMax | 生成 | [官方页](https://www.minimax.io/blog/minimax-h3) | 3,024 |

## 凭什么进这 20 个

引用量与 upvote 是选文判据，不进主表。核对日期 2026-08-31。

| 简称 | 类型 | 引用 | upvote | 理由 |
| --- | --- | ---: | ---: | --- |
| SVD | 方法 | 2,856 | 15 | 至今引用量最高的视频生成论文；数据策展流程被后续几乎所有工作沿用 |
| VBench | 基准 | 1,842 | 9 | 2026 年的论文仍默认报 VBench 分数，是唯一活下来的评测口径 |
| Sora | 技术报告 | — | — | 确立 DiT + 时空 patch + 规模化的范式，此后所有基座模型都在这条线上 |
| Genie | 方法 | 773 | 72 | world model 这条线的源头，直通 Genie 3 与 2026-01 上线的 Project Genie |
| CogVideoX | 模型 | 2,309 | 37 | 第一个真正可用的开源 DiT 视频模型，3D VAE + expert transformer 成为开源默认结构 |
| HunyuanVideo | 技术报告 | 1,614 | 12 | 13B 开源权重，把开源与闭源的差距第一次压到可比 |
| CausVid | 方法 | 387 | 3 | 引用量不高但是整个 Forcing 家族的根：双向教师蒸馏成因果学生，实时视频生成从这里开始 |
| Cosmos | 技术报告 | 817 | 84 | 把视频生成明确定位成机器人与自动驾驶的数据引擎，开辟 physical AI 应用面 |
| VACE | 方法 | 472 | 58 | 生成与编辑统一进一个模型，是 ComfyUI 生态里被实际接得最多的可控方案 |
| Wan | 技术报告 | 2,414 | 71 | 17 个月 2414 次引用（142 次/月，全表最高）；2026 年绝大多数开源二次开发的底座 |
| DanceGRPO | 奖励与 RL | 352 | 34 | 把 GRPO 搬到视觉生成，RL 后训练从此成为视频基座的标配环节 |
| Self Forcing | 方法 | 519 | 32 | 用学生自 rollout 消掉训练-推理落差，单卡亚秒延迟；衍生出 Rolling / Causal / Sparse / Light Forcing 一整族 |
| Seedance 1.0 | 技术报告 | 242 | 109 | 闭源阵营里少见地把训练与推理加速细节写清楚的报告，1080p/5s 仅 41.4 秒 |
| Chain-of-Frames | 方法 | 203 | 101 | 用 Veo 3 在 62 个未训练任务上验证零样本能力，提出 chain-of-frames；把视频模型重新定义为通用视觉基座 |
| HunyuanVideo 1.5 | 技术报告 | 107 | 29 | 8.3B 跑消费级显卡，SSTA 稀疏注意力；把开源视频生成拉回个人可负担区间 |
| Kling-Omni | 技术报告 | 50 | 173 | 173 upvote 是 2025 年底最高热度；生成/编辑/推理统一进一个框架，音画原生同步 |
| Matrix-Game 3.0 | 方法 | 52 | 51 | 实时流式可交互 + 长程记忆，开源阵营对标 Genie 3 的最近位置 |
| Seedance 2.0 | 技术报告 | 101 | 170 | 4 个月 101 次引用（25 次/月，新论文里最快）；Artificial Analysis 视频竞技场第一，全模态条件输入 |
| VidGen-VL | 方法 | 5 | 88 | 上线一个月 88 upvote；把 chain-of-frames 那条线推到「视频生成模型即通用视觉学习器」 |
| MiniMax H3 | 技术报告 | — | — | 33B 稠密单流 omni transformer，H3-VAE 把有效序列长度拉到 4 倍以支撑原生 2K；8-03 开源权重后成为首个登顶 Artificial Analysis 全球视频榜的开源模型，压过全部闭源 |

## 仓库长什么样

```
video-gen-edit-papers/
├── README.md              ← 本文件。收什么 + 怎么用 + 全量清单
├── LICENSE                ← CC BY 4.0
├── docs/
│   ├── prompt.md          ← 生成解读用的 prompt（原样作为 system prompt）
│   ├── INDEX.md           ← 按技术脉络与任务分组的索引
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
没有把演绎权授给第三方，公开发布译文需要作者授权。判断口径见 docs/许可清单.md。

## 已知没核到的

| 项 | 状态 |
| --- | --- |
| 标 **（未核）** 的机构 | OpenAlex 对 arXiv 预印本没有机构字段，且会误配（把 HunyuanVideo 配给 "Applied GeoSolutions"）。可靠来源只有 PDF 首页作者块 |
| Genie 的 ICML 2024 Best Paper | 会议名经 Semantic Scholar 确认，**最佳论文这一项未核**，表中只写 ICML 2024 |
| Sora 报告与 MiniMax H3 的引用量 | 均非 arXiv 条目，Semantic Scholar 与 HF 都无记录，不编数字 |
| MiniMax H3 的完整技术报告 | 官方页写明「完整报告即将发布」，当前只有博客级描述 |
| Sora 解读的事实来源 | 不是 PDF。这份报告只发在 OpenAI 官网，且 openai.com 拒绝脚本请求（HTTP 403），正文取自 Internet Archive 2026-08-27 的官方页快照。快照 URL 与抽取文本的 sha256 记在 `papers/2024-02_Sora/meta.json` |
| 解读正文 | 机器生成，未逐句人工复核。数字与结论以原文为准 |
| 视频编辑覆盖度 | 本期只有 2 篇涉及编辑，且都是生成/编辑统一的工作。专门的视频编辑论文尚未收 |
| 无论文的重要产品 | Veo 3.1、Kling 3.0、Genie 3 / Project Genie、Runway Gen-4、LTX-2.5、FLUX 3 Video 均无独立论文，按「只收 Paper / 技术报告」的口径不进表 |

arXiv ID、标题、首次公开日期已全部经 arXiv API 逐条核对，与官方元数据一致。
发表会议经 Semantic Scholar 与 arXiv comment 字段双源确认。
