nrm教程
================

如果你还像以前切换npm镜像那你也太low了，现在告诉你一个很拽的方式，通过cli切换不同的镜像源 


.. toctree::
    :maxdepth: 2
    :numbered: 2


nrm安装
-------
打开命令窗口

安装::

    npm install -g nrm 

nrm镜像管理工具常用命令
----------------------
常用命令集::

    // 查看镜像列表
    nrm 

    // 查看当前使用的镜像
    nrm current 

    // 添加镜像
    nrm add <名称> <远程地址或私服地址>

    // 删除镜像
    nrm del <名称>

    // 切换镜像
    nrm use <名称> 

    // 测试镜像网络传输速度
    nrm test <名称>

    // 查看nrm版本号
    nrm <-version | -V> 

    // 查看nrm相关信息
    nrm <-help | -h>

    // 打开镜像主页
    nrm home <名称> [browser]

    // 上传npm包或命令程序
    nrm publish [<tarball>|<folder>]
