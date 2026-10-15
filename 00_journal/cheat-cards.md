# Cheat cards

## W1 L1: Virtual environments (venv)
- venv = a separate Python toolbox for one project; packages installed there stay there.
- Create: `python -m venv .venv`   Activate: `.venv\Scripts\Activate.ps1`   Off: `deactivate`
- Activating puts .venv\Scripts at the FRONT of PATH; Windows runs the FIRST match.
- Check which Python is running: `Get-Command python`; list packages: `pip list`
- Why: isolation (projects can't break each other) + reproducibility (rebuild from requirements.txt).

## W1 L1: Git basics
- Commit = a save point (snapshot + message) on MY computer. Push = send commits to GitHub.
- Loop: `git status` → `git add <file>` or `git add .` → `git commit -m "Verb what changed"` → `git push`
- States: untracked (new) → modified (changed) → staged (in the box) → committed (saved).
- `git log --oneline` = history; `git remote -v` = where pushes go. Git ignores empty folders.
- .gitignore = files Git must never save (e.g. .venv). Never push secrets or venvs.

## W1 L2: Terminal navigation
- `Get-Location` (pwd) = where am I; `ls` = what's here; `cd <folder>` = go in; `cd ..` = up one level
- Absolute path = full address (G:\...), works from anywhere. Relative = from where I stand (02_sql, ..\02_sql)
- Tab = autocomplete names (no typos); Up arrow = previous commands; Esc = clear line
- "Cannot find path ... does not exist" → check Get-Location, then ls
- In code: relative paths resolve from the working directory, not the script → use Path(__file__).parent