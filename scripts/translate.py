#!/usr/bin/env python3
"""把 _work/txt_*.txt 的论文全文分块译成中文，落到 translations/<简称>_全文翻译.md。

分块在段落边界切，块内顺序翻译保证行文连贯。术语保留英文原词。

⚠️ 许可：本库 20 篇里只有 4 篇是 CC BY 4.0，可公开再分发全文翻译；其余为
arXiv 永久非独占许可 / CC BY-NC-ND / 官方网页，翻译仅供本地阅读。
translations/ 默认写进 .gitignore，不进仓库。见 docs/许可清单.md。
"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_notes import deepseek, cjk, ROOT

CHUNK = 7000

SYS = """你是把机器学习论文译成中文的译者。逐段翻译，不要摘要、不要省略、不要评论。

规则：
- 简体中文。技术术语保留英文原词，首次出现给中文解释，如「扩散变换器（diffusion transformer, DiT）」。
- 保留原文的章节结构与编号。数学公式原样保留 LaTeX 或原符号，不要翻译符号本身。
- 表格译成 Markdown 表格。图注译出并标明是图注。
- 参考文献列表（References/Bibliography）整段跳过，不要译，也不要保留。
- PDF 抽取会产生断行、页眉页脚、行号残留，遇到就还原成通顺句子并丢掉噪声。
- 不要输出「以下是翻译」这类客套话，不要输出思考过程。直接给译文。
- 这是一段长文档的一部分，前后还有内容。不要写开场白或结语，接着译就行。"""


def chunks(t, n=CHUNK):
    paras, cur, out = t.split("\n"), [], []
    size = 0
    for p in paras:
        if size + len(p) > n and cur:
            out.append("\n".join(cur)); cur, size = [], 0
        cur.append(p); size += len(p) + 1
    if cur:
        out.append("\n".join(cur))
    return out


def one(p):
    short = p["short"]
    src = f"{ROOT}/_work/txt_{short.replace(' ', '-')}.txt"
    out = f"{ROOT}/translations/{short.replace(' ', '-')}_全文翻译.md"
    if not os.path.exists(src):
        return short, 0, "无原文文字"
    if os.path.exists(out) and cjk(open(out, encoding="utf-8").read()) > 3000:
        return short, cjk(open(out, encoding="utf-8").read()), "skip"
    text = open(src, encoding="utf-8").read()
    cs = chunks(text)
    parts = []
    for i, c in enumerate(cs):
        ctx = f"【这是第 {i+1}/{len(cs)} 块】\n\n"
        parts.append(deepseek(SYS, ctx + c, max_tokens=16000, temp=0.2).strip())
    body = "\n\n".join(parts)
    hdr = (f"# {p['title']}\n\n"
           f"> **{short}** · {p['date']} · {p['venue']} · {p['org']}\n"
           f"> 原文：{p['url']}\n"
           f"> ⚠️ 由 DeepSeek v4 Pro 依据 PDF 抽取文字机器翻译，未人工校对。"
           f"公式符号与图内信息在 PDF 抽取阶段会丢失，**引用前务必回原文核对**。\n"
           f"> 参考文献列表未翻译。\n\n---\n\n")
    os.makedirs(f"{ROOT}/translations", exist_ok=True)
    open(out, "w", encoding="utf-8").write(hdr + body + "\n")
    return short, cjk(body), f"ok（{len(cs)} 块）"


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    if only:
        ps = [p for p in ps if any(o in p["short"] for o in only)]
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(one, p): p["short"] for p in ps}
        for f in as_completed(futs):
            try:
                s, n, st = f.result()
                print(f"[{st:14s}] {s:18s} {n:>7,} 字", flush=True)
            except Exception as e:
                print(f"[ERROR        ] {futs[f]:18s} {e}", flush=True)


if __name__ == "__main__":
    main()
