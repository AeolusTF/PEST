:: Init Script for cmd.exe
:: Created as part of batch_scan
:: #########################################################################
:: 1 ��������״����иó��������ã�������--����--һ��--�û��ļ����ļ���(D:\appscan\result);��־�ļ����ļ���(D:\appscan\Logs)
:: 2 ��������״����иó��������ã�������--����--ɨ��ѡ��--ָʾɨ���Ƿ����(��ѡ)��ɨ��������Զ�����(��ѡ)
@REM 3 ��������״����иó��������ã�������--ɨ��--ɨ������--����--���Բ���--ѡ��ò��Ժ󵼳���D:\appscan\attack.scant 
@REM 4 �������32λϵͳ���뽫·��C:\Program Files (x86)\IBM\AppScan Standard ��Ϊ C:\Program Files\IBM\AppScan Standard

::@mode con cp select=936
@chcp 936
echo 1 ��������״����иó��������ã�������--����--һ��--�û��ļ����ļ���(D:\appscan\result);��־�ļ����ļ���(D:\appscan\Logs)
echo 2 ��������״����иó��������ã�������--����--ɨ��ѡ��--ָʾɨ���Ƿ����(��ѡ)��ɨ��������Զ�����(��ѡ)
echo 3 ��������״����иó��������ã�������--ɨ��--ɨ������--����--���Բ���--ѡ��ò��Ժ󵼳���D:\appscan\attack.scant 
echo 4 �������32λϵͳ���뽫·��C:\Program Files (x86)\IBM\AppScan Standard ��Ϊ C:\Program Files\IBM\AppScan Standard
echo 5 �ڵ�ǰĿ¼��ÿ��urltoscan�ļ��У��ֱ𱣴�3��URl����Ϊ�������Է��֣�ͬʱ��������ɨ�������ܺ�Ч����ߵġ�
@echo off
@REM delete the script created by the last time
::@DEL urltoscan*.bat

@REM change to the path where AppScan was installed
@echo @cd /d C:\Program Files (x86)\IBM\AppScan Standard > urltoscan0.bat
@echo @cd /d C:\Program Files (x86)\IBM\AppScan Standard > urltoscan1.bat
@echo @cd /d C:\Program Files (x86)\IBM\AppScan Standard > urltoscan2.bat

@REM produce batch_scan for appscancm 
::for /F "delims=/,tokens=3" %%f in (urltoscan.txt) do echo %%f >> urltoname.txt


::��ÿ��urltoscan�ļ��У�����3��URl����Ϊ�������Է��֣�ͬʱ��������ɨ�������ܺ�Ч����ߵġ�
for /F %%u in (urltoscan0.txt) do echo appscancmd /e /su %%u /st D:\appscan\attack.scant /d D:\appscan\result\ /v >> urltoscan0.bat
for /F %%u in (urltoscan1.txt) do echo appscancmd /e /su %%u /st D:\appscan\attack.scant /d D:\appscan\result\ /v >> urltoscan1.bat
for /F %%u in (urltoscan2.txt) do echo appscancmd /e /su %%u /st D:\appscan\attack.scant /d D:\appscan\result\ /v >> urltoscan2.bat

echo "������ɣ�����������ɨ��ִ��" 
echo "�������������Եȣ�"
echo "���ڵ�ǰĿ¼�·ֱ���urltoscan1.bat��urltoscan2.bat"

urltoscan0.bat

pause









