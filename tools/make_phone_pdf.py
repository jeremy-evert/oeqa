#!/usr/bin/env python3
"""Phone-sized (9:16) Roll and Read deck. Usage: python3 make_phone_pdf.py words.csv out.pdf
Words and directions are the teacher's sheet, verbatim. Pages marked NEW are additions."""
import csv, sys
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor, white

W, H = 360, 640          # 9:16 portrait, big type, fits a phone screen
INK, TEAL, SKY = HexColor("#0B3340"), HexColor("#0E5A66"), HexColor("#CFEFF2")
SUN, FLAME, PAPER = HexColor("#FFC94A"), HexColor("#B94E0A"), HexColor("#FFFDF6")
DIRECTIONS = ["Roll a die.", "Find the column that matches your number.",
 "Read the word in that column in Row A. Then roll again for Row B, and keep going to Row D.",
 "Cover the word, then spell it without looking (out loud or on paper). Uncover it to check.",
 "Put a tally mark or a check next to each word you read correctly.",
 "Challenge: use each word you read in a sentence."]
WAYS = [("Partner race:", "Both players roll, read their word, and the first correct reader earns a point."),
 ("Write it:", "Roll, read the word, then write it on a whiteboard or in a notebook."),
 ("Sort it:", "Collect the words and sort them by spelling pattern (er, ir, ur, ear, ar, or) and by tricky words (Very, Every, Before).")]
PIPS = {1:[5],2:[1,9],3:[1,5,9],4:[1,3,7,9],5:[1,3,5,7,9],6:[1,3,4,6,7,9]}
TOTAL = 9

def load(p):
    g = {}
    for r in csv.DictReader(open(p, newline="", encoding="utf-8")):
        g[(r["row"], int(r["col"]))] = r["word"]
    assert len(g) == 24
    return g

def die(c, x, y, s, n):
    c.setStrokeColor(INK); c.setLineWidth(2.5); c.setFillColor(white)
    c.roundRect(x, y, s, s, s*.2, stroke=1, fill=1)
    c.setFillColor(INK)
    for k in PIPS[n]:
        r, q = divmod(k-1, 3)
        c.circle(x + s*(.24 + .26*q), y + s*(.76 - .26*r), s*.075, stroke=0, fill=1)

def bg(c):
    c.setFillColor(SKY); c.rect(0, 0, W, H, stroke=0, fill=1)

def hills(c):
    c.setFillColor(HexColor("#8CC7CD"))
    p = c.beginPath(); p.moveTo(0,0); p.lineTo(0,70); p.lineTo(70,110); p.lineTo(140,66); p.lineTo(220,122); p.lineTo(300,70); p.lineTo(W,100); p.lineTo(W,0); p.close(); c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(TEAL)
    p = c.beginPath(); p.moveTo(0,0); p.lineTo(0,46); p.lineTo(90,76); p.lineTo(200,44); p.lineTo(290,70); p.lineTo(W,48); p.lineTo(W,0); p.close(); c.drawPath(p, stroke=0, fill=1)
    c.setFillColor(SUN); c.setStrokeColor(FLAME); c.setLineWidth(2); c.circle(W-52, 104, 20, stroke=1, fill=1)

def footer(c, n, note):
    c.setFont("Helvetica", 7); c.setFillColor(HexColor("#EAF6F7") if n in (1,) else INK)
    c.drawString(16, 14, f"Roll and Read · page {n} of {TOTAL} · {note}")

def card(c, x, y, w, h, fill=PAPER):
    c.setStrokeColor(INK); c.setLineWidth(2.5); c.setFillColor(fill); c.roundRect(x, y, w, h, 14, stroke=1, fill=1)

def wrap(c, text, x, y, w, font, size, lead):
    c.setFont(font, size)
    for ln in simpleSplit(text, font, size, w):
        c.drawString(x, y, ln); y -= lead
    return y

