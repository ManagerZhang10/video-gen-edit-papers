#!/usr/bin/env python3
"""由 20 份解读的第 1 节（定位）与第 8 节（工程判断与收束）合成 docs/总结分析.md。

素材只用解读里的这两节——不回读全文，避免把几十万字灌进上下文。
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_notes import deepseek, cjk, folder, ROOT

SYS = """你在为一个 20 篇的视频生成论文库写「跨论文综述」。素材是每篇解读里的两节：
定位（这篇解决什么）和工程判断与收束（可行性/风险/上限/必须记住的事）。

硬规则：
- 事实只能来自给你的素材。素材没写的，不要补充、不要脑补。
- 不写引用量、榜单名次、社区评价、后续产品——素材里没有这些。
- 不确定就不写，不要用「据了解」「普遍认为」这类模糊措辞。
- 禁止营销词：碾压、吊打、开山之作、革命性、里程碑、颠覆、彻底解决。
- 中文写作，技术术语保留英文原词（DiT、VAE、flow matching、distillation、MoE 等）。
- 能用表格表达对照关系就用表格，不要写成大段散文。
- 不要写「总结」「展望」「结语」这类凑数章节，不要写元话语。

输出 3000～4500 个中文字符，严格照抄以下五个二级标题，不加别的：

## 1. 三年里真正变了的是什么
两三段。说清 2023 到 2026 之间，这个领域的技术矛盾从哪里移到了哪里。
不要按时间罗列论文，要说矛盾的转移。

## 2. 几条主线各自在解决什么
一个表格，一行一条主线（4~6 行）。列：`主线 | 独有的技术矛盾 | 代表工作 | 现在停在哪`。
「独有的技术矛盾」写别的线不用面对、或者用别的办法绕不过去的那个点。

## 3. 已经稳定下来的做法
5~7 条。写被多篇反复采用、可以当默认选项的做法。每条一行：`- **做法** —— 一句话说清什么时候用`。

## 4. 还没解决的
5~7 条。只写素材里明确提到的局限、失败模式、未解问题。每条一行：`- **问题** —— 一句话说清卡在哪`。

## 5. 要动手的话，从哪几篇入手
一个表格。列：`我要做的事 | 先读哪几篇 | 为什么是这几篇`。4~6 行，覆盖典型意图
（跑通一个开源基座、做实时/交互、做可控编辑、做评测、做世界模型）。
"""


def sec(md, n):
    mo = re.search(rf"^## {n}\. .*?$(.*?)(?=^## \d+\. |\Z)", md, re.S | re.M)
    return mo.group(1).strip() if mo else ""


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    parts = []
    for p in ps:
        f = os.path.join(folder(p), "解读.md")
        if not os.path.exists(f):
            continue
        md = open(f, encoding="utf-8").read()
        parts.append(f"### {p['short']}（{p['date']}，{p['venue']}）\n"
                     f"【定位】{sec(md,1)}\n\n【工程判断与收束】{sec(md,8)}")
    print(f"素材：{len(parts)} 篇", flush=True)
    out = deepseek(SYS, "\n\n---\n\n".join(parts), max_tokens=16000, temp=0.35).strip()
    os.makedirs(f"{ROOT}/docs", exist_ok=True)
    hdr = ("# 总结分析\n\n"
           "> 读者：已经扫过清单，想知道跨论文的结论\n"
           "> 素材：本库 20 篇解读的「定位」与「工程判断」两节\n"
           "> ⚠️ 由 DeepSeek v4 Pro 合成，未逐句人工复核\n"
           "> 最后核对：2026-08-31\n\n---\n\n")
    open(f"{ROOT}/docs/总结分析.md", "w", encoding="utf-8").write(hdr + out + "\n")
    print(f"总结分析.md 已写入：{cjk(out):,} 字")


if __name__ == "__main__":
    main()
