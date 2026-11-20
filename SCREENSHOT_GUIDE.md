# Screenshot Guide (Steps 2–9)

Take these screenshots from **your own VS Code terminal and GitHub browser**. The commands below are real commands; the exact output, username, commit hashes, timestamps, and paths will depend on your computer. Do not alter screenshots or use generated screenshots to claim actions you did not perform.

## Step 2 — Repository creation
Open https://github.com/LAYMmMz/Calculator and screenshot the repository title and URL. The repository already exists, so do not create a duplicate.

## Step 3 — Clone the repository
Open **VS Code > Terminal > New Terminal**, navigate to the folder you want to work in, then run:

```powershell
git clone https://github.com/LAYMmMz/Calculator.git
cd Calculator
git remote -v
```

Screenshot the terminal after a successful clone and remote verification. If you already have a local `Calculator` folder, use another parent folder or skip cloning and run `git pull origin main` inside the existing clone.

## Step 4 — Project structure

```powershell
code .
git status
dir
```

Screenshot VS Code Explorer showing `calculator.py`, `test_calculator.py`, and `README.md`. Screenshot the terminal directory listing.

## Step 5 — Basic calculator code
Open `calculator.py` in VS Code, and screenshot the code with the main menu and function definitions visible.

## Step 6 — Branch and make a genuine new commit
The four arithmetic branches were already merged into `main`. **Do not rewrite their history.** To demonstrate a new branch, create a small documentation change and push it yourself:

```powershell
git switch main
git pull origin main
git switch -c docs/class-activity-notes
"Activity checked using VS Code." | Add-Content activity-notes.txt
git add activity-notes.txt
git commit -m "Add class activity notes"
git branch --show-current
git log -1 --oneline
```

The `Add-Content` line is for a **PowerShell terminal on Windows**. For Command Prompt, use `echo Activity checked using VS Code.>>activity-notes.txt`. Screenshot the actual branch name, successful commit, and output. If `git commit` asks for your identity, configure your real name and email in Git, then rerun it.

## Step 7 — Push to GitHub

```powershell
git push -u origin docs/class-activity-notes
git status
```

Screenshot the VS Code terminal after the successful push. This is genuine, fresh proof of a push from your machine. If you cannot push, ensure you are logged in and have collaborator access.

## Step 8 — Pull request, review, and merge
Go to https://github.com/LAYMmMz/Calculator/pulls and click **New pull request**, selecting `docs/class-activity-notes` into `main`. Write a short description, create the PR, and screenshot it. Ask **another group member** to review and approve the PR using **Files changed > Review changes > Approve** (reviewers generally cannot approve their own PRs). Screenshot the recorded approval, then merge and screenshot the merged status.

Existing arithmetic PRs for the activity:
- https://github.com/LAYMmMz/Calculator/pull/1
- https://github.com/LAYMmMz/Calculator/pull/2
- https://github.com/LAYMmMz/Calculator/pull/3
- https://github.com/LAYMmMz/Calculator/pull/4

These were already merged; don't claim that someone else approved them unless GitHub actually shows the approval.

## Step 9 — Pull and test merged changes
Once your documentation PR is merged:

```powershell
git switch main
git pull origin main
python -m unittest discover -v
python calculator.py
```

Try the menu options with test inputs:
- Addition: 8 and 2 → 10
- Subtraction: 8 and 2 → 6
- Multiplication: 8 and 2 → 16
- Division: 8 and 2 → 4
- Division by zero: 8 and 0 → error message (not a crash)

Screenshot the actual terminal test summary and one or more live calculator examples.

## Submission checklist
- Repository URL visible
- Clone and Git remotes terminal screenshot
- Project structure screenshot
- Calculator code screenshot
- Feature branch and commit evidence screenshot
- Successful push screenshot
- GitHub pull request screenshot
- **Actual** peer approval and merged PR screenshot
- Pull, unit test, and calculator output screenshot

Screenshots are evidence of your own activity; they should reflect actual operations, not a simulated history.
