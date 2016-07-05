@Echo off&setlocal,EnableDelayedExpansion
title 关键词提取并统计词频
echo 进行分词与关键词提取耗时较长，请耐心等待至完成度到100%%
Pause
python fenciqianzhi.py
echo 分词完毕，关键词抽取完毕
:Choice
set /p Choice=是否进行关键词词频统计，请选择(Y/N):
IF /i "!Choice!"=="Y" Goto :Next
IF /i "!Choice!"=="N" Goto :End
Echo 您输入的!Choice!不合法！，请按任意键返回重新输入。
Pause>Nul&Goto :Choice
:Next
Echo 继续执行...
python cipin.py
echo 词频统计完毕，按任意键退出
pause&exit
:End
Echo 退出...&pause&exit