def newtag(c, x, y, text="NEW · not teacher-reviewed"):
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(INK)
    tw = c.stringWidth(text, "Helvetica-Bold", 7.5) + 12
    c.setStrokeColor(INK); c.setDash(2, 2); c.setLineWidth(1); c.setFillColor(white); c.roundRect(x, y, tw, 15, 4, stroke=1, fill=1); c.setDash()
    c.setFillColor(INK); c.drawString(x+6, y+4.5, text)

def cover(c):
    bg(c); hills(c)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 52); c.drawString(24, 510, "Roll &")
    c.drawString(24, 458, "Read")
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold", 17); c.drawString(24, 428, "R-controlled vowels")
    c.drawString(24, 406, "and tricky words")
    die(c, 28, 300, 80, 4); die(c, 124, 300, 80, 2)
    card(c, 24, 214, 312, 60, SUN)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 20); c.drawCentredString(W/2, 237, "Swipe to start  >")
    c.setFont("Helvetica", 9); c.setFillColor(INK); c.drawString(24, 190, "Grab a real die. Four rows. Twenty-four words.")
    footer(c, 1, "Reading game for 3rd grade")
    c.showPage()

def howto(c):
    bg(c); c.setFillColor(INK); c.setFont("Helvetica-Bold", 28); c.drawString(20, 590, "How to play")
    y = 556
    for i, d in enumerate(DIRECTIONS, 1):
        lines = simpleSplit(d, "Helvetica", 14.5, W-84)
        h = len(lines)*18 + 18
        card(c, 16, y-h+8, W-32, h)
        c.setFillColor(FLAME); c.circle(38, y-h/2+8, 12, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 14); c.drawCentredString(38, y-h/2+3, str(i))
        c.setFillColor(INK); wrap(c, d, 60, y-8, W-84, "Helvetica", 14.5, 18)
        y -= h + 10
    c.setFillColor(TEAL); c.setFont("Helvetica-Bold", 13); c.drawString(20, y-6, "Ways to Play")
    y -= 24; c.setFillColor(INK)
    for lead, body in WAYS:
        c.setFont("Helvetica-Bold", 9.5); c.drawString(20, y, lead)
        lw = c.stringWidth(lead + " ", "Helvetica-Bold", 9.5)
        lines = simpleSplit(body, "Helvetica", 9.5, W-40-lw)
        c.setFont("Helvetica", 9.5); c.drawString(20+lw, y, lines[0]); y -= 12
        rest = body[len(lines[0]):].strip()
        if rest: y = wrap(c, rest, 20, y, W-40, "Helvetica", 9.5, 12)
        y -= 4
    assert y > 40
    footer(c, 2, "Directions and Ways to Play: teacher's sheet, word for word")
    c.showPage()

def row_page(c, g, r, n):
    bg(c)
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 30); c.drawString(20, 590, f"Row {r}")
    c.setFont("Helvetica", 11); c.setFillColor(TEAL); c.drawString(20, 570, "Roll a die. Find your number. Read that word.")
    cw, chh, gx, gy = 150, 128, 12, 12
    for i in range(6):
        col, rr = i % 2, i // 2
        x = 20 + col*(cw+gx); y = 548 - (rr+1)*chh - rr*gy
        card(c, x, y, cw, chh, PAPER if (col+rr) % 2 == 0 else HexColor("#FFF1C9"))
        die(c, x+10, y+chh-46, 36, i+1)
        w = g[(r, i+1)]
        size = 30
        while c.stringWidth(w, "Helvetica-Bold", size) > cw-20: size -= 1
        c.setFillColor(INK); c.setFont("Helvetica-Bold", size); c.drawCentredString(x+cw/2, y+34, w)
        if w in ("Very", "Every", "Before"):
            c.setFillColor(INK); c.roundRect(x+cw-70, y+chh-30, 60, 18, 9, stroke=0, fill=1)
            c.setFillColor(white); c.setFont("Helvetica-Bold", 8); c.drawCentredString(x+cw-40, y+chh-24, "TRICKY")
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 12); c.drawString(20, 62, "Then: cover it, spell it, uncover it to check.")
    c.setFont("Helvetica", 10); c.drawString(20, 46, "Make a tally mark for each word you read correctly.")
    footer(c, n, "Words: teacher's sheet, row " + r)
    c.showPage()

