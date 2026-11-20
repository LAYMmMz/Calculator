# Calculator

A simple Python command-line calculator built for our **Version Control with Git** activity. The project uses separate feature branches and pull requests for the four basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with a check for division by zero)
- Input validation and an option to exit the program

## Project files

| File | Purpose |
| --- | --- |
| `calculator.py` | Main program and arithmetic functions |
| `test_calculator.py` | Unit tests for each operation and division by zero |
| `README.md` | Setup and Git activity instructions |
| `SCREENSHOT_GUIDE.md` | Steps for collecting original evidence from VS Code and GitHub |
| `.gitignore` | Excludes Python cache files |

## Requirements

- Python 3.9 or newer
- Git
- Visual Studio Code (optional, recommended for screenshots)
- GitHub account and repository access to push code

No third-party Python packages are required.

## Clone and run

Open a VS Code terminal (Terminal > New Terminal), then enter:

```powershell
git clone https://github.com/LAYMmMz/Calculator.git
cd Calculator
python calculator.py
```

On Windows, if `python` is unavailable, try `py calculator.py`.

## Test

```powershell
python -m unittest discover -v
```

## Git branches used

| Branch | Operation | Pull request |
| --- | --- | --- |
| `feature/addition` | `add(a, b)` | [#1](https://github.com/LAYMmMz/Calculator/pull/1) |
| `feature/subtraction` | `subtract(a, b)` | [#2](https://github.com/LAYMmMz/Calculator/pull/2) |
| `feature/multiplication` | `multiply(a, b)` | [#3](https://github.com/LAYMmMz/Calculator/pull/3) |
| `feature/division` | `divide(a, b)` | [#4](https://github.com/LAYMmMz/Calculator/pull/4) |

These operation branches were merged into `main` through separate pull requests. **Peer review is a distinct requirement:** real group members should review and approve their teammates' changes; the existing PR history should not be presented as evidence of peer approval unless such reviews are actually recorded.

## How we used Git

1. Created the shared `Calculator` repository.
2. Added the basic `calculator.py` menu.
3. Created a separate `feature/...` branch for each arithmetic operation.
4. Committed each function on its respective feature branch.
5. Opened one pull request per operation and merged into `main`.
6. Added tests, then pulled the completed `main` branch to run and check the calculator.

## Useful commands

```powershell
git branch -a
git log --oneline --graph --all --decorate
git status
git pull origin main
python -m unittest discover -v
python calculator.py
```

For the required screenshots, follow [SCREENSHOT_GUIDE.md](SCREENSHOT_GUIDE.md). Capture your **actual** VS Code terminal, GitHub PR pages, and test output. Do not use example screenshots as proof of commands you did not personally execute.

## Repository

https://github.com/LAYMmMz/Calculator
