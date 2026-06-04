@echo off
chcp 932 > nul
title knowledge_based_push

set "LOG=C:\kvba\knowledge-base\push.log"
cd /d "C:\kvba\knowledge-base"

echo === push START %DATE% %TIME% === > "%LOG%"

git remote remove origin 2>nul
git remote add origin https://github.com/ai-crafted-portfolio/knowledge-based.git >> "%LOG%" 2>&1
git branch -M main >> "%LOG%" 2>&1
git push -u origin main >> "%LOG%" 2>&1
set "RC=%errorlevel%"
echo push RC=%RC% >> "%LOG%"

echo === DONE %DATE% %TIME% === >> "%LOG%"
exit /b %RC%
