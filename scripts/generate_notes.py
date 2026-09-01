#!/usr/bin/env python3
"""用 DeepSeek V4 Pro 依据 PDF 抽取的文字生成每篇的解读.md。

规范见 ../CLAUDE.md：3000~5000 个中文字符，固定 8 节。不达标自动重生成，
最多 3 次，attempts 记进 meta.json。凭证从 BaseModel/.env 运行时读，不落盘。
"""
import json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANDIDATES = [
    os.environ.get("LLM_ENV_FILE"),
    os.path.expanduser("~/ZhangYu/self_learning/BaseModel/.env"),
    os.path.expanduser("~/ZhangYu/BaseModel/.env"),
]
ENV = next((c for c in CANDIDATES if c and os.path.exists(c)), None)
if ENV is None:
    sys.exit("找不到 BaseModel/.env，用 LLM_ENV_FILE 指定路径")
LO, HI = 3000, 5000

cfg = {}
for line in open(ENV, encoding="utf-8"):
    line = line.strip()
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        cfg[k.strip()] = v.strip().strip('"').strip("'")
KEY, BASE, MODEL = cfg["DEEPSEEK_API_KEY"], cfg["DEEPSEEK_BASE_URL"], cfg["DEEPSEEK_V4_PRO_MODEL"]
SYS = open(f"{ROOT}/docs/prompt.md", encoding="utf-8").read()


def cjk(t):
    return sum(1 for ch in t if "一" <= ch <= "鿿")


def deepseek(sysmsg, usermsg, max_tokens=16000, temp=0.3):
    body = json.dumps({"model": MODEL, "temperature": temp, "max_tokens": max_tokens,
                       "messages": [{"role": "system", "content": sysmsg},
                                    {"role": "user", "content": usermsg}]}).encode()
    req = urllib.request.Request(BASE.rstrip("/") + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + KEY})
    last = None
    for att in range(4):
        try:
            with urllib.request.urlopen(req, timeout=1800) as r:
                d = json.loads(r.read())
            # v4-pro 是 reasoning 模型，正文只取 content，reasoning_content 丢掉
            return d["choices"][0]["message"]["content"] or ""
        except Exception as e:
            last = e
            time.sleep(10 * (att + 1))
    raise last


def folder(p):
    return os.path.join(ROOT, "papers", p["date"][:7].replace("/", "-") + "_" + p["short"].replace(" ", "-"))


def one(p):
    short = p["short"]
    d = folder(p)
    os.makedirs(d, exist_ok=True)
    out = os.path.join(d, "解读.md")
    if os.path.exists(out) and LO <= cjk(open(out, encoding="utf-8").read()) <= HI:
        return short, cjk(open(out, encoding="utf-8").read()), 0, "skip"
    src = f"{ROOT}/_work/txt_{short.replace(' ', '-')}.txt"
    if not os.path.exists(src):
        return short, 0, 0, "无原文文字"
    text = open(src, encoding="utf-8").read()
    header = (f"论文简称：{short}\n标题：{p['title']}\n首次公开：{p['date']}\n"
              f"发表：{p['venue']}\n\n以下是该论文原文抽取的文字：\n\n")
    note, n, attempts = "", 0, 0
    extra = ""
    for attempts in range(1, 4):
        note = deepseek(SYS + extra, header + text).strip()
        note = re.sub(r"\n*<!--\s*COMPLETE\s*-->\s*$", "", note).strip()
        n = cjk(note)
        if LO <= n <= HI:
            break
        extra = (f"\n\n【重要】上一次生成是 {n} 个中文字符，"
                 f"{'超出上限，请压缩' if n > HI else '不足下限，请扩写'}到 {LO}~{HI} 之间。"
                 f"不要增删章节，只调整各节篇幅。")
    open(out, "w", encoding="utf-8").write(note + "\n")
    meta = {k: p[k] for k in ("short", "date", "arxiv_id", "title", "url", "venue", "org")}
    meta.update({"cn_chars": n, "attempts": attempts,
                 "note": "DeepSeek V4 Pro 依据 PDF 抽取文字生成，未逐句人工复核",
                 "impact": {"citation_count": p.get("cites"), "hf_upvotes": p.get("upvotes"),
                            "citation_provider": "Semantic Scholar Graph API",
                            "checked_at": "2026-08-31"}})
    json.dump(meta, open(os.path.join(d, "meta.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return short, n, attempts, "ok" if LO <= n <= HI else "字数未达标"


def main():
    papers = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    if only:
        papers = [p for p in papers if any(o in p["short"] for o in only)]
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = {ex.submit(one, p): p["short"] for p in papers}
        for f in as_completed(futs):
            try:
                s, n, a, st = f.result()
                print(f"[{st:12s}] {s:18s} {n:>5} 字  {a} 次", flush=True)
            except Exception as e:
                print(f"[ERROR       ] {futs[f]:18s} {e}", flush=True)


if __name__ == "__main__":
    main()
