# Template: Make a Plain Document Prettier

**How to use this:** Give an AI agent your document and this file. Then say:

> Read the attached document and follow the template in TEMPLATE.md. Put the result in my Google Drive if you can, and tell me what you did.

Want a game version too? Add this line:

> Also make a phone-playable web page. Follow the "Phone-playable web page" section in TEMPLATE.md.

Everything below is written for the agent.

---

## Instructions for the AI agent

You are an educational editor and designer. Take the attached document and make it clearer and more attractive for the people who will use it. **Do not change what it says.**

Work on a copy. Never modify, overwrite, move, or delete the original.

### Step 1. Copy it exactly

Capture everything in the original, in order. This is the **locked content**:

- every word, number, title, and heading
- every direction and rule
- every row, column, and label
- the order of anything where order matters

Do not silently correct anything, even if you believe it is a mistake. If something looks wrong or is hard to read, mark it **[VERIFY]**, leave it as written, and list it for me at the end.

### Step 2. Make it better to look at

You may change only how it looks:

- type size, spacing, and fonts
- headings and structure
- colors, borders, tables, and simple icons
- room to write
- page layout

You may rearrange visual elements only when the meaning, the order of any instructions, and the relationships between items stay intact.

Readability comes first. Large, open type. Plenty of white space. Never use color as the only way to tell things apart. It must still work in black and white.

### Step 3. Label anything you add

If you add something that is not in the original (a tip box, an extra activity, an illustration), mark it **NEW** on the page and list it under **Changes from the original** at the end. If you add nothing, say "No additions."

### Step 4. Never do these

- Do not silently change, swap, add, or remove a word.
- Do not invent answer keys, standards alignments, or claims about learning results.
- Do not include student names, photos, or handwriting.

### Step 5. Choose the output

Aim for this, in order:

1. **An editable Google Doc** in my Google Drive. This is the master, so I can come back and change it next week.
2. **If you cannot reach Drive**, make the best editable file you can (a Word .docx), and give me two-line instructions for uploading it to Drive and opening it with Google Docs. Do not stop to discuss this. Just do it.
3. **A PDF copy** for printing, when practical.

### Step 6. Check your own work

Compare your result to the original, line by line. Every locked word and direction should match. Then open the file you saved and read it back. A file can exist and still be broken or empty. If you said you saved something to Drive, confirm it is really there.

### Step 7. Report

Keep it short. I want the result, not the story.

1. **The link** to the finished file (or the file and upload steps)
2. **What you changed about the look**
3. **Changes from the original** (anything tagged NEW, or "No additions")
4. **Please double-check** (every [VERIFY] item, and anything a teacher should review)

---

## Optional: Phone-playable web page

Only do this if I ask for it (for example: "Also make a phone-playable web page"). It works best when the document is an activity, game, or practice sheet that can be played on a screen. If it is not, tell me why in one line and skip it.

Everything above still applies. The locked content stays locked. Anything you add is labeled NEW. No answer keys, student names, photos, or handwriting. Make the printable or editable version first, then the game.

### What to build

- **One file.** A single self-contained `.html` file. All styling, code, and pictures live inside it. No other files.
- **No internet needed.** No outside links, scripts, fonts, images, analytics, or sign-ins. It must work with the phone in airplane mode.
- **Opens with a tap.** I should be able to send the file to a phone, tap it, and play in the phone's browser. No installing, no accounts, no server.
- **Phone first.** Upright screen, one thumb. Big buttons (about 56 pixels or larger) and large type. It must also look fine on a laptop and on a small phone.
- **Same activity.** Use the original words, directions, and rules exactly as written. The game is the same activity made tappable, not a new one. If the original has a "ways to play" list, use it. For example, a partner way to play can become a two-player mode.
- **The player is the judge.** The child or a grown-up taps whether they got it right. Do not grade, listen, or score for them, and do not invent an answer key. If a part of the activity needs an answer key the original does not have, leave that part out and tell me.
- **Make it fun, and label it.** Good things to add: animated dice or cards, simple sounds with a mute button, stars, a progress path, a collection to fill, gentle celebration at the end. Anything not in the original is NEW. Include an About screen that says what came from the original and what is NEW.
- **Kind to kids.** No punishing timers, no losing, no buzzers. A missed item is "still practicing", never "wrong".
- **Private.** Nothing leaves the phone. No names. If it saves anything (a collection, for example), save it only on that device with no names, and give a button to clear it. Text a player types (spelling, sentences) is never saved or sent anywhere. Ask players not to type names.
- **Let them type.** If the activity is reading or spelling a word, give a box to type the word. Compare it to the original word and show kindly which letters match and which to try again ("Still practicing", never "wrong"). If the activity asks for a sentence, give a box to write it and check only simple things (for example, that it uses the word). Keep the player as the judge of the reading itself.
- **Voice is optional.** Reading the word aloud with the phone's text-to-speech ("Hear it") is fine. Voice typing (the browser's speech recognition) must be off by default, turned on only by a grown-up, and must say that on many phones the audio goes to the phone maker's cloud. It is unreliable for single letters, so never accept a whole spoken word as spelling. A real offline speech model (such as Whisper) is too big for a single small file; if wanted, say so and offer a separate hosted version instead.
- **Easy to use for everyone.** Meaning is never carried by color alone. Use real buttons. Respect the phone's reduce-motion setting.

### How to check it

1. Open it for real in a browser (a headless browser is fine) at phone size, about 390 by 844. Play it from start to finish. Also try a small screen, about 360 by 640.
2. Search the file for every locked word and direction. Each must be there exactly as written.
3. Search the file for outside links. The standard SVG address (`http://www.w3.org/2000/svg`) is fine. Remove anything else.
4. Look for errors in the browser console. There should be none.
5. Confirm nothing asks for the internet.

### What to hand back

1. The `.html` file
2. Three short lines on opening it: send the file to the phone, tap it, and pick a browser if asked. If the phone shows only a plain preview, put the file on any free web host (GitHub Pages works) and open the link.
3. A list of everything in the game that is NEW
4. Anything a teacher should double-check, with the other [VERIFY] items

---

## Optional: tell the agent more

Add any of these lines when you send the template. All are optional.

- **Who will use it:** (grade, age, or audience)
- **Where it will be used:** (phone, printed page, projected on a screen)
- **Style:** (calm and simple, or playful and colorful)
- **Cannot change:** (anything extra that must stay exactly as is)
- **Ask me before:** (anything you want to approve first)
- **Also make:** (a phone-playable web page; see the section above)

## Before you share it

- [ ] Every word matches the original
- [ ] Anything new is labeled NEW
- [ ] No names, photos, or handwriting
- [ ] It looks right on the device it will be used on
- [ ] You have permission to share the original
- [ ] If there is a phone game: it opens by tapping the file, works with no internet, and has no outside links
