echo off
color a
cls
set ip=www.baidu.com
set qt=0
set ok=0
set of=0
set zj=0
set aa=0
echo off
color a
:a
cls
title  ���ӳɹ���%ok%��   ����ʧ�ܣ�%of%��   ��������%zj%��   δ֪����%qt%��
echo/
echo/  �ɹ���ʧ�ܡ�����δ֪,�����ۼ�200�����ϻ��Զ��رգ��ܼ�500�����ϻ��Զ��رգ�
echo/
echo/
echo/      ���ӳɹ���%ok%��
echo/
echo/      ����ʧ�ܣ�%of%��
echo/
echo/      ��������%zj%��
echo/
echo/      δ֪����%qt%��
echo/
echo/
echo/                 �ܼƣ�%aa%��
echo/
echo/
echo/
echo/   -���ؿͻ���-------^> %ip% ^<-------ָ������----С��-----
echo/                                       
if %ok% gtr 200 exit
if %of% gtr 200 exit
if %zj% gtr 200 exit
if %qt% gtr 200 exit
set/a aa+=1
ping %ip% -n 1 >nul
if %errorlevel% equ 1 (set/a of+=1 &goto a)
if %errorlevel% equ 0 (set/a ok+=1 &goto a)
if %errorlevel% lss 0 (set/a zj+=1 &goto a)
set/a qt+=1
goto a
