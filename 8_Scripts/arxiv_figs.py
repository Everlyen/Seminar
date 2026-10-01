#!/usr/bin/env python3
"""
arxiv_figs.py — save every figure from an arXiv paper into a folder named after the paper.

    python arxiv_figs.py <arxiv link or id> <output folder>

Example:
    python arxiv_figs.py https://arxiv.org/abs/1706.03762 ~/Vault/Papers
    → ~/Vault/Papers/Attention Is All You Need/Figure 1.png, Figure 2a.png, ...

Figures are the original files the authors uploaded (from the LaTeX source), named by
their figure number in the paper. Panels inside one figure get a, b, c...
Optional: `pip install pymupdf` turns PDF figures into PNGs. Otherwise only standard Python.
"""

import gzip, io, re, shutil, sys, tarfile, tempfile, urllib.request
from pathlib import Path

EXTS = [".png", ".jpg", ".jpeg", ".pdf", ".eps", ".gif", ".svg"]


def arxiv_id(text):
    text = text.strip()
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/([^\s?#]+)", text)
    text = re.sub(r"\.pdf$", "", m.group(1) if m else text).strip("/")
    if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?|[a-z\-]+(\.[A-Z]{2})?/\d{7}(v\d+)?", text):
        return text
    sys.exit(f"Not an arXiv link or id: {text!r}")


def download(aid):
    req = urllib.request.Request(f"https://arxiv.org/e-print/{aid}",
                                 headers={"User-Agent": "arxiv-figs/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read()
    except Exception as e:
        sys.exit(f"Could not download from arXiv: {e}")


def unpack(data, dest):
    if data[:4] == b"%PDF":
        sys.exit("This paper has no LaTeX source on arXiv, only a PDF.")
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as tar:
            for m in tar.getmembers():
                if (m.isfile() or m.isdir()) and str((dest / m.name).resolve()).startswith(str(dest.resolve())):
                    tar.extract(m, dest)
            return
    except tarfile.ReadError:
        pass
    try:
        data = gzip.decompress(data)
    except OSError:
        pass
    (dest / "main.tex").write_bytes(data)


def braced(s, i):
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{" and s[j - 1] != "\\":
            depth += 1
        elif s[j] == "}" and s[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return s[i + 1:j]
    return s[i + 1:]


def args_of(body, cmd):
    out = []
    for m in re.finditer(r"\\" + cmd + r"\*?\s*(\[[^\]]*\]\s*)*", body):
        if m.end() < len(body) and body[m.end()] == "{":
            out.append(braced(body, m.end()))
    return out


def read_tex(root):
    files = list(root.rglob("*.tex"))
    if not files:
        sys.exit("No LaTeX files in the source.")
    nocomment = lambda p: re.sub(r"(?<!\\)%.*", "", p.read_text(errors="ignore"))
    main = next((f for f in files if "\\documentclass" in f.read_text(errors="ignore")), files[0])
    seen = set()

    def expand(p):
        if p in seen:
            return ""
        seen.add(p)

        def repl(m):
            n = m.group(1).strip()
            for c in (root / n, root / (n + ".tex"), p.parent / n, p.parent / (n + ".tex")):
                if c.is_file():
                    return expand(c)
            return ""
        return re.sub(r"\\(?:input|include|subfile)\s*\{([^}]*)\}", repl, nocomment(p))

    return expand(main)


def short_title(tex, aid):
    t = args_of(tex, "title")
    if not t:
        return aid
    t = re.sub(r"\\thanks\{[^}]*\}|\\\\", " ", t[0])
    for _ in range(3):
        t = re.sub(r"\\[a-zA-Z]+\*?\{([^{}]*)\}", r"\1", t)   # \textbf{x} -> x
    t = re.sub(r"\\[a-zA-Z]+|[{}$~^_]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.split(r"\s*[:?]\s+", t)[0]                       # part before a colon
    words = t.split()
    t = " ".join(words[:8]) + ("…" if len(words) > 8 else "")
    t = re.sub(r'[<>:"/\\|?*]', "", t).strip(" .")             # safe on Windows too
    return t or aid


def find_image(name, root, dirs):
    for base in [root] + [root / d for d in dirs]:
        for cand in [base / name] + [base / (name + e) for e in EXTS]:
            if cand.suffix.lower() in EXTS and cand.is_file():
                return cand
    stem = Path(name).stem.lower()
    return next((p for p in root.rglob("*") if p.suffix.lower() in EXTS and p.stem.lower() == stem), None)


def save(src, out, name):
    if src.suffix.lower() == ".pdf":
        try:
            try:
                import pymupdf as fitz
            except ImportError:
                import fitz
            fitz.open(src)[0].get_pixmap(dpi=200).save(out / (name + ".png"))
            return
        except Exception:
            pass
    shutil.copy2(src, out / (name + src.suffix.lower()))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    aid, out_root = arxiv_id(sys.argv[1]), Path(sys.argv[2]).expanduser()

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        unpack(download(aid) if len(sys.argv) < 4 else Path(sys.argv[3]).read_bytes(), root)
        tex = read_tex(root)
        out = out_root / short_title(tex, aid)
        out.mkdir(parents=True, exist_ok=True)
        dirs = re.findall(r"\{([^{}]+)\}", "".join(args_of(tex, "graphicspath")))

        # Figures are numbered in the order they appear in the paper
        figs = re.findall(r"\\begin\{(?:figure|wrapfigure|SCfigure)\*?\}(.*?)\\end\{(?:figure|wrapfigure|SCfigure)\*?\}", tex, re.S)
        count = 0
        for n, body in enumerate(figs, 1):
            images = [p for p in (find_image(g.strip(), root, dirs) for g in args_of(body, "includegraphics")) if p]
            for k, img in enumerate(images):
                save(img, out, f"Figure {n}" + ("abcdefghijklmnopqrstuvwxyz"[k] if len(images) > 1 else ""))
                count += 1
    print(f"Saved {count} images from {len(figs)} figures to: {out}")


if __name__ == "__main__":
    main()
