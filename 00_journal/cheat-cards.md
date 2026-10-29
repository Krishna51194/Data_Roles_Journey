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

## W2 L1: Values and types
- Types: int (45), float (129.99), str ("Delta"), bool (True/False), None (missing). Check with type(x).
- Convert explicitly: int("120"), float("180.50"), str(45). Python won't mix text and numbers for you.
- "120" + "5" = "1205" (joins text!) · 10 / 2 = 5.0 (always float) · 10 // 4 = 2 · True + True = 2
- TypeError = wrong type for the operation ("120" + 5). ValueError = right type, bad content (int("Delta")).
- Debugger: click left of a line number = breakpoint → F5 start → F10 step → watch the Variables panel. Yellow line = runs NEXT.

## W2 L2: Strings
- Index from 0; negative from the end: code[0] = "D", code[-1] = "7". Slice [start:stop], stop NOT included.
- Shortcuts: code[:2] = first 2 · code[2:] = from 2 to end · date[-2:] = last 2. Slicing is forgiving; indexing out of range = IndexError.
- Cleaning: .strip() .upper() .lower() .title() (.capitalize() = first letter only) .replace("$", "") .split(",") len(x)
- Strings are IMMUTABLE: methods return a new copy → always save it: name = name.strip()
- split = separator-based (CSV, routes; removes the separator) · slice = position-based (codes, dates)
- f"Flight {code} costs ${price}" · Text compares char by char: "999" > "1287" → convert to int before sorting/maths

## W2 L3: Lists
- List = ordered, MUTABLE collection: delays = [45, 5, 120]. Index/slice exactly like strings ([0], [-1], [1:3], [1:-1]).
- Change in place (return None, so DON'T assign): .append(x) .remove(x) .sort() .sort(reverse=True). .pop() removes the last item and returns it.
- New copy (DO assign): sorted(lst), sorted(lst, reverse=True). Top 3 biggest: sorted(lst, reverse=True)[:3]
- Ask the list: len() sum() max() min(), round(x, 1), `x in lst` → True/False
- Strings immutable → must assign (s = s.strip()). Lists mutable → must NOT assign (lst.sort()). "'NoneType' has no ..." → you stored a None.
- Text numbers sort wrong ('1287' < '45' < '999'). Convert to int/float before sorting or maths. Check output vs expected, line by line.