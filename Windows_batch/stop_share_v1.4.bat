:: authour: kym 
:: time: 2018-1-15
:: verison: 1.4
:: aimming to close the windows default  share  files on silence
@echo off
@echo *********************************************************************** >> C:\Users\Public\stop_share_result.txt 2>&1

:: echo *********************************************************
:: echo �����޸�����ϵͳ,���Ե�Ƭ��!
:: echo *********************************************************
:: echo ���ڹرմ��̹���...
@echo %date% %time% ���رմ��̹�������������£� >> C:\Users\Public\stop_share_result.txt 2>&1
@reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v "AutoShareServer" /t REG_DWORD /d "00000000" /f >> C:\Users\Public\stop_share_result.txt 2>&1

:: echo ���ڹر�ϵͳ����...
@echo %date% %time% ���ر�ϵͳ��������������£� >> C:\Users\Public\stop_share_result.txt 2>&1
@reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" /v "AutoShareWks" /t REG_DWORD  /d "00000000" /f >> C:\Users\Public\stop_share_result.txt 2>&1

@echo %date% %time% ���ر��û���������������£� >> C:\Users\Public\stop_share_result.txt 2>&1
@reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Shares" /v "Users"  /f >> C:\Users\Public\stop_share_result.txt 2>&1
@reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Shares\Security" /v "Users"  /f >> C:\Users\Public\stop_share_result.txt 2>&1

@echo %date% %time% ���رմ�ӡ��������������£� >> C:\Users\Public\stop_share_result.txt 2>&1
@reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Shares" /v "print$"  /f >> C:\Users\Public\stop_share_result.txt 2>&1
@reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\LanmanServer\Shares\Security" /v "print$" /f >> C:\Users\Public\stop_share_result.txt 2>&1


:: echo *********************************************************
:: echo �޸���ɣ�����������!
:: echo *********************************************************
@echo *********************************************************************** >> C:\Users\Public\stop_share_result.txt 2>&1
:: del %0
exit