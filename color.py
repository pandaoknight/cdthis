#!/usr/bin/python
# -*- coding:utf-8 -*-

RED    = '\033[1;31m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE   = '\033[1;34m'
PURPLE = '\033[1;35m'
CYAN   = '\033[1;36m'
GRAY   = '\033[1;37m'
WHITE  = '\033[1;38m'
RESET  = '\033[1;0m'


DEBUG     =  '%s'
INFO      =  GREEN + '%s' + RESET
WARNING   =  YELLOW + '%s' + RESET
ERROR     =  RED + '%s' + RESET
CRITICAL  =  RED + '%s' + RESET
EXCEPTION =  RED + '%s' + RESET
