
 # 安装Sphinx #
 ## 安装Sphinx ## 
 打开终端：这一步由于太基础了所以不做过多介绍

 linux 系统下安装极简，一行代码搞定
 `
 	brew cask install sphinx
 `

 或window安装方式
 `pip install sphinx`

 ## 创建项目 ## 

```
mkdir myBook

cd myBook

sphinx-quickstart
```
输入完后按提示设置文档信息：
```  
sphinx-quickstart
Welcome to the Sphinx 4.0.3 quickstart utility. 
Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets). 
Selected root path: . 
You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y  <--------这里选y表示编译的文件单独放在build中 
The project name will occur in several places in the built documentation.
> Project name: CppDictionary  <--------项目名
> Author name(s): TOMOCAT      <--------作者
> Project release []: v1.0     <--------版本号 
If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language. 
For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: zh_CN  <-------- 语言(简体中文) 
Creating file /root/readTheDocs/cpp_dictionary/source/conf.py.
Creating file /root/readTheDocs/cpp_dictionary/source/index.rst.
Creating file /root/readTheDocs/cpp_dictionary/Makefile.
Creating file /root/readTheDocs/cpp_dictionary/make.bat. 
Finished: An initial directory structure has been created. 
You should now populate your master file /root/readTheDocs/cpp_dictionary/source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```
## 安装tree查看目录结构 ##

window
```
tree
```

linux
```
yum install tree
tree -C .
```

项目解构解析

```
|-- build       <--------  生成文件的输出目录
|-- make.bat    <--------  Windows 命令行中编译用的脚本
|-- Makefile    <--------  编译脚本，make 命令编译时用
`-- source      <--------  文档源文件
    |-- conf.py     <--------  进行 Sphinx 的配置，如主题配置等
    |-- index.rst   <--------  文档项目起始文件，用于配置文档的显示结构
    |-- _static     <--------  静态文件目录, 比如图片等
    `-- _templates  <--------  模板目录

```

## 编译文档成html ##
命令

 `
 	make html
   //如果报错的话看是不是没找到make文件，制定下执行本地make文件
   .\make html
 `

结果

```
make html

Running Sphinx v4.0.3
loading translations [zh_CN]... done
making output directory... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: [new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index                                                                                      
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index                                                                                       
generating indices... genindex done
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in Chinese (code: zh)... done
dumping object inventory... done
build succeeded. 
The HTML pages are in build/html.

```
在build/html目录下打开index.html就可以看到效果

## 部署http服务 ##

make html的方式可以生成html文件，但是需要用浏览器打开。我们也可以通过sphinx-autobuild工具部署http服务：

### 安装HTTP服务 ###

```
pip install sphinx sphinx-autobuild 
```
### 启动HTTP服务 ###

``` 
sphinx-autobuild source build/html

```

## 更换主题 ## 

上面的测试效果，使用的是默认的主题alabaster，如果想安装其它的主题，可以先到Sphinx的官网查看：[](https://sphinx-themes.org/)

### 安装主题 ###
我们安装并使用最常用的Read the Docs主题：`pip install sphinx sphinx_rtd_theme`

### 修改conf.py文件 ###
```
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

```

[其他主题参考](https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/)

## 支持markdown ## 

Sphinx默认只支持reST格式的文件，我们需要安装支持MarkDown的插件：

### 安装markdown ###
```
pip install recommonmark
pip install sphinx-markdown-tables

```
### 修改conf.py文件 ###
```
extensions = ['recommonmark','sphinx_markdown_tables']
```
## 文档结构描述及配置 ## 

要配置文档内容，我们需要修改`index.rst`文件（也可以使用*.md格式），它的内容如下：

```
.. cpp_dictionary documentation master file, created by
   sphinx-quickstart on Wed Jul  7 09:42:42 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive. 
Welcome to cpp_dictionary's documentation!
========================================== 
.. toctree::
   :maxdepth: 2
   :caption: Contents: 
Indices and tables
================== 
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
语法解释：

- 两个点..+空格+后面的文本，代表注释
- 等号线====+上一行的文本，代表一级标题
- .. toctree::声明的一个树状结构
- :maxdepth: 2 表示页面的级数最多显示两级
- :caption: Contents: 用于指定标题文本
- 最下面的3行是索引和搜索链接

查看更多 ``reStructuredText（*.rst）`` ，

[reStructuredText 英文](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html){target="_blank"};

[reStructuredText 中文](https://www.osgeo.cn/sphinx/usage/restructuredtext/basics.html#google_vignette)或者 https://zh-sphinx-doc.readthedocs.io/en/latest/rest.html

[reStructuredText 配置项](https://www.osgeo.cn/sphinx-note/sphinx-conf.html){target="_blank"};  
