:: authour: kym 
:: time: 2017-12-14
:: verison: 1.2
:: aimming to start the windows default  share  files.
:: ʹ��AD��ؽ������ͽű���ʱ����ʹ��authenticated users ��Ȩ��
@echo off
echo *********************************************************
echo �����޸�����ϵͳ,���Ե�Ƭ��!
echo *********************************************************
echo *********************************************************************** >> C:\Users\Public\start_share_result.txt 2>&1

echo ���ڿ������̹���...
echo %date% %time% ���������̹�������������£� >> C:\Users\Public\start_share_result.txt 2>&1

reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v "AutoShareServer" /t REG_DWORD /d "00000001" /f >> C:\Users\Public\start_share_result.txt 2>&1


echo ���ڿ����û�����...
echo %date% %time% ���������̹�������������£� >> C:\Users\Public\start_share_result.txt 2>&1
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v "AutoShareWks" /t REG_DWORD  /d "00000001" /f >> C:\Users\Public\start_share_result.txt 2>&1

echo %date% %time% �������û���������������£� >> C:\Users\Public\start_share_result.txt 2>&1
net share users=C:\Users >> C:\Users\Public\start_share_result.txt 2>&1

echo %date% %time% ��������ӡ��������������£� >> C:\Users\Public\start_share_result.txt 2>&1
net share print$=C:\Windows\System32\spool\drivers >> C:\Users\Public\start_share_result.txt 2>&1

echo *********************************************************
echo �޸���ɣ�����������!
echo *********************************************************
echo *********************************************************************** >> C:\Users\Public\start_share_result.txt 2>&1
:: del %0
pause