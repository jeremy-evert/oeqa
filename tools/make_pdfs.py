#!/usr/bin/env python3
"""Roll and Read packet generator.
Usage: python3 make_pdfs.py words.csv OUTDIR
Produces both design versions from the SAME word table and SAME text.
Page 1 text is verbatim from the clean one-page source document.
Pages 2-5 are NEW optional additions (labelled as such on the page).
"""
import csv, sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor, white

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
# EMBED_FONTS=1 -> embed DejaVu Sans (larger file, identical look everywhere).
# default      -> built-in PDF Helvetica (tiny file; every viewer/printer has it).
EMBED = os.environ.get("EMBED_FONTS") == "1"
if EMBED:
    pdfmetrics.registerFont(TTFont("Body", FONT_DIR + "DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("Bold", FONT_DIR + "DejaVuSans-Bold.ttf"))
else:
    from reportlab.pdfbase.pdfmetrics import Font
    pdfmetrics.registerFont(Font("Body", "Helvetica", "WinAnsiEncoding"))
    pdfmetrics.registerFont(Font("Bold", "Helvetica-Bold", "WinAnsiEncoding"))
ARROW = "  →" if EMBED else "  >"

W, H = letter
M = 40
CW = W - 2 * M
TOTAL_PAGES = 5

# ---------- SOURCE TEXT (verbatim from the clean one-page source) ----------
TITLE1 = "Roll and Read:"
TITLE2 = "R-Controlled Vowels and Tricky Words"
FULL_TITLE = "Roll and Read: R-Controlled Vowels and Tricky Words"
DIRECTIONS = [
    "Roll a die.",
    "Find the column that matches your number.",
    "Read the word in that column in Row A. Then roll again for Row B, and keep going to Row D.",
    "Cover the word, then spell it without looking (out loud or on paper). Uncover it to check.",
    "Put a tally mark or a check next to each word you read correctly.",
    "Challenge: use each word you read in a sentence.",
]
WAYS = [
    ("Partner race:", "Both players roll, read their word, and the first correct reader earns a point."),
    ("Write it:", "Roll, read the word, then write it on a whiteboard or in a notebook."),
    ("Sort it:", "Collect the words and sort them by spelling pattern (er, ir, ur, ear, ar, or) and by tricky words (Very, Every, Before)."),
]

THEMES = {
    "A": dict(name="A — Clean Classroom", ink=HexColor("#111111"), accent=HexColor("#333333"),
              soft=HexColor("#EDEDED"), soft2=HexColor("#F7F7F7"), line=HexColor("#555555"),
              guide=HexColor("#BBBBBB"), muted=HexColor("#666666"), hi=HexColor("#111111")),
    "B": dict(name="B — Playful Adventure", ink=HexColor("#1B1B1B"), accent=HexColor("#0E5A66"),
              soft=HexColor("#D6EEF0"), soft2=HexColor("#FFF1C9"), line=HexColor("#0E5A66"),
              guide=HexColor("#9CC9CE"), muted=HexColor("#555555"), hi=HexColor("#8A3F00")),
}


def load_grid(path):
    g = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            g[(r["row"], int(r["col"]))] = r["word"]
    assert len(g) == 24, "word table must have 24 cells"
    return g


def unique_words(g):
    seen, out = set(), []
    for r in "ABCD":
        for c in range(1, 7):
            w = g[(r, c)]
            if w not in seen:
                seen.add(w)
                out.append(w)
    return out


def wrap_draw(c, text, x, y, width, font, size, leading, color=None):
    if color is not None:
        c.setFillColor(color)
    c.setFont(font, size)
    lines = simpleSplit(text, font, size, width)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= leading
    return y


PIPS = {
    1: [(.5, .5)],
    2: [(.27, .73), (.73, .27)],
    3: [(.27, .73), (.5, .5), (.73, .27)],
    4: [(.27, .73), (.73, .73), (.27, .27), (.73, .27)],
    5: [(.27, .73), (.73, .73), (.5, .5), (.27, .27), (.73, .27)],
    6: [(.27, .73), (.73, .73), (.27, .5), (.73, .5), (.27, .27), (.73, .27)],
}


def dice(c, x, y, s, n, fill, ink, pip):
    c.setStrokeColor(ink)
    c.setLineWidth(1.4)
    c.setFillColor(fill)
    c.roundRect(x, y, s, s, s * 0.18, stroke=1, fill=1)
    c.setFillColor(pip)
    for px, py in PIPS[n]:
        c.circle(x + px * s, y + py * s, s * 0.075, stroke=0, fill=1)


def checkbox(c, x, y, s, th):
    c.setStrokeColor(th["line"])
    c.setLineWidth(1)
    c.setFillColor(white)
    c.rect(x, y, s, s, stroke=1, fill=1)


def write_lines(c, th, x, y, w, n, gap):
    """Primary-style writing lines. y is the first baseline."""
    for i in range(n):
        by = y - i * gap
        c.setStrokeColor(th["guide"])
        c.setLineWidth(0.7)
        c.setDash(3, 3)
        c.line(x, by + gap * 0.40, x + w, by + gap * 0.40)
        c.setDash()
        c.setStrokeColor(th["line"])
        c.setLineWidth(1)
        c.line(x, by, x + w, by)


# ---------- Version B decoration (original shapes only) ----------
def hills(c, x, y, w, h):
    c.saveState()
    p = c.beginPath()
    p.roundRect(x, y, w, h, 10)
    c.clipPath(p, stroke=0, fill=0)
    c.setFillColor(HexColor("#D6EEF0"))
    c.rect(x, y, w, h, stroke=0, fill=1)
    c.setFillColor(HexColor("#B7DEE2"))
    q = c.beginPath()
    q.moveTo(x, y); q.lineTo(x, y + h * 0.45)
    q.lineTo(x + w * 0.18, y + h * 0.80); q.lineTo(x + w * 0.34, y + h * 0.40)
    q.lineTo(x + w * 0.50, y + h * 0.65); q.lineTo(x + w * 0.70, y + h * 0.30)
    q.lineTo(x + w * 0.86, y + h * 0.70); q.lineTo(x + w, y + h * 0.40)
    q.lineTo(x + w, y); q.close()
    c.drawPath(q, stroke=0, fill=1)
    c.setFillColor(HexColor("#8CC7CD"))
    q = c.beginPath()
    q.moveTo(x, y); q.lineTo(x, y + h * 0.20)
    q.lineTo(x + w * 0.25, y + h * 0.42); q.lineTo(x + w * 0.55, y + h * 0.18)
    q.lineTo(x + w * 0.80, y + h * 0.38); q.lineTo(x + w, y + h * 0.15)
    q.lineTo(x + w, y); q.close()
    c.drawPath(q, stroke=0, fill=1)
    # sun
    c.setFillColor(HexColor("#FFD36B"))
    c.setStrokeColor(HexColor("#D9731A"))
    c.setLineWidth(1.2)
    c.circle(x + w - 46, y + h - 26, 14, stroke=1, fill=1)
    c.restoreState()
    c.setStrokeColor(HexColor("#0E5A66"))
    c.setLineWidth(1.2)
    c.roundRect(x, y, w, h, 10, stroke=1, fill=0)


def star(c, cx, cy, r, color):
    import math
    c.setFillColor(color)
    p = c.beginPath()
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        px, py = cx + rr * math.cos(ang), cy + rr * math.sin(ang)
        (p.moveTo if i == 0 else p.lineTo)(px, py)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def footer(c, th, page, note=None):
    c.setFont("Body", 7.5)
    c.setFillColor(th["muted"])
    c.drawString(M, 24, f"Roll and Read · Version {th['name']} · page {page} of {TOTAL_PAGES}")
    if note:
        c.drawRightString(W - M, 24, note)


def header(c, th, ver, page, big=False, badge=None):
    """Returns y just below the header."""
    top = H - 34
    if ver == "A":
        if big:
            c.setFillColor(th["ink"]); c.setFont("Bold", 28)
            c.drawString(M, top - 24, TITLE1)
            c.setFont("Bold", 15)
            c.drawString(M, top - 46, TITLE2)
            c.setStrokeColor(th["ink"]); c.setLineWidth(2)
            c.line(M, top - 56, W - M, top - 56)
            return top - 56
        c.setFillColor(th["ink"]); c.setFont("Bold", 15)
        c.drawString(M, top - 14, FULL_TITLE)
        if badge:
            c.setFont("Bold", 9); c.setFillColor(th["muted"])
            c.drawString(M, top - 28, badge)
        c.setStrokeColor(th["ink"]); c.setLineWidth(1.5)
        c.line(M, top - 36, W - M, top - 36)
        return top - 36
    # version B
    bh = 92 if big else 62
    hills(c, M, top - bh, CW, bh)
    if big:
        star(c, M + CW - 104, top - 20, 6, HexColor("#D9731A"))
        star(c, M + CW - 134, top - 40, 4, HexColor("#0E5A66"))
    c.setFillColor(th["accent"])
    c.setFont("Bold", 8.5)
    c.drawString(M + 16, top - 14 if not big else top - 18, "ADVENTURE TRAIL" if big else (badge or "ADVENTURE TRAIL"))
    if big:
        c.setFont("Bold", 28); c.setFillColor(th["ink"])
        c.drawString(M + 16, top - 48, TITLE1)
        c.setFont("Bold", 14.5)
        c.drawString(M + 16, top - 70, TITLE2)
    else:
        c.setFont("Bold", 13); c.setFillColor(th["ink"])
        c.drawString(M + 16, top - 38, FULL_TITLE)
    return top - bh


def grid(c, th, ver, g, y_top, hdr_h, row_h):
    lab_w = 52
    cell_w = (CW - lab_w) / 6
    x0 = M
    # header row
    c.setLineWidth(1.4)
    c.setStrokeColor(th["ink"] if ver == "A" else th["line"])
    c.setFillColor(th["soft"] if ver == "A" else th["soft2"])
    c.rect(x0, y_top - hdr_h, lab_w, hdr_h, stroke=1, fill=1)
    c.setFillColor(th["ink"]); c.setFont("Bold", 9.5)
    c.drawCentredString(x0 + lab_w / 2, y_top - hdr_h / 2 - 3.5, "ROLL")
    for i in range(6):
        cx = x0 + lab_w + i * cell_w
        c.setFillColor(th["soft"] if ver == "A" else th["soft2"])
        c.setStrokeColor(th["ink"] if ver == "A" else th["line"])
        c.rect(cx, y_top - hdr_h, cell_w, hdr_h, stroke=1, fill=1)
        s = 26
        dice(c, cx + 9, y_top - hdr_h / 2 - s / 2, s, i + 1,
             white, th["ink"], th["ink"] if ver == "A" else th["hi"])
        c.setFillColor(th["ink"]); c.setFont("Bold", 20)
        c.drawString(cx + 9 + s + 9, y_top - hdr_h / 2 - 7, str(i + 1))
    # body rows
    for ri, r in enumerate("ABCD"):
        ry = y_top - hdr_h - (ri + 1) * row_h
        c.setStrokeColor(th["ink"] if ver == "A" else th["line"])
        c.setLineWidth(1.4)
        c.setFillColor(th["soft"] if ver == "A" else th["soft2"])
        c.rect(x0, ry, lab_w, row_h, stroke=1, fill=1)
        c.setFillColor(th["ink"]); c.setFont("Bold", 9)
        c.drawCentredString(x0 + lab_w / 2, ry + row_h - 15, "ROW")
        if ver == "A":
            c.setFont("Bold", 24)
            c.drawCentredString(x0 + lab_w / 2, ry + row_h / 2 - 13, r)
        else:
            c.setFillColor(th["accent"])
            c.circle(x0 + lab_w / 2, ry + row_h / 2 - 8, 14, stroke=0, fill=1)
            c.setFillColor(white); c.setFont("Bold", 17)
            c.drawCentredString(x0 + lab_w / 2, ry + row_h / 2 - 14, r)
        for ci in range(6):
            cx = x0 + lab_w + ci * cell_w
            if ver == "B" and (ri + ci) % 2 == 0:
                c.setFillColor(HexColor("#EAF6F7"))
            else:
                c.setFillColor(white)
            c.setStrokeColor(th["ink"] if ver == "A" else th["line"])
            c.setLineWidth(1.4)
            c.rect(cx, ry, cell_w, row_h, stroke=1, fill=1)
            word = g[(r, ci + 1)]
            size = 15.5
            while pdfmetrics.stringWidth(word, "Body", size) > cell_w - 14 and size > 10:
                size -= 0.5
            c.setFillColor(th["ink"]); c.setFont("Body", size)
            c.drawCentredString(cx + cell_w / 2, ry + row_h / 2 - 8, word)
            checkbox(c, cx + cell_w - 14, ry + row_h - 14, 9, th)  # NEW: check-off box
    return y_top - hdr_h - 4 * row_h


def page1(c, th, ver, g):
    y = header(c, th, ver, 1, big=True)
    y -= 26
    c.setFillColor(th["ink"]); c.setFont("Body", 11)
    c.drawString(M, y, "Name:")
    c.line(M + 38, y - 2, M + 300, y - 2)
    c.drawString(M + 330, y, "Date:")
    c.line(M + 364, y - 2, W - M, y - 2)
    y -= 26
    c.setFont("Bold", 13); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
    c.drawString(M, y, "Directions")
    y -= 17
    for i, d in enumerate(DIRECTIONS, 1):
        c.setFont("Bold", 11); c.setFillColor(th["ink"])
        c.drawString(M + 2, y, f"{i}.")
        y = wrap_draw(c, d, M + 20, y, CW - 20, "Body", 10.5, 14.5, th["ink"]) - 3.5
    y -= 8
    row_h = 54 if ver == "A" else 50
    gy = grid(c, th, ver, g, y, 40, row_h)
    y = gy - 22
    c.setFont("Bold", 12); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
    c.drawString(M, y, "Words I Read Correctly")
    write_lines(c, th, M, y - 24, CW, 2, 24)
    y -= 24 + 24 + 24
    c.setFont("Bold", 12); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
    c.drawString(M, y, "Ways to Play")
    y -= 16
    for lead, body in WAYS:
        c.setFont("Body", 10.5); c.setFillColor(th["ink"])
        c.drawString(M + 2, y, "•")
        c.setFont("Bold", 10.5)
        c.drawString(M + 14, y, lead)
        lw = pdfmetrics.stringWidth(lead + " ", "Bold", 10.5)
        # first line continues after lead
        words = body.split(" ")
        line, first = "", True
        c.setFont("Body", 10.5)
        xcur = M + 14 + lw
        avail = CW - 14 - lw
        lines = simpleSplit(body, "Body", 10.5, avail)
        c.drawString(xcur, y, lines[0])
        rest = body[len(lines[0]):].strip()
        y -= 13.5
        if rest:
            y = wrap_draw(c, rest, M + 14, y, CW - 14, "Body", 10.5, 13.5, th["ink"])
        y -= 2
    assert y > 52, f"page 1 overflow: y={y}"
    footer(c, th, 1, "Page 1 = original activity, re-typeset · Pages 2–5 = optional new additions")
    c.showPage()
    return y


def practice_header(c, th, ver, page, name):
    y = header(c, th, ver, page, big=False, badge="NEW · OPTIONAL ADDITION — " + name)
    return y - (0 if ver == "A" else 12)


def badge_note(c, th, ver, y, text):
    c.setFont("Body", 9.5); c.setFillColor(th["muted"])
    return wrap_draw(c, text, M, y, CW, "Body", 9.5, 12.5, th["muted"])


def word_chips(c, th, ver, words, x, y, per_row, chip_w, chip_h, gap):
    for i, w in enumerate(words):
        r, k = divmod(i, per_row)
        cx = x + k * (chip_w + gap)
        cy = y - r * (chip_h + gap)
        c.setStrokeColor(th["line"]); c.setLineWidth(1)
        c.setFillColor(th["soft2"] if ver == "B" else white)
        c.roundRect(cx, cy - chip_h, chip_w, chip_h, 7, stroke=1, fill=1)
        c.setFillColor(th["ink"]); c.setFont("Body", 11)
        c.drawCentredString(cx + chip_w / 2, cy - chip_h + 7, w)
    rows = (len(words) + per_row - 1) // per_row
    return y - rows * (chip_h + gap)


def page2(c, th, ver, g):
    y = practice_header(c, th, ver, 2, "Spell It, Check It!")
    y -= 14
    c.setFont("Bold", 20); c.setFillColor(th["ink"])
    c.drawString(M, y - 6, "Spell It, Check It!")
    y -= 22
    y = badge_note(c, th, ver, y - 2, "Roll and read a word from page 1. Write it, cover it, spell it from memory, then check. Four rounds.")
    y -= 8
    panel_h = 124
    steps = ["1 READ", "2 COVER", "3 SPELL", "4 CHECK"]
    for rnd in range(4):
        top = y
        c.setStrokeColor(th["line"]); c.setLineWidth(1.4)
        c.setFillColor(white)
        c.roundRect(M, top - panel_h, CW, panel_h, 8, stroke=1, fill=1)
        # step strip
        c.setFillColor(th["soft"] if ver == "A" else th["soft2"])
        c.roundRect(M, top - 22, CW, 22, 8, stroke=0, fill=1)
        c.setStrokeColor(th["line"]); c.line(M, top - 22, M + CW, top - 22)
        c.setFillColor(th["ink"]); c.setFont("Bold", 9.5)
        c.drawString(M + 10, top - 15, f"ROUND {rnd + 1}")
        for si, s in enumerate(steps):
            c.drawString(M + 130 + si * 100, top - 15, s + (ARROW if si < 3 else ""))
        # read area
        c.setFont("Body", 9.5); c.setFillColor(th["muted"])
        c.drawString(M + 10, top - 42, "Word I rolled:")
        c.setStrokeColor(th["line"]); c.setLineWidth(1)
        c.line(M + 10, top - 70, M + 136, top - 70)
        c.setFillColor(th["muted"]); c.drawString(M + 10, top - 83, "(read it out loud)")
        # spell area
        c.setFillColor(th["muted"]); c.setFont("Body", 9.5)
        c.drawString(M + 160, top - 42, "Cover it. Spell it here:")
        write_lines(c, th, M + 160, top - 66, CW - 176, 2, 30)
        # check
        checkbox(c, M + 10, top - 112, 11, th)
        checkbox(c, M + 160, top - 112, 11, th)
        c.setFillColor(th["ink"]); c.setFont("Body", 10)
        c.drawString(M + 26, top - 110, "I spelled it right")
        c.drawString(M + 176, top - 110, "I fixed it")
        y = top - panel_h - 8
    c.setFont("Bold", 10.5); c.setFillColor(th["ink"])
    c.drawString(M, y - 8, "Word bank (the words on page 1):")
    words = unique_words(g)
    wrap_draw(c, "   ".join(words), M, y - 24, CW, "Body", 10.5, 14, th["ink"])
    assert y - 24 - 28 > 40, f"page 2 overflow y={y}"
    footer(c, th, 2, "New content · not from the original sheet · not educator-reviewed")
    c.showPage()


def page3(c, th, ver, g):
    y = practice_header(c, th, ver, 3, "Word Detective")
    y -= 14
    c.setFont("Bold", 20); c.setFillColor(th["ink"])
    c.drawString(M, y - 6, "Word Detective")
    y -= 22
    y = badge_note(c, th, ver, y - 2,
                   "Write each word where you think it belongs. Some words may fit more than one spot, or none. Put those in “Let’s Discuss” and talk it over with your teacher or grown-up.")
    y -= 6
    words = unique_words(g)
    y = word_chips(c, th, ver, words, M, y, 5, 98, 24, 8.5)
    y -= 6
    pats = ["er", "ir", "ur", "ear", "ar", "or"]
    bw, bh, gap = (CW - 2 * 10) / 3, 112, 10
    for i, p in enumerate(pats):
        r, k = divmod(i, 3)
        bx = M + k * (bw + gap)
        by = y - r * (bh + gap)
        c.setStrokeColor(th["line"]); c.setLineWidth(1.4)
        c.setFillColor(white)
        c.roundRect(bx, by - bh, bw, bh, 8, stroke=1, fill=1)
        c.setFillColor(th["soft"] if ver == "A" else th["soft2"])
        c.roundRect(bx, by - 30, bw, 30, 8, stroke=0, fill=1)
        c.setStrokeColor(th["line"]); c.line(bx, by - 30, bx + bw, by - 30)
        c.setFillColor(th["ink"]); c.setFont("Bold", 17)
        c.drawString(bx + 12, by - 22, p)
        write_lines(c, th, bx + 10, by - 54, bw - 20, 3, 24)
    y = y - 2 * (bh + gap)
    c.setStrokeColor(th["line"]); c.setLineWidth(1.4); c.setFillColor(white)
    dh = 104
    c.roundRect(M, y - dh, CW, dh, 8, stroke=1, fill=1)
    c.setFillColor(th["ink"]); c.setFont("Bold", 14)
    c.drawString(M + 12, y - 22, "Let’s Discuss")
    c.setFont("Body", 9); c.setFillColor(th["muted"])
    c.drawString(M + 12, y - 36, "Words that fit more than one spot, or none. The original sheet lists Very, Every, Before as tricky words.")
    write_lines(c, th, M + 12, y - 62, CW - 24, 2, 26)
    y -= dh
    c.setFont("Body", 8.5); c.setFillColor(th["muted"])
    wrap_draw(c, "No answer key is supplied. Sorting words by pattern needs educator review before use as an assessment.",
              M, y - 14, CW, "Body", 8.5, 11, th["muted"])
    assert y - 30 > 40, f"page 3 overflow y={y}"
    footer(c, th, 3, "New content · not from the original sheet · not educator-reviewed")
    c.showPage()


def page4(c, th, ver, g):
    y = practice_header(c, th, ver, 4, "Silly Sentence Lab")
    y -= 14
    c.setFont("Bold", 20); c.setFillColor(th["ink"])
    c.drawString(M, y - 6, "Silly Sentence Lab")
    y -= 22
    y = badge_note(c, th, ver, y - 2, "Pick two words from the game. Write one funny sentence that uses both. Draw it. Read it out loud!")
    y -= 14
    c.setFillColor(th["ink"]); c.setFont("Bold", 12)
    c.drawString(M, y, "My two words:")
    c.setStrokeColor(th["line"]); c.setLineWidth(1)
    c.line(M + 112, y - 2, M + 262, y - 2)
    c.drawString(M + 274, y, "and")
    c.line(M + 304, y - 2, M + 454, y - 2)
    y -= 30
    c.setFont("Bold", 12)
    c.drawString(M, y, "My sentence:")
    write_lines(c, th, M, y - 30, CW, 4, 34)
    y = y - 30 - 3 * 34 - 24
    c.setFont("Bold", 12); c.setFillColor(th["ink"])
    c.drawString(M, y, "My picture:")
    bh = y - 70 - 40
    c.setStrokeColor(th["line"]); c.setLineWidth(1.6); c.setFillColor(white)
    c.roundRect(M, 78, CW, y - 12 - 78, 10, stroke=1, fill=1)
    checkbox(c, M, 50, 12, th)
    c.setFillColor(th["ink"]); c.setFont("Body", 11)
    c.drawString(M + 20, 52, "I read my sentence out loud.")
    assert y - 12 - 78 > 120, "page 4 picture box too small"
    footer(c, th, 4, "New content · not from the original sheet · not educator-reviewed")
    c.showPage()


def page5(c, th, ver, g):
    y = practice_header(c, th, ver, 5, "Caregiver Panel")
    y -= 14
    c.setFont("Bold", 20); c.setFillColor(th["ink"])
    c.drawString(M, y - 6, "For Grown-Ups: Playing Roll and Read")
    y -= 30
    sections = [
        ("What the game is",
         "Your child rolls a die, finds the matching column, and reads a word. Then they cover the word, spell it from memory, and uncover it to check. They put a check or tally by each word they read correctly."),
        ("A short practice session",
         "Ten to fifteen minutes can be plenty, if that suits your child. Stop sooner if they are tired or frustrated. A few words, read happily, is a good day."),
        ("How you can help",
         "Let your child try first and wait a few seconds before helping. Praise effort and strategies (“You sounded that out!”). If a word is stuck, say it together and move on. The original sheet calls Very, Every, and Before “tricky words,” so ask the teacher how they would like those practiced."),
        ("Good to know",
         "This page is a family guide written for this packet. It is not a substitute for reading instruction or intervention. If reading feels very hard for your child, talk with their teacher."),
    ]
    for head, body in sections:
        c.setFont("Bold", 12); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
        c.drawString(M, y, head)
        y = wrap_draw(c, body, M, y - 15, CW, "Body", 10.5, 14, th["ink"]) - 10
    c.setFont("Bold", 12); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
    c.drawString(M, y, "Notes of encouragement (for your child)")
    write_lines(c, th, M, y - 26, CW, 2, 28)
    y = y - 26 - 28 - 22
    c.setFont("Bold", 12); c.setFillColor(th["accent"] if ver == "B" else th["ink"])
    c.drawString(M, y, "Feedback for the teacher")
    c.setFont("Body", 9.5); c.setFillColor(th["muted"])
    c.drawString(M, y - 14, "Could you use this tomorrow, and what would you change?")
    write_lines(c, th, M, y - 40, CW, 3, 28)
    assert y - 40 - 2 * 28 > 52, f"page 5 overflow y={y}"
    footer(c, th, 5, "New content · not educator-reviewed · permissions unconfirmed")
    c.showPage()


def build(ver, g, outpath):
    th = THEMES[ver]
    c = canvas.Canvas(outpath, pagesize=letter)
    c.setTitle(f"Roll and Read — Version {th['name']}")
    c.setAuthor("Community Anchors template test (Claude)")
    c.setSubject("R-Controlled Vowels and Tricky Words — printable activity packet")
    page1(c, th, ver, g)
    page2(c, th, ver, g)
    page3(c, th, ver, g)
    page4(c, th, ver, g)
    page5(c, th, ver, g)
    c.save()


if __name__ == "__main__":
    grid_data = load_grid(sys.argv[1])
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    build("A", grid_data, os.path.join(out, "01_Roll_and_Read_Clean_Classroom.pdf"))
    build("B", grid_data, os.path.join(out, "02_Roll_and_Read_Playful_Adventure.pdf"))
    print("built", len(unique_words(grid_data)), "unique words from 24 cells")
