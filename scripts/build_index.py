#!/usr/bin/env python3
"""渲染 docs/INDEX.md：按技术脉络和任务分组的索引。

README 是一张按时间排的平表（规范要求），分组视图放这里。
每篇的一句话取自 解读.md 第 1 节的首句——那是依据原文写的，不另编。
"""
import json, os, re
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKED = "2026-09-01"

# 脉络的阅读顺序：从底座往外，评测收尾
ORDER = ["基座架构", "少步与因果蒸馏", "统一多模态", "世界模型与交互环境",
         "视频模型即通用视觉基座", "视频编辑与统一创作", "RL 与对齐", "评测"]

BLURB = {
    "基座架构": "文本到视频的主干怎么搭：潜空间压缩、时空 patch、DiT 规模化，以及各家开源/闭源旗舰的取舍。",
    "少步与因果蒸馏": "把双向扩散教师蒸馏成因果学生，换来实时与流式生成。CausVid 是根，Self Forcing 消掉训练-推理落差。",
    "统一多模态": "生成、编辑、理解、音画同步进一个模型，输入输出都不再单一。",
    "世界模型与交互环境": "视频模型当可交互环境用：接受动作输入、保持长程记忆，服务机器人、自动驾驶和游戏。",
    "视频模型即通用视觉基座": "不训练也能做未见过的视觉任务——把视频生成模型当成视觉领域的 GPT-3 时刻来验证。",
    "视频编辑与统一创作": "输入已有视频并改动它。当前只有生成/编辑统一的工作，专门的视频编辑论文尚未收。",
    "RL 与对齐": "生成质量与人类偏好对齐：把 GRPO 一类的策略优化搬到视觉生成上。",
    "评测": "怎么量一个视频模型的好坏。VBench 是这个领域唯一活下来的通用口径。",
}


def cjk(t):
    return sum(1 for ch in t if "一" <= ch <= "鿿")


def folder(p):
    return p["date"][:7].replace("/", "-") + "_" + p["short"].replace(" ", "-")


def one_liner(d):
    """取 解读.md 第 1 节的首句。"""
    p = f"{ROOT}/papers/{d}/解读.md"
    if not os.path.exists(p):
        return "（解读待生成）"
    body = open(p, encoding="utf-8").read()
    m = re.search(r"^## 1\.[^\n]*\n+(.+?)(?=\n\n|\n## )", body, re.S | re.M)
    if not m:
        return "—"
    s = " ".join(m.group(1).split())
    cut = re.split(r"(?<=。)", s)
    out = cut[0] if cut else s
    if len(out) > 190:
        out = out[:188] + "……"
    return out.replace("|", "／")


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ps.sort(key=lambda p: p["date"])
    by_line = OrderedDict((k, []) for k in ORDER)
    for p in ps:
        by_line.setdefault(p["line"], []).append(p)
    missing = [k for k in by_line if k not in ORDER]
    assert not missing, f"ORDER 里没有排到的脉络：{missing}"

    out = [f"""# 视频生成与编辑论文库索引

> 读者：要系统补齐 2023–2026 视频生成技术脉络的人
> 目标：按脉络挑论文，点进任意一篇能直接读完整解读，不用再读原文
> 覆盖：{len(ps)} 项，2023-11 ～ 2026-07
> 最后核对：{CHECKED}

[README](../README.md) 是一张按时间排的平表，用来查。本页按技术脉络分组，用来读。
每篇的「一句话」摘自该篇 `解读.md` 第 1 节首句，依据是论文原文，不是另写的导读。

## 任务分布

一篇论文可以同时是生成和编辑——这就是本库按模态而不按任务划分的原因。

| 任务 | 篇数 | 篇目 |
| --- | ---: | --- |"""]
    for t in ("生成", "编辑"):
        hit = [p["short"] for p in ps if t in p["task"]]
        out.append(f"| {t} | {len(hit)} | {'、'.join(hit)} |")

    out.append(f"\n## {len(by_line)} 条脉络\n")
    for k in ORDER:
        v = by_line[k]
        out.append(f"### {k}（{len(v)} 篇）\n")
        out.append(BLURB[k] + "\n")
        out.append("| 时间 | 简称 | 论文标题 | 类型 | 一句话 |")
        out.append("| --- | --- | --- | --- | --- |")
        for p in v:
            d = folder(p)
            out.append(f"| {p['date'][:7].replace('/','-')} | "
                       f"[{p['short']}](../papers/{d}/解读.md) | {p['title']} | "
                       f"{p['type']} | {one_liner(d)} |")
        out.append("")

    out.append(f"""## 按时间的全量清单

带发表、机构、引用、upvote 的完整版在 [README](../README.md#全量清单)。

| 时间 | 简称 | 脉络 | 任务 | 解读字数 |
| --- | --- | --- | --- | ---: |""")
    for p in ps:
        d = folder(p)
        note = f"{ROOT}/papers/{d}/解读.md"
        n = f"{cjk(open(note, encoding='utf-8').read()):,}" if os.path.exists(note) else "—"
        out.append(f"| {p['date'].replace('/','-')} | [{p['short']}](../papers/{d}/解读.md) | "
                   f"{p['line']} | {'+'.join(p['task'])} | {n} |")

    out.append("""
## 可信度边界

解读正文由 DeepSeek V4 Pro 依据原文抽取的文字生成，人定标准、做机器校验（8 节齐全、
3000～5000 汉字、证据表至少 4 行），**未逐句人工复核**。图里的信息模型读不到，
公式符号会在 PDF 抽取时丢失。数字与结论以原文为准。

Sora 那篇的事实来源不是 PDF：报告只发在 OpenAI 官网，且该站拒绝脚本请求（HTTP 403），
正文取自 Internet Archive 2026-08-27 的官方页快照，快照 URL 与抽取文本的 sha256
记在 `papers/2024-02_Sora/meta.json`。

机构一列标 **（未核）** 的，是 OpenAlex 无机构字段、也没回 PDF 首页逐条核过的。
""")
    open(f"{ROOT}/docs/INDEX.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"docs/INDEX.md 已渲染：{len(by_line)} 条脉络，{len(ps)} 篇")


if __name__ == "__main__":
    main()