def tricky(c):
    bg(c); c.setFillColor(INK); c.setFont("Helvetica-Bold", 28); c.drawString(20, 590, "Tricky words")
    newtag(c, 20, 560)
    y = 520
    c.setFont("Helvetica", 12); c.setFillColor(INK)
    y = wrap(c, "The teacher's sheet calls these three words tricky. Say each one out loud. Look closely. Which part surprises you?", 20, y, W-40, "Helvetica", 12, 16) - 10
    for w in ("Very", "Every", "Before"):
        card(c, 20, y-86, W-40, 86, SUN if w == "Very" else PAPER)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 44); c.drawCentredString(W/2, y-60, w)
        y -= 100
    c.setFont("Helvetica", 9); c.setFillColor(INK)
    wrap(c, "Ask your teacher how they want these words practiced. No answer key is supplied.", 20, 70, W-40, "Helvetica", 9, 12)
    footer(c, 7, "Tricky words: from the sheet · layout is NEW")
    c.showPage()

def sentence(c):
    bg(c); c.setFillColor(INK); c.setFont("Helvetica-Bold", 28); c.drawString(20, 590, "Silly sentence")
    newtag(c, 20, 560)
    steps = ["Pick two words from the game.", "Say one funny sentence that uses both.", "Write it in a notebook, or tell a grown-up.", "Read it out loud!"]
    y = 520
    for i, s in enumerate(steps, 1):
        lines = simpleSplit(s, "Helvetica-Bold", 16, W-100)
        h = len(lines)*20 + 22
        card(c, 20, y-h, W-40, h)
        c.setFillColor(FLAME); c.circle(46, y-h/2, 15, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 16); c.drawCentredString(46, y-h/2-5, str(i))
        c.setFillColor(INK); wrap(c, s, 72, y-26, W-100, "Helvetica-Bold", 16, 20)
        y -= h + 14
    c.setFont("Helvetica", 11); c.setFillColor(INK)
    wrap(c, "Example idea: use Nurse and Songbird. Make it as silly as you like!", 20, y-8, W-40, "Helvetica", 11, 15)
    footer(c, 8, "Challenge from the sheet · layout is NEW")
    c.showPage()

def grownups(c):
    bg(c); c.setFillColor(INK); c.setFont("Helvetica-Bold", 26); c.drawString(20, 590, "For grown-ups")
    newtag(c, 20, 562)
    parts = [("What the game is", "Your child rolls a die, finds the matching column, and reads a word. Then they cover the word, spell it, and uncover it to check."),
             ("A short session", "Ten to fifteen minutes can be plenty. Stop sooner if they are tired. A few words, read happily, is a good day."),
             ("How you can help", "Let your child try first. Praise effort (\"You sounded that out!\"). If a word is stuck, say it together and move on."),
             ("Good to know", "Words and directions come from the teacher's sheet. Pages 7 and 8 are new and not educator-reviewed. Permission to share the original is not confirmed. Not a substitute for reading instruction."),
             ("Feedback", "Could you use this tomorrow, and what would you change?")]
    y = 540
    for h, t in parts:
        c.setFillColor(FLAME); c.setFont("Helvetica-Bold", 13); c.drawString(20, y, h)
        c.setFillColor(INK); y = wrap(c, t, 20, y-16, W-40, "Helvetica", 11, 14) - 12
    footer(c, 9, "NEW · not educator-reviewed · permissions unconfirmed")
    c.showPage()

def build(g, out):
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Roll and Read - Phone Deck"); c.setAuthor("Community Anchors template test (Claude)")
    cover(c); howto(c)
    for i, r in enumerate("ABCD"): row_page(c, g, r, 3+i)
    tricky(c); sentence(c); grownups(c)
    c.save()

if __name__ == "__main__":
    build(load(sys.argv[1]), sys.argv[2])
