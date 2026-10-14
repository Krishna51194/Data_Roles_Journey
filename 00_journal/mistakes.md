# Mistakes log

| Date | Error | Cause | Fix |
|---|---|---|---|
| 2026-10-13 | "Get-Children is not recognized as the name of a cmdlet" | Typo in command name | Correct name: Get-ChildItem |
| 2026-10-13 | "Python was not found; run without arguments to install from the Microsoft Store" | Fake WindowsApps python.exe was first on PATH | Turned off Python (default) app execution aliases; opened a fresh terminal |
| 2026-10-13 | SyntaxError: invalid syntax | Used `:` instead of `;` between two commands in `python -c` | Use `;` to separate commands on one line |
| 2026-10-13 | ModuleNotFoundError: No module named 'rich' | Package was never installed in the active environment | `pip install rich` inside the activated venv |
| 2026-10-13 | fatal: unrecognized argument -- online | it is git log --oneline 