@Echo off&setlocal,EnableDelayedExpansion
title �ؼ�����ȡ��ͳ�ƴ�Ƶ
echo ���зִ���ؼ�����ȡ��ʱ�ϳ��������ĵȴ�����ɶȵ�100%%
Pause
python fenciqianzhi.py
echo �ִ���ϣ��ؼ��ʳ�ȡ���
:Choice
set /p Choice=�Ƿ���йؼ��ʴ�Ƶͳ�ƣ���ѡ��(Y/N):
IF /i "!Choice!"=="Y" Goto :Next
IF /i "!Choice!"=="N" Goto :End
Echo �������!Choice!���Ϸ������밴����������������롣
Pause>Nul&Goto :Choice
:Next
Echo ����ִ��...
python cipin.py
echo ��Ƶͳ����ϣ���������˳�
pause&exit
:End
Echo �˳�...&pause&exit
