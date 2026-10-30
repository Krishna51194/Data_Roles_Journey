# Mistakes log

| Date | Error | Cause | Fix |
|---|---|---|---|
| 2026-10-13 | "Get-Children is not recognized as the name of a cmdlet" | Typo in command name | Correct name: Get-ChildItem |
| 2026-10-13 | "Python was not found; run without arguments to install from the Microsoft Store" | Fake WindowsApps python.exe was first on PATH | Turned off Python (default) app execution aliases; opened a fresh terminal |
| 2026-10-13 | SyntaxError: invalid syntax | Used `:` instead of `;` between two commands in `python -c` | Use `;` to separate commands on one line |
| 2026-10-13 | ModuleNotFoundError: No module named 'rich' | Package was never installed in the active environment | `pip install rich` inside the activated venv |
| 2026-10-13 | fatal: unrecognized argument --online | Typo in option name | git log --oneline |
| 2026-10-29 | Quiz: thought int("12.5") gives 12 | int() on TEXT only accepts whole-number text; int(12.5) on a NUMBER truncates | Use float("12.5") for decimal text |
| 2026-10-29 | Quiz: thought text sorts numerically | Text compares character by character ("10" < "100" < "9") | Convert to int/float before sorting |