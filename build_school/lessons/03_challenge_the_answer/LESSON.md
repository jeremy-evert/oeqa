# Lesson 03: Challenge the answer

**Time:** 15 minutes · **Needs:** this page only · **Status:** draft, untested with a learner
**Sources:** a real case from this repository's PDF project (the v1 test, `reports/v1_independent_test_summary.md`). The facts below come from that session's log, not from a re-run.

## 1. The idea
An AI, a website or a tool can say "done" and be wrong. Often the first sign is a number that looks right. Your job is to find one claim that needs evidence, then go and get it.

## 2. The tiny experiment: three uploads
An AI was asked to save a 5-page PDF to Google Drive. The file it had made was **15,695 bytes** (A), and a second PDF was **18,496 bytes** (B). It uploaded copies and reported what happened:

| Upload | What the tool reported | What the AI could have said |
|---|---|---|
| A, first copy | File saved, **15,697 bytes** | "Saved. Size is about right." |
| A, second copy | File saved, **16,139 bytes** | "Saved." |
| B, first copy | File saved, **18,496 bytes**, exactly the right size | "Saved. The size matches exactly, so it is correct." |

Your task: for each row, write one of these:
- **Demonstrated** (we saw the file's pages and they were right)
- **Claimed** (something said it was saved, nothing checked the contents)
- **Unverified** (no check at all)

Then answer: **which row is the most dangerous to believe, and why?**

## 3. The safety check
- **Reads:** nothing on your computer.
- **Changes:** nothing.
- **Stop:** close the page.

## 4. The proof
Answers are below. Try first.

<details>
<summary>Show the answers</summary>

All three rows are **Claimed**. A size is a number the tool reports. It is not the pages themselves.

The AI then did one extra thing: it asked Drive to **read the text back out of each file**, and compared it with what it meant to save. That check found:
- A, first copy: damaged (a broken internal table). Size was off by 2 bytes.
- A, second copy: a piece of the other file had been spliced in.
- B, first copy: **the size matched exactly, but page 3 was missing from the text.** The copy had been damaged while keeping the same length.

The most dangerous row is **B's first copy**, because the number everyone would check looked perfect. The only thing that caught it was reading the contents.

Lesson: **checking the size is checking the label on the box. Reading the contents is opening the box.**

The AI moved the bad copies to the Trash and uploaded again until the read-back showed all five pages.
</details>

## 5. The next doorway
Next: Lesson 04, "Read the evidence", on the roadmap (not written). You may stop here.

**Your win:** you can point at one claim and say what evidence would turn it from claimed into demonstrated.

**One question for you:** Did the answers surprise you? Which one?
