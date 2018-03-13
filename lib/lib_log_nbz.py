#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: <Zurdi>


class Logging:

    def __init__(self):
        pass

    @staticmethod
    def log(level, msg):
        if level == 'NOTE':
            print("\033[92m" + '  - NBZ Log' + ': ' + "\033[0m" + msg)
        elif level == 'ERROR':
            print("\033[91m" + '  - NBZ Error' + ': ' + "\033[0m" + msg)
        else:
            print('Not defined logger level: ' + str(level))
