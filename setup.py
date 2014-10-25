#!/usr/bin/python
#-*- coding:utf-8 -*-
#libs
import sys
import os
import re
from string import Template
from optparse import OptionParser
from datetime import datetime
#mylibs
import const_string  #TODO:[命名冲突][规范化]


tpl = """# Main entry for cdthis.
# cdthis is opensource software. ${cr}
if [ -f ${path} ]; then
    . ${path}
    fi
"""
tpl_done = Template(tpl).substitute(path = const_string.cdthis_path, cr = const_string.copyleft)

cdthis_alias_tpl = "alias cdthis='. %s %s'"
#project_root = os.path.realpath( os.path.join( os.getcwd(), os.path.dirname(__file__) ) )
project_root = os.path.realpath( os.path.dirname(__file__) )  #CLEAN:[无歧义:使用realpath可以稳定地获得绝对路径，然后用于生成脚本，保证执行可靠]
print project_root
cdthis_alias_tpl_done = cdthis_alias_tpl % ((project_root + "/cdthis"), project_root)

def checkEntryFile():
    with open(os.path.expanduser(const_string.entry_path)) as f:  #TODO:[实验:一个自己的支持with的类,支持__enter__和__exit__方法]
        all_text = f.read()
        if re.search(re.escape(tpl_done + cdthis_alias_tpl_done), all_text):
            return True;
        else:
            return False;

def appendEntry():
    with open(os.path.expanduser(const_string.entry_path), 'a') as f:  #TODO:[兼容:Mac上面默认是不会加载bashrc，却会加载bash_profile的]
        f.write("\n\n");  #TODO:[兼容]
        f.write(tpl_done + cdthis_alias_tpl_done);

def setup():
    if not checkEntryFile(): #如果已经存在入口，则不再向.bashrc append代码。
        print "[info] Entry not exists in %s, then append." % const_string.entry_path
        appendEntry()
        print "\033[1;32;40m"+"[IMPORTANT!!] To take EFFECT. Please restart your bash, or CLONE your session in terminal!"+"\033[0m" #TODO:[重构:改为使用coloram]
    else:
        print "[warn] Entry already exists in %s." % const_string.entry_path
    pass  #TODO:[待尝试的技术:增加日志或者控制台输出。]

def uninstall():
    with open(os.path.expanduser(const_string.entry_path), 'r') as f:
        all_text = f.read();
    re_obj = re.compile(re.escape(tpl_done + cdthis_alias_tpl_done))
    m = re_obj.search(all_text)
    if not m:
        return False
    # 如果匹配到可以运行的cdthis入口，则注释掉匹配的代码。然后回写到文件中。
    # group(0)的写法比"re.findall()然后取[0]"显得要不那么山寨些。
    commentted_matched = ("# cdthis setup.py -u Commentted at %s\n" % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  #TODO:[兼容:需要想办法兼容mac的\r]
    commentted_matched += re.sub("^", "#", m.group(0), flags=re.M)

    subbed_all_text = re_obj.sub(commentted_matched, all_text)  #TODO:[扩展性:扩展为非全段匹配，而是带有标识地匹配]
    with open(os.path.expanduser(const_string.entry_path), "w") as f:
        f.write(subbed_all_text)
    return True;

if "__main__" == __name__:
    opt = OptionParser("./setup.py [-u uninstall]")  #TODO:[用户友好-可读性:更好的Usage范本]
    opt.add_option('-u', '--uninstall', action="store_true", dest="uninstall", default=False)
    (options, args) = opt.parse_args()

    #CLEAN:[程序之道:把实现可逆的操作作为一个好习惯]
    if not options.uninstall:
        setup();
        print "[info] Setup finished!!";
    else:
        if uninstall():
            print "[info] Uninstall finished!!";
        else:
            print "[warn] Uninstall failed, no runnable entry already.";
    pass
