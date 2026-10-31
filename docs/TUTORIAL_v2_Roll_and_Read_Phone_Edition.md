# HOW TO MAKE A PHONE-READY GAME (Tutorial v2)

Worked example: **Roll and Read: R-Controlled Vowels and Tricky Words**, 3rd grade
Community Anchors · October 31, 2026

---

## WHY A SECOND TUTORIAL

The first attempt worked for an AI with a programming sandbox. An independent test with a different AI showed what a classroom teacher would hit:

| Finding from the test | What v2 does about it |
|---|---|
| Teacher independence scored 2 of 5. The route assumed Python and file tools. | Four routes by what your AI can actually make. A no-code route is first-class. |
| "Faithful" was undefined. A check box in every cell: change or not? | A Fidelity Contract: Locked, Allowed, Must be listed, Never. |
| Page names and sort lists differed between the guide, tutorial and source. | One word table, one name per activity. The CSV is the single source of truth. |
| "Carefully reviewed sorting" had no reviewer. | The brief asks for a named reviewer. Otherwise every page says "Not reviewed". |
| Three uploaded PDFs were damaged. File size matched. Only reading the text back caught it. | Stage 5: read every saved file back. Avoid sending binary files by hand. |
| The sheet is built for paper at 8.5 by 11. Children play on phones. | A phone route with tap-to-roll, hear-it, letter tiles and a trail. |

Not yet tested: a real child, a real caregiver, a real teacher, a printer, a screen reader. The phone version is a first draft for those people to react to.

---

## WHAT WE MAKE

1. **Phone Quest** (a web page). Roll the on-screen die, or tap the number from a real die. Read the word and tap "Hear it". Cover it. Build it from letter tiles, or choose "spell out loud or on paper". Uncover to check. Add a tally mark. Four rows make a trail. At the end: Silly Sentence Lab and Word Detective, both tagged NEW.
2. **Phone Deck** (a PDF, 9:16 pages). Swipe through the directions, one page per row, tricky words, a sentence challenge and a grown-up page. It is for reading and saying, with a real die. A PDF cannot do tap games.
3. **Print Packet** (US Letter, grayscale). The version 1 files.

All three use one word table, `words.csv`, and the same 24 words in the same cells.

---

## THE STEPS

### Step 1. Type the worksheet
Read the sheet on paper. Type every word and direction. Do not paste a photo that shows names or handwriting. Mark anything unsure as [VERIFY]. Read your typing against the paper once, out loud, slowly.

For this sheet the grid is:

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Row A | Her | Church | First | Birthday | Third | Serve |
| Row B | Hurt | Turning | Thirst | Verse | Skirt | Burned |
| Row C | Squirm | Nurse | Songbird | Mercy | Large | Before |
| Row D | Mercy | Very | Birthday | Every | Thirst | Nurse |

Two things to notice, and not to "fix": four words appear twice (Mercy, Birthday, Thirst, Nurse), so 24 cells hold 20 different words. And the sheet's "Sort it" list includes **ear**, but no word on the grid clearly uses it. Ask the teacher.

### Step 2. Write the brief
Use Part A of Template v2. The two lines most people skip are "Locked" and "Who reviews". Fill both in.

### Step 3. Ask your AI what it can really make
This is Stage 0 of the Master Prompt. If it says it can make a web page, take the Phone Quest route. If only text, take Docs Only. Do not let it promise a file it cannot make.

### Step 4. Build the locked part first
The directions, the 4 by 6 grid and the "Ways to Play" come over exactly as written. Add the fun around them, not into them.

### Step 5. Add the fun (and tag it)
For a 3rd grader on a phone, these made the difference in the example:

- **A tumbling die** instead of a Next button. A "use my real die" row of six numbers sits underneath.
- **Hear it** on every word, using the phone's own voice, when it has one.
- **Letter tiles** to spell, with "spell it out loud or on paper" kept as a choice, as the sheet says.
- **A letter-pair highlight** (er, ir, ur, ear, ar, or) found by matching the letters. It is not a phonics ruling, and the page says so.
- **A trail** with Row A to Row D, a star count, a tally mark in the teacher's style (four lines and a slash).
- **No failure state.** A mismatch shows the letters side by side. There is no buzzer.

Every item above is tagged NEW on screen and listed under "Changes from the original".

### Step 6. Check it with a script, not your eyes
Compare every locked item against the typed original:

```
python3 verify.py        # checks the CSV against the expected grid
```

No Python? Print the table from your brief and tick each cell against the finished screen.

### Step 7. Test on a real phone
Portrait. One hand. Sound off, then on. Nothing sideways. No tiny buttons. If your AI made a web page, open its link on the phone itself, not on a computer.

### Step 8. Try it with a child
Hand over the phone. Say only: "Try it." Watch. Write down where they paused, where they laughed and what they tapped that did nothing. Ask:

1. Which part was the most fun?
2. Which part was confusing?
3. Would you play it again?

Ask a caregiver whether the directions explain themselves. Ask the teacher whether it matches the objective. A child's preference is useful feedback. It is not evidence that anyone read better.

### Step 9. Save it, then read it back
Save the phone page, the deck, the print file, the CSV and the scripts together. Then open each one again. Check every page. Write down what you could not save.

### Step 10. Share on purpose
Send it first to the person who asked. Do not post the teacher's original sheet unless you have permission. Your own new pages need a license you choose after rights are clear.

---

## NOTES FOR WHOEVER OPERATES THE AI (what went wrong, so it doesn't again)

- **A matching file size proves nothing.** Three copies of a PDF arrived at the right or nearly right size with damaged pages. Reading the text back caught it every time. Extraction can lag a few seconds after upload, so re-read before you decide it failed.
- **Prefer text.** Web pages, CSV files, scripts and Google Docs (made from HTML) copy over reliably. Binary files copied by hand do not. If a PDF must go up, upload once, read it back, and if a page is missing, upload again from the original.
- **Do not claim before you check.** "Saved" means read back. "Verified" means a script or a line-by-line table, not a glance.
- **Check the machine before you trust the picture.** Render pages, but also extract the text and diff it against the CSV.
- **Say what you could not do.** "Not created / not saved" is a useful sentence.

---

## SCORE IT THE SAME WAY EVERY TIME (so improvement is visible)

Rate 1 to 5 with one observation and one improvement each:

1. Source fidelity
2. Print or screen usability
3. Instructional usefulness
4. Teacher independence
5. Reproducibility
6. Rights and privacy
7. Visual delight (and, new in v2: **would a child play it again?**)

Version 1 baseline from the independent test: 4, 4, 3, **2**, 4, 3, 3.

## THE NEXT EXPERIMENT

Give Template v2 to a brand-new AI conversation with the same three source documents and no history. Ask it to build the Phone Quest. Score it on the seven criteria. If teacher independence rises above 2 and the fidelity check passes on the first try, the template is learning. Then hand the phone to a child.

---

SUCCESS MEANS: A child can play it. A parent can explain it. A teacher recognizes it. Another educator can make the next one.
