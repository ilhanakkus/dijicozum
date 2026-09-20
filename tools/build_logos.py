"""DijiÇözüm logo dosyalarını üretir. Yazılar eğrilere (path) çevrilir, yazı tipi gerekmez.

Kullanım:
    python3 -m venv .venv && .venv/bin/pip install fonttools
    .venv/bin/python tools/build_logos.py path/to/PlusJakartaSans-ExtraBold.ttf

Yazı tipi: Plus Jakarta Sans ExtraBold (SIL Open Font License).
Çıktı: assets/logo/*.svg
"""
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

NAVY, ORANGE, ORANGE_DARK_BG, WHITE, BLACK = "#0f172a", "#e8590c", "#ff8a4c", "#ffffff", "#000000"
TRACKING = -0.03  # em

font = TTFont(sys.argv[1])
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
UPEM = font["head"].unitsPerEm
CAP = font["OS/2"].sCapHeight


def text_paths(segments, x, baseline, size):
    """segments: [(metin, renk)] -> ([(d, renk)], bitiş_x)"""
    s = size / UPEM
    out = []
    for text, color in segments:
        parts = []
        for ch in text:
            name = cmap[ord(ch)]
            pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
            gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
            d = pen.getCommands()
            if d:
                parts.append(d)
            x += hmtx[name][0] * s + TRACKING * size
        out.append((" ".join(parts), color))
    return out, x - TRACKING * size


def svg(w, h, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
        f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{title}">'
        f"<title>{title}</title>{body}</svg>\n"
    )


def icon(x=0, y=0, bg=ORANGE, fg=WHITE):
    return (
        f'<g transform="translate({x} {y})"><rect width="44" height="44" rx="12" fill="{bg}"/>'
        f'<circle cx="22" cy="19" r="7" fill="none" stroke="{fg}" stroke-width="3.4"/>'
        f'<path d="M22 27v9" stroke="{fg}" stroke-width="3.4" stroke-linecap="round" fill="none"/></g>'
    )


def paths(items):
    return "".join(f'<path d="{d}" fill="{c}"/>' for d, c in items)


def lockup_a(c1, c2, icon_bg, icon_fg):
    size, gap = 30, 12
    base = 22 + CAP / UPEM * size / 2
    items, end = text_paths([("Diji", c1), ("Çözüm", c2)], 44 + gap, base, size)
    return svg(end + 2, 44, icon(0, 0, icon_bg, icon_fg) + paths(items), "DijiÇözüm")


def wordmark_c(c1, c2):
    size = 40
    items, end = text_paths([("diji", c1), ("çözüm.", c2)], 2, size * 1.0, size)
    return svg(end + 2, size * 1.4, paths(items), "dijiçözüm")


out = Path(__file__).resolve().parent.parent / "assets" / "logo"
out.mkdir(parents=True, exist_ok=True)
files = {
    # A: ikon + yazı
    "logo-a.svg": lockup_a(NAVY, ORANGE, ORANGE, WHITE),
    "logo-a-dark.svg": lockup_a(WHITE, ORANGE_DARK_BG, ORANGE, WHITE),
    "logo-a-mono.svg": lockup_a(BLACK, BLACK, BLACK, WHITE),
    # C: yalnızca yazı
    "logo-c.svg": wordmark_c(NAVY, ORANGE),
    "logo-c-dark.svg": wordmark_c(WHITE, ORANGE_DARK_BG),
    "logo-c-mono.svg": wordmark_c(BLACK, BLACK),
    # Simge
    "icon.svg": svg(44, 44, icon(), "DijiÇözüm simgesi"),
}
for name, content in files.items():
    (out / name).write_text(content, encoding="utf-8")
    print(f"{name:20s} {len(content):6d} bayt")
