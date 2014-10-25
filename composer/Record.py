#-*- coding:utf-8 -*-
import re
import string


tpl="""# createtime ${createtime}
alias cd${name}='cd ${target}'
"""
createtime_rep=r"^# createtime (?P<createtime>.+)$"
main_rep="^alias cd(?P<name>\S+)='cd (?P<target>\S+)'$"  #CLEAN:[可测性:拆分为两个正则而不是用一个，以便可以分开测试，也能更灵活地使用]

def parseText(text):
    pass

class Record:
    #Member
    __target = None;
    __name = None;
    __createtime = None;

    #Setter&Getter
    def setName(self, name):
        self.__name = name

    def setTarget(self, target):
        self.__target = target

    def setCreatetime(self, createtime):
        self.__createtime = createtime

    def getName(self):
        return self.__name

    def getTarget(self):
        return self.__target

    def getCreatetime(self):
        return self.__createtime

    #Method
    def parse(self, text):
        #参数text可以是多行的。
        matchobject = re.search(main_rep, text, flags=re.M)
        if not matchobject:
            return False
        cg = captured_groups = matchobject.groupdict();

        self.__target = cg['target'];
        self.__name = cg['name'];

        cmo = re.search(createtime_rep, text, flags=re.M)
        if cmo:
            ccg = createtime_captured_groups = cmo.groupdict();
            self.__createtime = ccg['createtime'];

        return True

    def toString(self):
        s = string.Template(tpl)
        s_done = s.substitute(target=self.__target, name=self.__name, createtime=self.__createtime)
        return s_done

#Inline Test
def __test():
    r = Record()
    print r.parse("text")
    print r.toString()

    r = Record()
    print r.parse("alias cdthis='cd ~/that'")
    print r.toString()

    r = Record()
    print r.parse('alias cdthis="cd ~/that"')  #双引号测试
    print r.toString()

    r = Record()
    print r.parse("alias cdthis='cd ~/that'\nalias cdthis='cd ~/that'")  #多行测试
    print r.toString()

    r = Record()
    print r.parse("# createtime 2014-10-24 15:50:58\nalias cdthis='cd ~/that'")
    print r.toString()

    r = Record()
    print r.parse("something jamming\n   \n# createtime 2014-10-24 15:50:58\nalias cdthis='cd ~/that'")  #带干扰的测试
    print r.toString()

if '__main__' == __name__:
    __test()
