dirs3arch
=========

Current Release: v0.3.0 (2015.02.05)

![alt tag](http://4.bp.blogspot.com/-YF6eVa_2Yu0/VHFhKT2Ac9I/AAAAAAAAAFQ/YC6ouf1b8WM/s1600/d3.png)

Overview
--------
dirs3arch is a simple command line tool designed to brute force directories and files in websites.


Operating Systems supported
---------------------------
- Windows XP/7/8
- GNU/Linux
- MacOSX

Features
--------
- Multithreaded
- Keep alive connections
- Support for multiple extensions (-e|--extensions asp,php)
- Reporting (plain text, JSON)
- Detect not found web pages when 404 not found errors are masked (.htaccess, web.config, etc).
- Recursive brute forcing
- HTTP(S) proxy support

License
-------
Copyright (C) Mauro Soria (maurosoria at gmail dot com)

License: GNU General Public License, version 2

Changelog
---------
- 0.3.0 - 2015.02.05 Fixed issue3, fixed timeout exception, ported to Python3, other bugfixes
- 0.2.7 - 2014.11.21 Added Url List feature (-L). Changed output. Minor Fixes
- 0.2.6 - 2014.9.12 Fixed bug when dictionary size is greater than threads count. Fixed URL encoding bug (issue2).
- 0.2.5 - 2014.9.2 Shows Content-Length in output and reports, added default.conf file (for setting defaults) and report auto save feature added.
- 0.2.4 - 2014.7.17 Added Windows support, --scan-subdir|--scan-subdirs argument added, --exclude-subdir|--exclude-subdirs added, --header argument added, dirbuster dictionaries added, fixed some concurrency bugs, MVC refactoring
- 0.2.3 - 2014.7.7 Fixed some bugs, minor refactorings, exclude status switch, "pause/next directory" feature, changed help structure, expaded default dictionary
- 0.2.2 - 2014.7.2 Fixed some bugs, showing percentage of tested paths and added report generation feature
- 0.2.1 - 2014.5.1 Fixed some bugs and added recursive option
- 0.2.0 - 2014.1.31 Initial public release


