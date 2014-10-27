#-*- coding:utf-8 -*-
import os
import re
import datetime
#mylib
#import const_string
from Record import Record  #TODO:[命名:类的文件命名]

#Data
#__all__ = ['apppend', 'remove', 'list', 'is_available']
__all__ = ['Composer']

#Function

#Class
class Composer:
    #Member
    __path = None;  #TODO:[命名:成员变量的命名]
    __records_list = []
    __records_index_name = {}
    #__records_index_target = {}  #暂时不做复杂的按

    #Public Function
    def __init__(self, path):
        #def __init__(self, path=const_string.cdthis_path):  #CLEAN:[良构:这个Composer可以独立运行，而不需要依赖于const_string模块。const_string相当于是整个工程的配置。不应该被一个可以独立运行的模块引用]
        self.__path = path

    def add(self, target, name, force=False):
        #检查
        swap_out = self.__records_index_name.get(name, None)
        if swap_out:
            print "[warn] alias already exists: %s" % swap_out.toString()
            if not force:
                print "[fail] If you wanna override, please use 'cdthis -f'."
                return False;
            self.__records_list.remove(swap_out)

        r = Record();
        r.setName(name)
        r.setTarget(target)
        t = datetime.datetime.now()
        r.setCreatetime(t.strftime("%y-%m-%d %H:%M:%S"))
        self.__records_list.insert(0, r)
        self.__records_index_name[name] = r
        print "[OK] new alias done."
        return True
        pass

    def remove(self, name):
        removing = self.__records_index_name.get(name, None)
        if not removing:
            print "[fail] name:{%s} not exists." % name
            return False;

        self.__records_list.remove(removing)
        self.__records_index_name.pop(name)
        print "[OK] name:{%s} removed." % name
        return True
        pass

    def list(self):
        print "[info] All alias you have (sort by date, newer on top):"
        for r in self.__records_list:
            print "  %s\t=>  %s" % (r.getName(), r.getTarget())  #TODO:[涂装:用coloram上色 XD]
        pass

    def _read(self):
        #如果有重名，则以后面一个为准，因为实际上bash也是这么做的，后定义的alias会覆盖前面重名的。
        #with open(os.path.expanduser(self.__path), 'r') as f:
        with open(os.path.expanduser(self.__path), 'a+') as f:
            alltext = f.read()
            for matched in self._findall(alltext):
                r = Record()
                if r.parse(matched):
                    swap_out = self.__records_index_name.get(r.getName(), None)
                    if swap_out:
                        self.__records_list.remove(swap_out)

                    self.__records_index_name[r.getName()] = r;
                    self.__records_list.append(r)


    def _write(self):
        #输出的时候，重名的alias会被干掉。因为我的数据结构里面压根儿就不保存它了。
        with open(os.path.expanduser(self.__path), 'w') as f:
            for r in self.__records_list:
                f.write(r.toString())

    def _source(self):
        print "[Bash] source %s" % self.__path
        #os.system("bash -c 'source %s'" % self.__path)  #TODO:[REMOVE:在python起bash并设环境变量是没有意义的，因为][实验:os.popen异步管道]
        return "source %s" % self.__path

    #@classmethod
    @staticmethod
    def _unalias(name):
        print "[Bash] unalias cd%s" % name
        #os.system("bash -c 'unalias cd%s'" % name)  #TODO:[REMOVE:同上]
        #
        return "unalias cd%s" % name

    #Private Function
    def _findall(self, text):
        all_captured = re.findall(r"((^#.+$\n)*^alias.+$)", text, flags=re.M)
        return map(lambda x: x[0], all_captured)

#Inline Test
def __test_default():
    cp = Composer("/tmp/test_cdthis")
    cp.add(os.getcwd(), os.getcwd().split('/')[-1]);

def __test_findall():
    cp = Composer("/tmp/test_cdthis")
    print cp._findall("#aaa\n#bbb\nalias cd='~/something'\n#ccc\n#ddd\nalias cd='www'\n#eee\n#fff");
    print cp._findall("alias cd='~/something'\nalias cd='~/something'\nalias cd='~/something'\n");

def __test():
    tmp_path = "/tmp/test_cdthis"
    with open(tmp_path, 'w') as f:
        f.write("""
# createtime 2014-10-24 16:29:50
alias cdthis='cd ~/.that'
# createtime 2014-10-24 16:29:50
alias cdthat='cd ~/.this'

Jamming
#Jamming
# createtime 2014-10-24 16:29:50
#alias cdthis='cd Jamming'

#
alias cdnocreatetime='cd /no_createtime/'

# no createtime
alias cdnamedup='cd ~/first'
# no createtime
alias cdnamedup='cd ~/second'

# createtime 2014-10-24 16:29:50
alias cdother='cd ~/.where'
alias cdnocreatetime_again='cd /no_createtime/'

alias cdnamedup='cd ~/third'
""")
    cp = Composer(tmp_path)
    cp._read()
    cp.list()

    print "\nTest add:"
    cp.add("~/.new_added", "add");
    cp.list()

    print "\nTest add a duplicate name:"
    cp.add("~/.xxxxxxxxxxxx", "namedup");
    cp.list()

    print "\nTest add a duplicate name by force:"
    cp.add("~/.force_added", "namedup", force=True);
    cp.list()

    print "\nTest remove:"
    cp.remove("add");
    cp.list()

    print "\nTest remove again:"
    cp.remove("add");
    cp.list()

    print "\nTest unalias:"
    Composer._unalias('add')


if '__main__' == __name__:
    #__test_default()
    #__test_findall()
    __test()

