#-*- coding:utf-8 -*-
import os


#Data
__all__ = ['issue_checker']

#Function
def issue_checker():
    return True

def issue_version():
    f = open("/etc/issue", "r")
    first_line = f.readline()
    f.close()

    return first_line


#Inline Test
def __test():
    issue_checker()
    print issue_version()

if '__main__' == __name__:
    __test()
