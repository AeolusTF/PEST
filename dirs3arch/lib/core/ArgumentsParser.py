# -*- coding: utf-8 -*-
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Author: Mauro Soria



import configparser
from optparse import OptionParser, OptionGroup
from lib.utils.FileUtils import File
from lib.utils.FileUtils import FileUtils
from lib.utils.DefaultConfigParser import DefaultConfigParser
from thirdparty.oset import *
import os


class ArgumentsParser(object):

    def __init__(self, script_path):
        self.script_path = script_path
        self.parseConfig()
        options = self.parseArguments()
        if options.url == None:
            if options.urlList != None:
                with File(options.urlList) as urlList:
                    if not urlList.exists():
                        print("The file with URLs does not exist")
                        exit(0)
                    if not urlList.isValid():
                        print('The wordlist is invalid')
                        exit(0)
                    if not urlList.canRead():
                        print('The wordlist cannot be read')
                        exit(0)
                    self.urlList = list(urlList.getLines())
            elif options.url == None:
                print('Url target is missing')
                exit(0)
        else:
            self.urlList = [options.url]
        if options.extensions == None:
            print('No extension specified. You must specify at least one extension')
            exit(0)
        with File(options.wordlist) as wordlist:
            if not wordlist.exists():
                print('The wordlist file does not exist')
                exit(0)
            if not wordlist.isValid():
                print('The wordlist is invalid')
                exit(0)
            if not wordlist.canRead():
                print('The wordlist cannot be read')
                exit(0)
        if options.httpProxy is not None:
            if options.httpProxy.startswith('http://'):
                self.proxy = options.httpProxy
            else:
                self.proxy = 'http://{0}'.format(options.httpProxy)
        else:
            self.proxy = None
        if options.headers is not None:
            try:
                self.headers = dict((key.strip(), value.strip()) for (key, value) in (header.split(':', 1)
                                    for header in options.headers))
            except Exception as e:
                print('Invalid headers')
                exit(0)
        else:
            self.headers = {}
        
        self.extensions = list(oset([extension.strip() for extension in options.extensions.split(',')]))
        self.useragent = options.useragent
        self.cookie = options.cookie
        if options.threadsCount < 1:
            print('Threads number must be a number greater than zero')
            exit(0)
        self.threadsCount = options.threadsCount
        if options.excludeStatusCodes is not None:
            try:
                self.excludeStatusCodes = list(oset([int(excludeStatusCode.strip()) if excludeStatusCode else None for excludeStatusCode in
                                           options.excludeStatusCodes.split(',')]))
            except ValueError:
                self.excludeStatusCodes = []
        else: 
            self.excludeStatusCodes = []
        self.wordlist = options.wordlist
        self.lowercase = options.lowercase
        self.simpleOutputFile = options.simpleOutputFile
        self.plainTextOutputFile = options.plainTextOutputFile
        self.jsonOutputFile = options.jsonOutputFile
        self.timeout = options.timeout
        self.ip = options.ip
        self.maxRetries = options.maxRetries
        self.recursive = options.recursive
        if options.scanSubdirs is not None:
            self.scanSubdirs = list(oset([subdir.strip() for subdir in options.scanSubdirs.split(',')]))
            for i in range(len(self.scanSubdirs)):
                while self.scanSubdirs[i].startswith("/"):
                    self.scanSubdirs[i] = self.scanSubdirs[i][1:]
                while self.scanSubdirs[i].endswith("/"):
                    self.scanSubdirs[i] = self.scanSubdirs[i][:-1]
            self.scanSubdirs = list(oset([subdir + "/" for subdir in self.scanSubdirs]))
        else: self.scanSubdirs = None
        if not self.recursive and options.excludeSubdirs is not None:
            print('--exclude-subdir argument can only be used with -r|--recursive')
            exit(0)
        elif options.excludeSubdirs is not None:
            self.excludeSubdirs = list(oset([subdir.strip() for subdir in options.excludeSubdirs.split(',')]))
            for i in range(len(self.excludeSubdirs)):
                while self.excludeSubdirs[i].startswith("/"):
                    self.excludeSubdirs[i] = self.excludeSubdirs[i][1:]
                while self.excludeSubdirs[i].endswith("/"):
                    self.excludeSubdirs[i] = self.excludeSubdirs[i][:-1]
            self.excludeSubdirs = list(oset(self.excludeSubdirs))
        else:
            self.excludeSubdirs = None
        self.redirect = options.noFollowRedirects




    def parseConfig(self):
        config = DefaultConfigParser()
        configPath = FileUtils.buildPath(self.script_path, "default.conf")
        config.read(configPath)

        # General
        self.threadsCount = config.safe_getint("general", "threads", 10, list(range(1, 50)))
        self.excludeStatusCodes = config.safe_get("general", "exclude-status", None)
        self.redirect  = config.safe_getboolean("general", "follow-redirects", False)
        self.recursive = config.safe_getboolean("general", "recursive", False)
        self.testFailPath = config.safe_get("general", "test-fail-path", "youCannotBeHere7331").strip()
        # Reports
        self.autoSave = config.safe_getboolean("reports", "autosave-report", False)
        self.autoSaveFormat = config.safe_get("reports", "autosave-report-format", "plain", ["plain", "json", "simple"])
        # Dictionary
        self.wordlist = config.safe_get("dictionary", "wordlist", FileUtils.buildPath(self.script_path, "db", "dicc.txt"))
        self.lowercase = config.safe_getboolean("dictionary", "lowercase", False)
        # Connection
        self.useragent = config.safe_get("connection", "user-agent", None)
        self.timeout = config.safe_getint("connection", "timeout", 30)
        self.maxRetries = config.safe_getint("connection", "max-retries", 5)
        self.proxy = config.safe_get("connection", "http-proxy", None)



    def parseArguments(self):
        usage = 'Usage: %prog [-u|--url] target [-e|--extensions] extensions [options]'
        parser = OptionParser(usage)
        # Mandatory arguments
        mandatory = OptionGroup(parser, 'Mandatory')
        mandatory.add_option('-u', '--url', help='URL target', action='store', type='string', dest='url', default=None)
        mandatory.add_option('-L', '--url-list', help='URL list target', action='store', type='string', dest='urlList', default=None)
        mandatory.add_option('-e', '--extensions', help='Extension list separated by comma (Example: php,asp)',
                             action='store', dest='extensions', default=None)

        connection = OptionGroup(parser, 'Connection Settings')
        connection.add_option('--timeout', '--timeout', action='store', dest='timeout', type='int', default=self.timeout,
                              help='Connection timeout')
        connection.add_option('--ip', '--ip', action='store', dest='ip', default=None,
                              help='Resolve name to IP address')
        connection.add_option('--http-proxy', '--http-proxy', action='store', dest='httpProxy', type='string',
                              default=self.proxy, help='Http Proxy (example: localhost:8080')
        connection.add_option('--max-retries', '--max-retries', action='store', dest='maxRetries', type='int',
                              default=self.maxRetries)

        # Dictionary settings
        dictionary = OptionGroup(parser, 'Dictionary Settings')
        dictionary.add_option('-w', '--wordlist', action='store', dest='wordlist',
                              default=self.wordlist)
        dictionary.add_option('-l', '--lowercase', action='store_true', dest='lowercase', default=self.lowercase)

        # Optional Settings
        general = OptionGroup(parser, 'General Settings')
        general.add_option('-r', '--recursive', help='Bruteforce recursively', action='store_true', dest='recursive',
                           default=self.recursive)
        general.add_option('--scan-subdir', '--scan-subdirs', help='Scan subdirectories of the given -u|--url (separated by comma)', action='store', dest='scanSubdirs',
                           default=None)
        general.add_option('--exclude-subdir', '--exclude-subdirs', help='Exclude the following subdirectories during recursive scan (separated by comma)', action='store', dest='excludeSubdirs',
                           default=None)
        general.add_option('-t', '--threads', help='Number of Threads', action='store', type='int', dest='threadsCount'
                           , default=self.threadsCount)
        general.add_option('-x', '--exclude-status', help='Exclude status code, separated by comma (example: 301, 500)'
                           , action='store', dest='excludeStatusCodes', default=self.excludeStatusCodes)
        general.add_option('--cookie', '--cookie', action='store', type='string', dest='cookie', default=None)
        general.add_option('--user-agent', '--user-agent', action='store', type='string', dest='useragent',
                           default=self.useragent)
        general.add_option('--follow-redirects', '--follow-redirects', action='store_true', dest='noFollowRedirects'
                           , default=self.redirect)
        general.add_option('--header', '--header',
                    help='Headers to add (example: --header "Referer: example.com" --header "User-Agent: IE"',
                    action='append', type='string', dest='headers', default=None)

        reports = OptionGroup(parser, 'Reports')
        reports.add_option('--simple-report', '--simple-report', action='store', help="Only found paths", dest='simpleOutputFile', default=None)
        reports.add_option('--plain-text-report', '--plain-text-report', action='store', help="Found paths with status codes", dest='plainTextOutputFile', default=None)
        reports.add_option('--json-report', '--json-output', action='store', dest='jsonOutputFile', default=None)
        parser.add_option_group(mandatory)
        parser.add_option_group(dictionary)
        parser.add_option_group(general)
        parser.add_option_group(connection)
        parser.add_option_group(reports)
        options, arguments = parser.parse_args()
        return options

