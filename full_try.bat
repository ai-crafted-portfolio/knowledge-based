@echo off
chcp 932 > nul
title knowledge_based_full_try
set "LOG=C:\kvba\knowledge-base\full_try.log"
cd /d "C:\kvba\knowledge-base"

echo === full try START %DATE% %TIME% === > "%LOG%"

echo --- check gh CLI --- >> "%LOG%"
where gh >> "%LOG%" 2>&1
echo gh check RC=%errorlevel% >> "%LOG%"

echo --- check git --- >> "%LOG%"
git --version >> "%LOG%" 2>&1

echo --- git init if needed --- >> "%LOG%"
if not exist .git (
    git init -b main >> "%LOG%" 2>&1
)
git config user.email "shuichisueyoshi@users.noreply.github.com" >> "%LOG%" 2>&1
git config user.name "shuichisueyoshi" >> "%LOG%" 2>&1

echo --- gitignore --- >> "%LOG%"
if not exist .gitignore (
    (echo site/
     echo .venv/
     echo __pycache__/
     echo *.log) > .gitignore
)

echo --- add + commit --- >> "%LOG%"
git add -A >> "%LOG%" 2>&1
git commit -m "feat: initial knowledge-based site" >> "%LOG%" 2>&1
echo commit RC=%errorlevel% >> "%LOG%"

echo --- try gh repo create --- >> "%LOG%"
gh repo create ai-crafted-portfolio/knowledge-based --public --source=. --push --remote=origin >> "%LOG%" 2>&1
set "RC_GH=%errorlevel%"
echo gh RC=%RC_GH% >> "%LOG%"

if %RC_GH% NEQ 0 (
    echo --- fallback: remote add + push --- >> "%LOG%"
    git remote remove origin 2>nul
    git remote add origin https://github.com/ai-crafted-portfolio/knowledge-based.git >> "%LOG%" 2>&1
    git branch -M main >> "%LOG%" 2>&1
    git push -u origin main >> "%LOG%" 2>&1
    set "RC_PUSH=%errorlevel%"
    echo push RC=%RC_PUSH% >> "%LOG%"
)

echo === DONE %DATE% %TIME% === >> "%LOG%"
type "%LOG%"
pause
