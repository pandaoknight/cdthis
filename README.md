cdthis
======
还在为每次要进入到 / home / 你的大名 / workspace / svn / trunk / php / XX_project / smarty / templates / dest / 目录下面去编辑文件而烦恼么？
是时候用用cdthis了。
{git clone https://github.com/pandaoknight/cdthis.git
  python setup.py}
    安装完毕...
{cd /home/ .... /dest/ #你的目标文件夹
  cdthis #!!!}
    好了，一个名为cddest的alias已经在你当前的bash里生效了！已经生效了！
    快执行第一个“cddest”去跳转到你的“dest”目录吧！

问题来了
======
Linux跳转技术哪家强？GitHub找pandaoknight/cdthis。


++++个人吐槽板块
1. 所有的命令行提示都是英文的。。大家认真看吧，都是中国人XD
2. 尼玛，这个alias解决方案真是做得我吐血啊，python+Bash混合方案才弄出来。安装完后必须重启bash啊。不然我真没办法加入口啊。早知道用创建一个在PATH中文件夹，然后往里面塞cdXXX的方案来做，要稳定、简单、靠谱得多啊。