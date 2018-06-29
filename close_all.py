#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: <Zurdi>

import sys
import os
import psutil

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'lib'))

from lib_log_nbz import Logging
logger = Logging()


for process in psutil.process_iter():
    try:
        process_info = process.as_dict(attrs=['name', 'cmdline'])
        if process_info.get('name') in ('java', 'java.exe', 'Xvfb'):
            for cmd_info in process_info.get('cmdline'):
                if cmd_info == '-Dapp.name=browsermob-proxy' or cmd_info == ':99':
                    if process.ppid() == psutil.Process(os.getpid()).ppid() or psutil.Process(process.ppid()).ppid() == 1:
                        process.kill()
    except psutil.NoSuchProcess:
        pass

logs = ['geckodriver.log', 'bmp.log', 'server.log']
for log in logs:
    if os.path.isfile(os.path.join(os.getcwd(), log)):
        os.remove(os.path.join(os.getcwd(), log))