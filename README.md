# Make a plain document prettier with AI

## Try it now (about 5 minutes)

1. Open any AI assistant (Claude, ChatGPT, Gemini).
2. Attach your plain PDF or Word document.
3. Copy the box below, paste it, and send.

> Please redesign the attached educational document so it is more attractive, readable, and easy to use.
>
> Rules:
> - Keep every word, number, direction, and rule exactly as written. Do not fix anything silently. If you think something is a mistake, list it for me at the end and leave it alone.
> - Change only the look: type size, spacing, headings, layout, color, tables. Never rely on color alone, so it still works in black and white.
> - Label anything you add as NEW, and list every addition at the end.
> - No student names, photos, or handwriting.
>
> Make an editable Google Doc in my Google Drive if you can. If you cannot reach Drive, give me a Word file to download and tell me how to upload it. A PDF copy for printing is a nice extra.
>
> When you finish, compare your result to the original line by line, open the file you saved to make sure it works, then tell me what you changed and what I should double-check.

That's it. You should get back a finished document and a short list of things to check.

## Want more?

| File | What it is |
|---|---|
| [`TEMPLATE.md`](TEMPLATE.md) | The longer, more careful version of the prompt above. Attach it alongside your document for stricter results. |
| [`TIPS_AND_TRICKS.md`](TIPS_AND_TRICKS.md) | Plain-language advice for working with AI. No coding. |
| [`examples/final/`](examples/final/) | Three finished PDFs made from a plain one-page worksheet, plus a playable phone game made from the same sheet, to show what is possible. |
| [`04_Roll_and_Read_Phone_Game.html`](examples/final/04_Roll_and_Read_Phone_Game.html) | The phone game. One file. Open it in a phone's web browser and play. |

## Bonus: turn it into a phone game

If your document is really an activity (a dice game, a word list, a practice sheet), the AI can also build a small game from it that opens on a phone. The example in `examples/final/` does this for the Roll and Read worksheet. It is a single file. There is nothing to install, no account, and no internet needed once the file is on the phone. It keeps every word and direction exactly as written, labels everything it adds as NEW, and collects nothing. The player can type the word they read to check their spelling, and can type a sentence using the word. Typed spelling and sentences stay on the phone, are never saved or sent anywhere, and the page asks players not to type names. A microphone button is there too, but it starts off and a grown-up has to turn it on. On many phones, voice typing sends audio to the phone maker's cloud service, so it is optional.

To get one for your own document, add this line when you send the template:

> Also make a phone-playable web page. Follow the "Phone-playable web page" section in TEMPLATE.md.

To try the example, download `04_Roll_and_Read_Phone_Game.html`, send it to a phone, and open it in the phone's browser. (GitHub only shows the file as code. Use "Download raw file" first.) If your phone shows a plain preview instead of the game, put the file on any free web host, such as GitHub Pages, and open the link.

## Even better: have the agent publish it for you

The agent can also put the game on the web, so your phone only needs a link. This is how the live example was posted. The agent drove my own signed-in Chrome browser to create a new public GitHub repository, pushed the game into it, and switched on GitHub Pages. I only said what I wanted. It needs a Claude session with the Claude in Chrome extension connected to a Chrome that is signed in to GitHub.

**Play the live example on a phone:** https://jeremy-evert.github.io/oeqa_spell_roller_public/ (source: https://github.com/jeremy-evert/oeqa_spell_roller_public)

To get your own, add this line when you send the template:

> Also post the phone game on GitHub Pages. Create a new public repository for it, push the single HTML file as `index.html`, turn on Pages for the `main` branch, and give me the link. Ask me before you create anything.

Notes:
- The repository is public, so anyone with the link can play. Do not put names or student work in it.
- A link on the web (https) lets the phone remember microphone permission, so voice asks only once.
- If the agent cannot reach your browser, you can do the same by hand: new repository, upload `index.html`, then Settings, Pages, branch `main`, Save.

## License

BSD 2-Clause. See [`LICENSE`](LICENSE).
