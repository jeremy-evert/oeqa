"""Check words.csv and the built PDFs against the teacher's sheet.
Run from the repo root:  python3 tools/verify.py   (needs pdftotext from poppler)"""
import csv, os, re, subprocess, sys
DIRS=["Roll a die.","Find the column that matches your number.",
"Read the word in that column in Row A. Then roll again for Row B, and keep going to Row D.",
"Cover the word, then spell it without looking (out loud or on paper). Uncover it to check.",
"Put a tally mark or a check next to each word you read correctly.",
"Challenge: use each word you read in a sentence."]
EXPECTED={'A':["Her","Church","First","Birthday","Third","Serve"],'B':["Hurt","Turning","Thirst","Verse","Skirt","Burned"],
'C':["Squirm","Nurse","Songbird","Mercy","Large","Before"],'D':["Mercy","Very","Birthday","Every","Thirst","Nurse"]}
ok=True
def check(name,val):
    global ok; print(f"{'PASS' if val else 'FAIL'}  {name}"); ok&=bool(val)
g={(r['row'],int(r['col'])):r['word'] for r in csv.DictReader(open('data/words.csv'))}
check("data/words.csv equals the teacher's 4x6 grid (24 cells)",len(g)==24 and all(g[(r,i+1)]==w for r,ws in EXPECTED.items() for i,w in enumerate(ws)))
def text(f,pages=None):
    a=['pdftotext']+(['-f',str(pages),'-l',str(pages)] if pages else [])+[f,'-']
    return ' '.join(subprocess.run(a,capture_output=True,text=True).stdout.split())
for f in ["dist/01_Roll_and_Read_Clean_Classroom.pdf","dist/02_Roll_and_Read_Playful_Adventure.pdf"]:
    check(f+": file exists",os.path.isfile(f))
    if os.path.isfile(f):
        t=text(f,1); check(f+": directions verbatim, 24 words on page 1",all(' '.join(d.split()) in t for d in DIRS) and all(w in t for ws in EXPECTED.values() for w in ws))
f="dist/03_Roll_and_Read_Phone_Deck.pdf"
check(f+": file exists",os.path.isfile(f))
if os.path.isfile(f):
    t=text(f); check(f+": all words present",all(w in t for ws in EXPECTED.values() for w in ws))
    check(f+": directions verbatim",all(' '.join(d.split()) in text(f,2) for d in DIRS))
h=open('game/index.html',encoding='utf-8').read()
for r,ws in EXPECTED.items():
    m=re.search(r"\b"+r+r":\[([^\]]*)\]",h); check(f"game/index.html row {r} matches",m and re.findall(r"'([^']+)'",m.group(1))==ws)
check("game/index.html directions verbatim",all(d in h for d in DIRS))
sys.exit(0 if ok else 1)
