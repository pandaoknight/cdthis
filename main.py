#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
from optparse import OptionParser
#my libs
import envchecker
import cdthiscomposer
import color


def cdthis():
    opt = OptionParser("cdthis [options]... [name]")
    opt.add_option('-l', '--list', type='string', dest='path', default='.')
    opt.add_option('-a', '--listall', type='string', dest='path', default='.')
    opt.add_option('-f', '--force', type='string', dest='someth')
    opt.add_option('-d', '--delete', type='string', dest='someth')
    (options, args) = opt.parse_args()
    #print options
    #print args
    if 1 > len(args):
        print '[Fail] Name Not Provided'
        print 'Usage:'
        print '    cdthis[ -p <project path>][ -s <xyz>] name'
        print 'Ending ...'
        return
    name = args[0]

    if not projectchecker.check_php_project(options.path):
        print '[Fail] Please Check the Path'
        print 'Ending ...'
        return
    print ''
    filegen.gen_php_controller(options.path, name)
    filegen.gen_php_model(options.path, name)
    filegen.gen_php_tpl(options.path, name)

    print ''
    print color.INFO % 'Please put following code into InitRouter:'
    print '\t'+codegen.gen_php_router(name)
    print '[Success] Ending...'

if "__main__" == __name__:
    cdthis()
    pass
