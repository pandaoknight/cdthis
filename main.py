#!/usr/bin/python
#-*- coding:utf-8 -*-
import os
import sys
from optparse import OptionParser
#my libs
import color
import const_string
from composer import *

const_version = """    cdthis v0.1.0000
    %s
""" % const_string.copyleft  #TODO:[用户友好:version应该自动在发布egg的时候生成，才是对用户负责的]
const_usage = """cdthis [options]... [name]
Example:
    'cdthis sample' will generate a shortcut 'cdsample' to current working dir.
    'cdthis -l' will list all the shortcut now you have.""";

def cdthis():
    opt = OptionParser(const_usage)
    opt.add_option('-v', '--version', action="store_true", dest='version')
    opt.add_option('-f', '--force', action="store_true", dest='force', default=False)
    opt.add_option('-d', '--delete', type="string", dest='delete', default="")
    opt.add_option('-l', '--list', action="store_true", dest='list')
    opt.add_option('-a', '--listall', action="store_true", dest='listall')
    (options, args) = opt.parse_args()

    cp = Composer(const_string.cdthis_path);  #CLEAN:[良构:Composer依赖的路径是注入的，而不是配置]
    #TODO:[鲁棒性:有一些搭配是没有意义的，例如：d和f，所有的d现在都只是注释掉，而不是真正地删除。又例如l和a，因为a涵盖了l。现在只要你加了这个参数，它的逻辑就会被执行]
    cp._read()  #TODO:[良构:这种顺序执行还是耦合太紧]
    # 排它参数区 begin
    if options.version:
        print const_version;
        return True
    if options.list and not options.listall:
        print "[info]List..."
        cp.list()
        return True
    if options.listall:
        print "[info]List All..."
        cp.list()  #TODO:[功能:现在的-la和-l的效果是一样]
        return True
    # 排它参数区 end

    if options.delete:
        print "[info]Delete..."
        if cp.remove(options.delete):
            cp._write()
            #cp._source()
            with open(const_string.cdthis_gen_bash_path, 'w') as f:
                f.write(cp._unalias(options.delete))
            return True
        else:
            return False


    print "[info] Add new..."#TODO:[良构-可扩展:当所有分支都没有走到时，才认为做add()的模式，可扩展性不够好。]
    adding_name = args[0] if len(args) > 0 else os.getcwd().split('/')[-1]
    if cp.add(os.getcwd(), adding_name, options.force):
        cp._write()
        with open(const_string.cdthis_gen_bash_path, 'w') as f:
            f.write(cp._source())
        return True
    else:
        return False

if "__main__" == __name__:
    cdthis()
    pass
