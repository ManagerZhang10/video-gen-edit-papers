#!/usr/bin/env python3
"""按 scripts/papers.json 拉取论文原文，落到 papers/<YYYY-MM_简称>/paper.pdf。

只用标准库。按 arXiv 要求节流到每 3 秒一份，断了重跑只补没下成的。
Sora 没有 PDF，抓官方页面存成 source.html。
"""
import json, os, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = {"User-Agent": "Mozilla/5.0 (compatible; video-gen-papers/1.0; +local research use)"}


def folder(p):
    return os.path.join(ROOT, "papers", p["date"][:7].replace("/", "-") + "_" + p["short"].replace(" ", "-"))


def fetch(url, dest):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def main():
    papers = json.load(open(os.path.join(ROOT, "scripts", "papers.json"), encoding="utf-8"))
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    listing = "--list" in sys.argv
    todo = []
    for p in papers:
        d = folder(p)
        name = "paper.pdf" if p["pdf"] else "source.html"
        dest = os.path.join(d, name)
        if only and not any(o in os.path.basename(d) for o in only):
            continue
        if os.path.exists(dest) and os.path.getsize(dest) > 20000:
            continue
        todo.append((p, d, dest))
    if listing:
        for p, d, _ in todo:
            print(os.path.basename(d))
        print(f"缺 {len(todo)} 份")
        return
    for i, (p, d, dest) in enumerate(todo):
        os.makedirs(d, exist_ok=True)
        url = p["pdf"] or p["url"]
        try:
            n = fetch(url, dest)
            print(f"[OK]   {os.path.basename(d):28s} {n/1e6:6.2f} MB  {url}")
        except Exception as e:
            print(f"[FAIL] {os.path.basename(d):28s} {e}  {url}")
        if i < len(todo) - 1:
            time.sleep(3)


if __name__ == "__main__":
    main()
