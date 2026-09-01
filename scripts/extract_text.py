#!/usr/bin/env python3
"""把 papers/*/paper.pdf 或 source.html 抽成纯文本，落到 _work/txt_<简称>.txt。

PDF 用 pypdf。图里的信息抽不出来，公式符号会在这一步丢失——这是解读的已知边界。
"""
import html.parser, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_CHARS = 150_000   # 超长论文截断，正文足够写 8 节解读


def folder(p):
    return os.path.join(ROOT, "papers", p["date"][:7].replace("/", "-") + "_" + p["short"].replace(" ", "-"))


class Strip(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.buf, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "svg"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "svg") and self.skip:
            self.skip -= 1
        if tag in ("p", "div", "h1", "h2", "h3", "li", "br", "tr"):
            self.buf.append("\n")

    def handle_data(self, d):
        if not self.skip and d.strip():
            self.buf.append(d.strip() + " ")


def from_pdf(path):
    """优先 pymupdf。pypdf 在带字母间距 / 小型大写的排版上会把单词拆碎
    （Wan 的标题被抽成 "WA N: O PEN AND"），pymupdf 不会。"""
    try:
        import fitz
        doc = fitz.open(path)
        out = []
        for pg in doc:
            out.append(pg.get_text())
            if sum(len(x) for x in out) > MAX_CHARS * 2:
                break
        doc.close()
        return "\n".join(out)
    except ImportError:
        from pypdf import PdfReader
        r = PdfReader(path)
        out = []
        for pg in r.pages:
            try:
                out.append(pg.extract_text() or "")
            except Exception:
                out.append("")
            if sum(len(x) for x in out) > MAX_CHARS:
                break
        return "\n".join(out)


def drop_references(t):
    """切掉参考文献。60 页的论文里文献能占掉三分之一预算，喂进去纯属浪费。"""
    pat = re.compile(r"^\s*(References|REFERENCES|Bibliography|BIBLIOGRAPHY)\s*$", re.M)
    hits = list(pat.finditer(t))
    if not hits:
        return t
    # 取最后一个位置靠后的标题，避免误切正文里提到 References 的地方
    for m in reversed(hits):
        if m.start() > len(t) * 0.35:
            return t[:m.start()]
    return t


def from_html(path):
    s = Strip()
    s.feed(open(path, encoding="utf-8", errors="ignore").read())
    return "".join(s.buf)


def main():
    papers = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    os.makedirs(f"{ROOT}/_work", exist_ok=True)
    for p in papers:
        d = folder(p)
        out = f"{ROOT}/_work/txt_{p['short'].replace(' ', '-')}.txt"
        if os.path.exists(out) and os.path.getsize(out) > 4000:
            continue
        pdf, htm = os.path.join(d, "paper.pdf"), os.path.join(d, "source.html")
        try:
            if os.path.exists(pdf):
                t = from_pdf(pdf)
            elif os.path.exists(htm):
                t = from_html(htm)
            else:
                print(f"[MISS] {p['short']:18s} 没有原文文件"); continue
        except Exception as e:
            print(f"[FAIL] {p['short']:18s} {e}"); continue
        t = drop_references(t)
        t = re.sub(r"\n{3,}", "\n\n", t)[:MAX_CHARS]
        open(out, "w", encoding="utf-8").write(t)
        print(f"[OK]   {p['short']:18s} {len(t):>7,} 字符")


if __name__ == "__main__":
    main()
