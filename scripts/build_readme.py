#!/usr/bin/env python3
"""由 scripts/papers.json + 实际落盘的解读文件渲染 README.md。README 不手写。

列顺序遵守 ../CLAUDE.md 第二节的规定：# / 时间 / 简称 / 论文标题 / 发表 / 机构 / 原文
七列必须有且相对顺序固定；任务与解读字数作为附加列放在机构之后、原文之前。
引用量与 upvote 不进主表——它们是选文判据，放「凭什么进这 20 个」那一节。
"""
import json, os, re
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKED = "2026-09-02"


def cjk(t):
    return sum(1 for ch in t if "一" <= ch <= "鿿")


def folder(p):
    return p["date"][:7].replace("/", "-") + "_" + p["short"].replace(" ", "-")


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ps.sort(key=lambda p: p["date"])
    span_lo, span_hi = ps[0]["date"][:7], ps[-1]["date"][:7]      # YYYY/MM
    yr_lo, yr_hi = span_lo[:4], span_hi[:4]

    rows, whys, total, have = [], [], 0, 0
    for i, p in enumerate(ps, 1):
        d = folder(p)
        note = f"{ROOT}/papers/{d}/解读.md"
        if os.path.exists(note):
            n = cjk(open(note, encoding="utf-8").read())
            total += n; have += 1
            name, chars = f"[{p['short']}](papers/{d}/解读.md)", f"{n:,}"
        else:
            name, chars = p["short"], "—"
        link = f"[arXiv]({p['url']})" if p["arxiv_id"] else f"[官方页]({p['url']})"
        c = "—" if p["cites"] is None else f"{p['cites']:,}"
        u = "—" if p["upvotes"] is None else str(p["upvotes"])
        rows.append(f"| {i} | {p['date'].replace('/','-')} | {name} | {p['title']} | "
                    f"{p['venue']} | {p['org']} | {'+'.join(p['task'])} | {link} | {chars} |")
        whys.append(f"| {p['short']} | {p['type']} | {c} | {u} | {p['why']} |")

    tasks = Counter(t for p in ps for t in p["task"])
    both = [p["short"] for p in ps if set(p["task"]) == {"生成", "编辑"}]
    lines = OrderedDict()
    for p in ps:
        lines.setdefault(p["line"], []).append(p["short"])
    line_rows = [f"| {k} | {len(v)} | {'、'.join(v)} |"
                 for k, v in sorted(lines.items(), key=lambda kv: -len(kv[1]))]

    # 「已知没核到的」几行按数据算，不写死篇数
    # 「未核」既可能是 org 为空，也可能是机构串里带着（未核）标记，两种都要算
    org_unknown = [p["short"] for p in ps
                   if not p.get("org") or "未核" in p["org"]]
    ORG_METHOD = ('机构只认 PDF 首页作者块——**没用 OpenAlex 补**，它对 arXiv 预印本几乎没有'
                  '机构字段，且已知会误配（把 HunyuanVideo 配给 "Applied GeoSolutions"）。')
    org_line = (f"{len(ps)} 篇全部核过。" + ORG_METHOD if not org_unknown
                else f"**{len(org_unknown)} 篇未核**：{'、'.join(org_unknown)}。" + ORG_METHOD)
    NO_YEAR_OK = ("预印本", "技术报告", "Model Card", "官方")      # 这些本来就没有会议年份
    venue_no_year = [p["short"] for p in ps
                     if p["venue"] and not re.search(r"\d{4}", p["venue"])
                     and not any(k in p["venue"] for k in NO_YEAR_OK)]

    head = f"""# 视频生成与编辑论文库 {yr_lo}–{yr_hi}

[![papers](https://img.shields.io/badge/papers-{len(ps)}-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-{total//1000}K_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-{span_lo.replace("/", ".")}_--_{span_hi.replace("/", ".")}-e07b39)](#全量清单)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**{len(ps)} 篇视频生成与编辑领域最有影响力的论文，每篇一份中文解读，外加一条核验过的原文直链。**
时间跨度 {span_lo.replace("/", "-")} → {span_hi.replace("/", "-")}，解读合计 {total:,} 个汉字。

*{len(ps)} most influential video generation & editing papers, each with a Chinese reading note and a verified link to the source. {span_lo.replace("/", "-")} – {span_hi.replace("/", "-")}.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE) · **最后核对** {CHECKED}
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
| 生成 | {tasks['生成']} |
| 编辑 | {tasks['编辑']} |

其中 {len(both)} 篇同时是两者（生成/编辑统一的模型）：{'、'.join(both)}。

图像侧的生成与编辑在另一个库：[image-gen-edit-papers](https://github.com/ManagerYu10/image-gen-edit-papers)。

## 怎么用

拉到[全量清单](#全量清单)，{len(ps)} 行按时间排。每行两列可以点：**简称**去解读，**原文**去 arXiv 或官方页。
按技术脉络分组的视图在 [docs/INDEX.md](docs/INDEX.md)。

原文 PDF 不在仓库里（被 `.gitignore` 挡住）。批量拉到本地：

```bash
python3 scripts/fetch_pdfs.py          # 补齐所有缺的
python3 scripts/fetch_pdfs.py --list   # 只列缺什么
```

生成解读的 prompt 是 [docs/prompt.md](docs/prompt.md)，跟仓库一起提交，别人可以复现。
想公开转载全文翻译先看 [docs/许可清单.md](docs/许可清单.md)——{len(ps)} 篇里只有 4 篇的许可允许公开发布译文。

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
{chr(10).join(line_rows)}

逐篇归入哪条脉络、每条脉络怎么串起来，见 [docs/INDEX.md](docs/INDEX.md)。

## 全量清单

| # | 时间 | 简称（→ 解读） | 论文标题 | 发表 | 机构 | 任务 | 原文 | 解读字数 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
"""
    mid = f"""

## 凭什么进这 {len(ps)} 个

引用量与 upvote 是选文判据，不进主表。核对日期 2026-08-31。

| 简称 | 类型 | 引用 | upvote | 理由 |
| --- | --- | ---: | ---: | --- |
"""
    tail = f"""

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
| 机构 | {org_line} |
| 发表信息只有会议名、没有年份的 {len(venue_no_year)} 篇 | {'、'.join(venue_no_year) if venue_no_year else '无'}。Semantic Scholar 的 `year` 字段是论文年份不是会议年份，拼上去就是造一个假事实；DBLP 在产出这批时连不上。宁可只写会议名 |
| Genie 的 ICML 2024 Best Paper | 会议名经 Semantic Scholar 确认，**最佳论文这一项未核**，表中只写 ICML 2024 |
| Sora 报告与 MiniMax H3 的引用量 | 均非 arXiv 条目，Semantic Scholar 与 HF 都无记录，不编数字 |
| MiniMax H3 的完整技术报告 | 官方页写明「完整报告即将发布」，当前只有博客级描述 |
| Sora 解读的事实来源 | 不是 PDF。这份报告只发在 OpenAI 官网，且 openai.com 拒绝脚本请求（HTTP 403），正文取自 Internet Archive 2026-08-27 的官方页快照。快照 URL 与抽取文本的 sha256 记在 `papers/2024-02_Sora/meta.json` |
| 解读正文 | 机器生成，未逐句人工复核。数字与结论以原文为准 |
| 视频编辑覆盖度 | 2026-09-02 扩到 50 篇时补上，编辑侧从 2 篇到 {tasks['编辑']} 篇。**但 2024 年是空的**——InsV2V（2023-11）之后直到 Señorita-2M（2025-02），中间 15 个月没有编辑论文入选。唯一够格的补位是 AnyV2V（2024-03），本轮按 50 篇名额没放进来 |
| 原文许可 | 逐篇读 arXiv abs 页的许可声明，见 [docs/许可清单.md](docs/许可清单.md)。受限的是「公开再分发翻译」，不是翻译本身 |
| 无论文的重要产品 | Veo 3.1、Kling 3.0、Genie 3 / Project Genie、Runway Gen-4、LTX-2.5、FLUX 3 Video 均无独立论文，按「只收 Paper / 技术报告」的口径不进表 |

arXiv ID、标题、首次公开日期已全部经 arXiv API 逐条核对，与官方元数据一致。
发表会议经 Semantic Scholar 与 arXiv comment 字段双源确认。
"""
    open(f"{ROOT}/README.md", "w", encoding="utf-8").write(
        head + "\n".join(rows) + mid + "\n".join(whys) + tail)
    print(f"README 已渲染：{have}/{len(ps)} 篇有解读，合计 {total:,} 字，"
          f"{len(lines)} 条脉络，任务分布 {dict(tasks)}")


if __name__ == "__main__":
    main()
