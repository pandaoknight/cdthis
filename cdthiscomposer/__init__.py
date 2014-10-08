#-*- coding:utf-8 -*-
import os


#Data
__all__ = ['apppend', 'remove', 'list', 'is_available']
cdthis_path = "~/.bashcdthis"

#Function
def append():
    pass

def remove():
    pass

def list():
    pass

def is_available():
    pass

# private function
def read():
    f = open(cdthis_path)
    while line = f.readline():
        print line
    f.close()

#Inline Test
def __test():
    read()

if '__main__' == __name__:
    __test()

