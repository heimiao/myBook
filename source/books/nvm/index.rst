nvm
================

以下是 NVM（Node Version Manager）的常用命令大全，这些命令可以帮助你管理和切换不同版本的 Node.js：


.. toctree::
    .. :maxdepth: 2
    .. :numbered: 2

安装 `NVM <https://gitcode.com/gh_mirrors/nv/nvm/overview?utm_source=highlight_word_gitcode&word=nvm&isLogin=1/>`_
----------

1. 下载并安装 NVM::

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

2. 重新加载你的 shell 配置文件::

    source ~/.bashrc   # 如果你使用的是 bash
    source ~/.zshrc    # 如果你使用的是 zsh

验证 NVM 安装
-------------
1. 安装特定版本的 Node.js::
    
    nvm install <version>

例如，安装 18.16.0 版本::

    nvm install 18.16.0

2. 安装最新的 LTS 版本::
    
    nvm install --lts

3. 安装最新的 Node.js 版本::
    
    nvm install node


切换 Node.js 版本
-------------
1. 使用特定版本的 Node.js:: 

    nvm use <version>

例如，使用 18.16.0 版本::

    nvm use 18.16.0

2. 设置默认版本::

    nvm alias default <version>

例如，设置 18.16.0 为默认版本::

    nvm alias default 18.16.0 

3. 列出所有已安装的 Node.js 版本::

    nvm ls

4. 列出所有可安装的远程 Node.js 版本::

    nvm ls-remote

5. 列出已安装的 LTS 版本::

    nvm ls --lts

6. 卸载 Node.js 版本::

    nvm uninstall <version>

例如，卸载 18.16.0 版本::

    nvm uninstall 18.16.0

其他命令
----------
1. 显示当前使用的 Node.js 版本::

    nvm current

2. 显示 NVM 版本::

    nvm --version

3. 显示 NVM 使用帮助::

    nvm help 
4. 列出已安装的 npm 版本::

    nvm ls-remote --npm

高级命令
-------

1. 运行特定版本的 Node.js 代码::

    nvm exec <version> <command>

例如，使用 18.16.0 版本运行 node -v::

    nvm exec 18.16.0 node -v

2. 以特定版本打开新 shell::
    
    nvm run <version>

例如，使用 18.16.0 版本打开新 shell::

    nvm run 18.16.0
 