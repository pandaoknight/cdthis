#-*- coding:utf-8 -*-
import os
import re
import datetime
#from Record import Record  #TODO:[命名:类的文件命名]
from .Record import Record  # Python 3

#Data
#__all__ = ['apppend', 'remove', 'list', 'is_available']
__all__ = ['Composer']

#Class
class Composer:
    #Member
    __path = None;  #TODO:[命名:成员变量的命名]
    __records_list = []
    __records_index_name = {}

    #Public Function
    def __init__(self, path):
        self.__path = path

    def add(self, target, name, force=False):
        #检查
        swap_out = self.__records_index_name.get(name, None)
        if swap_out:
            print("[warn] alias already exists: {}".format(swap_out.toString()))
            if not force:
                print("[fail] If you wanna override, please use 'cdthis -f'.")
                return False
            self.__records_list.remove(swap_out)

        r = Record()
        r.setName(name)
        r.setTarget(target)
        t = datetime.datetime.now()
        r.setCreatetime(t.strftime("%y-%m-%d %H:%M:%S"))
        self.__records_list.insert(0, r)
        self.__records_index_name[name] = r
        print("[OK] new alias done.")
        return True

    def remove(self, name):
        removing = self.__records_index_name.get(name, None)
        if not removing:
            print("[fail] name:{{}} not exists.".format(name))
            return False

        self.__records_list.remove(removing)
        self.__records_index_name.pop(name)
        print("[OK] name:{{}} removed.".format(name))
        return True

    def list(self):
        print("[info] All alias you have (sort by date, newer on top):")
        for r in self.__records_list:
            print("  {}\t=>  {}".format(r.getName(), r.getTarget()))  #TODO:[涂装:用coloram 上色 XD]

    def _read(self):
        # print("[debug] _read path: ", open(os.path.expanduser(self.__path), 'a+'))
        #with open(os.path.expanduser(self.__path), 'a+') as f: # BUG FIXED
        open('/root/.bash_cdthis', 'a').close()
        with open(os.path.expanduser(self.__path), 'r') as f:
            alltext = f.read()
            # print("[debug] _read alltext: ", alltext)
            for matched in self._findall(alltext):
                r = Record()
                if r.parse(matched):
                    swap_out = self.__records_index_name.get(r.getName(), None)
                    if swap_out:
                        self.__records_list.remove(swap_out)

                    self.__records_index_name[r.getName()] = r
                    self.__records_list.append(r)
        # print("[debug] _read self.__records_list:", self.__records_list)

    def _write(self):
        with open(os.path.expanduser(self.__path), 'w') as f:
            for r in self.__records_list:
                f.write(r.toString())

    def _source(self):
        print("[Bash] source {}".format(self.__path))
        return "source {}".format(self.__path)

    @staticmethod
    def _unalias(name):
        print("[Bash] unalias cd{}".format(name))
        return "unalias cd{}".format(name)

    #Private Function
    def _findall(self, text):
        all_captured = re.findall(r"((^#.+$\n)*^alias.+$)", text, flags=re.M)
        # print("[debug] _findall all_captured:", all_captured)
        return list(map(lambda x: x[0], all_captured))

#Inline Test
def __test_default():
    cp = Composer("/tmp/test_cdthis")
    cp.add(os.getcwd(), os.getcwd().split('/')[-1])

def __test_findall():
    cp = Composer("/tmp/test_cdthis")
    print(cp._findall("#aaa\n#bbb\nalias cd='~/something'\n#ccc\n#ddd\nalias cd='www'\n#eee\n#fff"))
    print(cp._findall("alias cd='~/something'\nalias cd='~/something'\nalias cd='~/something'\n"))

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

    print("\nTest add:")
    cp.add("~/.new_added", "add")
    cp.list()

    print("\nTest add a duplicate name:")
    cp.add("~/.xxxxxxxxxxxx", "namedup")
    cp.list()

    print("\nTest add a duplicate name by force:")
    cp.add("~/.force_added", "namedup", force=True)
    cp.list()

    print("\nTest remove:")
    cp.remove("add")
    cp.list()

    print("\nTest remove again:")
    cp.remove("add")
    cp.list()

    print("\nTest unalias:")
    Composer._unalias('add')


if __name__ == '__main__':
    #__test_default()
    #__test_findall()
    __test()

