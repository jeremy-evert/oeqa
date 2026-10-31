# Lesson 00: Make the computer explain itself

**Time:** 5 minutes · **Needs:** a browser and any AI assistant · **Status:** written, untested with a learner
**Sources:** Build School's existing first lesson, per `sidecar/PLAN_2026-10-31_original.md` (to be re-verified)

## 1. The idea
Before you trust a computer command, find out what it does. An AI can explain a command to you in plain words without ever running it, and you can ask it how to check that explanation.

## 2. The tiny experiment
1. Open any AI assistant in your browser.
2. Copy this and send it:

> I'm learning how to use my computer. Explain the Windows PowerShell command `Get-Location` without running it. Tell me what it does, whether it changes anything, why it could be useful, and how I could check that your explanation is correct. Keep it simple.

3. Read the answer.

(On a Mac or Linux, you can swap in the command `pwd` and say "Terminal" instead of "Windows PowerShell".)

## 3. The safety check
- **Reads:** nothing. You are only chatting.
- **Changes:** nothing on your computer.
- **Stop:** close the tab.

## 4. The proof
Decide which of these your answer gave you. Tick each one you find.

- [ ] It said what the command does (it should say it shows the folder you are currently "in").
- [ ] It said whether the command changes anything (it should say **no**, it only shows information).
- [ ] It gave you a way to check it other than "trust me".

Now sort what you learned:
- **Demonstrated:** nothing yet. You have not run anything.
- **Claimed:** the AI's explanation.
- **Unverified:** whether the explanation is right.

*Optional, only if you already have a PowerShell window open:* type `Get-Location` and press Enter. It only prints the current folder. If it matches what the AI told you, the claim is now **demonstrated**. If you do not have a window open, skip this. The lesson is already complete.

## 5. The next doorway
Next, Lesson 01 ("Meet your computer") is on the roadmap but not written yet. You may stop here.

**Your win:** you have learned that you can ask the computer to explain itself before following instructions. No terminal access, installation or administrator rights were needed.

**One question for you:** What, if anything, confused you?
