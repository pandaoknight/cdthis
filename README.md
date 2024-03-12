cdthis
======
Linux跳转技术哪家强？GitHub找pandaoknight/cdthis。
-------
还在为每次要进入到 / home / 你的大名 / workspace / svn / trunk / php / XX_project / smarty / templates / dest / 目录下面去编辑文件而烦恼么？<br/>
是时候用用cdthis了。<br/>
{git clone https://github.com/pandaoknight/cdthis.git  <br/>
&nbsp;&nbsp;&nbsp;&nbsp;python setup.py}  <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;安装完毕...  <br/>
{cd /home/ .... /dest/ #你的目标文件夹  <br/>
&nbsp;&nbsp;&nbsp;&nbsp;cdthis } <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;执行完毕!<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;好了，一个名为cddest的alias已经在你当前的bash里生效了！已经生效了！<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;快执行第一个“cddest”去跳转到你的“dest”目录吧！<br/>
<br/>
<br/>
<br/>

##### 个人未来改进
1. 这个alias解决方案真是难做，python+Bash混合方案才弄出来。安装完后必须重启bash啊。不然我真没办法加入口啊。早知道用创建一个在PATH中文件夹，然后往里面塞cdXXX的方案来做，要稳定、简单、靠谱得多啊。
2. 我最近在很多机器上使用nfs来同步代码。这需要一个新功能就是不在依赖
3. 我之所以用alias的方案，是因为alias天生可以提供 bash completion，那么我们现在知道有更好的办法实现，参考K8s：
```
  # Installing bash completion on Linux
  ## If bash-completion is not installed on Linux, install the 'bash-completion' package
  ## via your distribution's package manager.
  ## Load the kubectl completion code for bash into the current shell
  source <(kubectl completion bash)
  ## Write bash completion code to a file and source it from .bash_profile
  kubectl completion bash > ~/.kube/completion.bash.inc
```

4. 会考虑简化python的代码，兼容python2.7和python3.11
5. 会考虑转写为golang
