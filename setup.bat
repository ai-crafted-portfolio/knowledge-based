@echo off
chcp 932 > nul
title knowledge_based_setup

set "LOG=C:\kvba\knowledge-base\setup.log"
cd /d "C:\kvba\knowledge-base"

echo === knowledge-based repo setup START %DATE% %TIME% === > "%LOG%"

REM gh CLI 確認
where gh >nul 2>&1
if errorlevel 1 (
    echo [ERROR] gh CLI not found. Install: winget install GitHub.cli >> "%LOG%"
    echo === ABORT === >> "%LOG%"
    exit /b 1
)

REM git init
if not exist .git (
    git init -b main >> "%LOG%" 2>&1
)
git config user.email "shuichisueyoshi@users.noreply.github.com" >> "%LOG%" 2>&1
git config user.name "shuichisueyoshi" >> "%LOG%" 2>&1

REM .gitignore 作成
if not exist .gitignore (
    echo site/ > .gitignore
    echo .venv/ >> .gitignore
    echo __pycache__/ >> .gitignore
    echo *.log >> .gitignore
)

git add . >> "%LOG%" 2>&1
git commit -m "feat: initial Microsoft Learn / Oracle Support style knowledge base" >> "%LOG%" 2>&1
echo commit RC=%errorlevel% >> "%LOG%"

REM GitHub repo 作成 + 初回 push (gh CLI authenticated 必要)
gh repo create ai-crafted-portfolio/knowledge-based --public --source=. --push --remote=origin >> "%LOG%" 2>&1
set "RC_CREATE=%errorlevel%"
echo gh repo create RC=%RC_CREATE% >> "%LOG%"

if %RC_CREATE% NEQ 0 (
    REM 既に repo 存在の場合 = remote add + push 試行
    git remote add origin https://github.com/ai-crafted-portfolio/knowledge-based.git >> "%LOG%" 2>&1
    git push -u origin main >> "%LOG%" 2>&1
    echo push RC=%errorlevel% >> "%LOG%"
)

echo === DONE %DATE% %TIME% === >> "%LOG%"
type "%LOG%"
pause
exit /b 0
