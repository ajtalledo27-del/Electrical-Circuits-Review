@echo off
REM One-time setup: run `gh auth login` and sign in as ajtalledo27-del
cd /d "%~dp0.."
git branch -M main
gh repo create ajtalledo27-del/Electrical-Circuits-Review --public --source=. --remote=origin --push --description "Electrical Circuits 1 (Part 1) DC Circuits offline reviewer and quiz bee"
if %ERRORLEVEL% EQU 0 (
  echo.
  echo Repo: https://github.com/ajtalledo27-del/Electrical-Circuits-Review
  echo.
  echo Enable GitHub Pages: Settings ^> Pages ^> Deploy from branch ^> main ^> / (root)
  echo Live site: https://ajtalledo27-del.github.io/Electrical-Circuits-Review/
) else (
  echo.
  echo Failed. Run these first:
  echo   gh auth login
  echo   (choose GitHub.com, HTTPS, login with browser as ajtalledo27-del)
  echo Then run this script again.
)
