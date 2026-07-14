@echo off
cd /d "%~dp0.."
git branch -M main
gh repo create ajtalledo27-del/Electrical-Circuits-Review --public --source=. --remote=origin --push --description "Electrical Circuits 1 reviewer with formula bank, lecture text and quiz bee"
if %ERRORLEVEL% EQU 0 (
  echo Repo: https://github.com/ajtalledo27-del/Electrical-Circuits-Review
  echo Live: https://ajtalledo27-del.github.io/Electrical-Circuits-Review/
) else (
  echo If repo exists, run: git push -u origin main
)
