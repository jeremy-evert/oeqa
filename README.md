# oeqa

Community Anchors toolkit: turn one classroom worksheet into a phone-ready learning game, and test whether the written instructions let a different AI do it without help.

Worked example: **Roll and Read: R-Controlled Vowels and Tricky Words** (3rd grade).

## What is here

| Path | What it is |
|---|---|
| `docs/TEMPLATE_v2_Make_It_Phone_Ready.md` | Reusable brief, fidelity contract, master prompt, engagement rules, quality gate |
| `docs/TUTORIAL_v2_Roll_and_Read_Phone_Edition.md` | Worked example, what the v1 test found, notes for whoever runs the AI |
| `game/index.html` | **Phone game.** One file, no build step. Open on a phone, or serve with GitHub Pages |
| `dist/03_Roll_and_Read_Phone_Deck.pdf` | 9-page swipeable 9:16 PDF (read-and-say, real die) |
| `dist/01_*.pdf`, `dist/02_*.pdf` | US Letter print packets, Clean Classroom and Playful Adventure (v1 route) |
| `data/words.csv` | The 24-cell word table. Single source of truth |
| `tools/make_phone_pdf.py`, `tools/make_pdfs.py` | Build the PDFs from the word table (Python + reportlab) |
| `tools/verify.py` | Checks the word table, PDFs and game against the teacher's words and directions |
| `reports/v1_independent_test_summary.md` | Scores and findings from the independent AI test of v1 |

## Run it

    pip install reportlab
    python3 tools/make_phone_pdf.py data/words.csv dist/03_Roll_and_Read_Phone_Deck.pdf
    python3 tools/make_pdfs.py data/words.csv dist      # print packets
    python3 tools/verify.py                              # needs poppler's pdftotext

To try the game locally: `python3 -m http.server` and open `game/index.html` on your phone's browser (same network), or enable GitHub Pages on the repo.

## Status and cautions

- **Not yet tried by a child, caregiver or educator.** Treat everything as a first draft.
- Words and directions come from a teacher's one-page sheet. Everything added (letter tiles, letter-pair highlights, Word Detective, Silly Sentence Lab, the caregiver page) is tagged NEW and is **not teacher-reviewed**. No answer key exists.
- **Permission to republish the original sheet is not confirmed.** The word list and directions in `data/` and the files in `dist/` reproduce it. Keep this repository private, or confirm permission, before making it public.
- No student names, photos or handwriting are used anywhere. The game stores only a star count on the device.
- Fonts in the PDFs are standard Helvetica (not embedded). The game loads two Google Fonts and falls back to system fonts.

## License

Code and new text: BSD 2-Clause (see `LICENSE`). That does not cover the teacher's original sheet.
