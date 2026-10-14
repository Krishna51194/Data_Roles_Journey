# Cheat cards

## W1 L1: Virtual environments (venv)
- venv = a separate Python toolbox for one project; packages installed there stay there.
- Create: `python -m venv .venv`   Activate: `.venv\Scripts\Activate.ps1`   Off: `deactivate`
- Activating puts .venv\Scripts at the FRONT of PATH; Windows runs the FIRST match.
- Check which Python is running: `Get-Command python`; list packages: `pip list`
- Why: isolation (projects can't break each other) + reproducibility (rebuild from requirements.txt).