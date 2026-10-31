# Build School

**The smallest school that can grow.**

Build School teaches a complete beginner to build software with AI: ask a good question, check the answer, make a small change, prove it worked, and decide what to do next. It starts in a web browser with no installation and no programming.

> Start with curiosity. Build confidence through tiny successes. Add complexity only when it earns its place. Every lesson should produce a skill that makes the next lesson easier.

## Status: 0.1 draft (not yet tested with a learner)

| What | State |
|---|---|
| Lesson 00, "Make the computer explain itself" | Written. Has a markdown version and a one-file browser version. Untested with a learner. |
| Lesson 03, "Challenge the answer" | Draft, built on a real case from this repo's PDF project. Untested. |
| Lessons 01, 02, 04 to 20 | **Roadmap only.** Titles and goals are in `CURRICULUM.md`. They are not written. |
| Harvest from other repositories | A plan, not a done job. See `sidecar/source_harvest.md`. |
| Release 0.1 checklist | 0 of 7 complete. See `sidecar/RELEASE_0.1_CHECKLIST.md`. |

## Where to go

- **Learner:** open `START_HERE.md`, or open `lessons/00_start/index.html` in a browser.
- **Author:** read `CURRICULUM.md`, then `templates/LESSON_TEMPLATE.md`.
- **Reviewer:** read `sidecar/` (the original plan, harvest map and release checklist).

## Layout

    build_school/
    ├── README.md  START_HERE.md  CURRICULUM.md
    ├── lessons/
    │   ├── 00_start/               LESSON.md and index.html (browser version)
    │   └── 03_challenge_the_answer/LESSON.md
    ├── templates/LESSON_TEMPLATE.md
    ├── resources/                  prompt_cards.md, safety_card.md, glossary.md
    └── sidecar/                    plan, harvest map, release checklist, lesson inbox

## Rules every lesson follows

1. One idea, one tiny experiment, one visible win.
2. Observe and predict before changing anything.
3. Say what is **demonstrated**, what is **claimed**, and what is **unverified**.
4. Nothing needed from a private repository.
5. The learner may stop at any lesson and still keep what they learned.

## Credit and rights

Concepts are harvested from the author's other projects and rewritten from scratch. Each lesson lists its sources in a `Sources` line. Private material is excluded unless cleared. Code and new text in this repository: BSD 2-Clause (see the repo `LICENSE`).
