文档托管
=================
github上托管仓库
-----------------
.. github上创建仓库
.. +++++++++++++++
.. github上创建仓库
.. _______________
.. github上创建仓库
.. *****************
.. github上创建仓库
.. #################
首先在github上创建仓库，比如myBook，然后建立本地仓库::

	echo "# myBook" >> README.md
	git init
	git add README.md
	git commit -m "first commit"
	git branch -M main
	git remote add origin https://github.com/maweichao2021/myBook.git
	git push -u origin main


	or 

	git remote add origin https://github.com/maweichao2021/myBook.git
	git branch -M main
	git push -u origin main

 

在 ``https://readthedocs.org/`` 页面引入一个仓库：点击`import aProject`按钮


注意如果编译出错且提示找不到插件:: 

	Running Sphinx v4.0.3
	loading translations [zh]... done 
	Traceback (most recent call last):
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/site-packages/sphinx/registry.py", line 420, in load_extension
	    mod = import_module(extname)
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/importlib/__init__.py", line 127, in import_module
	    return _bootstrap._gcd_import(name[level:], package, level)
	  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
	  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
	  File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
	ModuleNotFoundError: No module named 'sphinx_markdown_tables' 
	The above exception was the direct cause of the following exception: 
	Traceback (most recent call last):
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/site-packages/sphinx/cmd/build.py", line 279, in build_main
	    args.tags, args.verbosity, args.jobs, args.keep_going)
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/site-packages/sphinx/application.py", line 243, in __init__
	    self.setup_extension(extension)
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/site-packages/sphinx/application.py", line 400, in setup_extension
	    self.registry.load_extension(self, extname)
	  File "/home/docs/checkouts/readthedocs.org/user_builds/cpp-note/envs/latest/lib/python3.7/site-packages/sphinx/registry.py", line 424, in load_extension
	    err) from err
	sphinx.errors.ExtensionError: Could not import extension sphinx_markdown_tables (exception: No module named 'sphinx_markdown_tables') 
	Extension error:
	Could not import extension sphinx_markdown_tables (exception: No module named 'sphinx_markdown_tables') 

原因是ReadTheDocs的python环境没有对应的第三方库文件，需要在项目根目录执行如下命令生成requirements.txt，这样ReadTheDocs会自动安装对应的插件依赖。

命令::
	
	python3 -m pip freeze > requirements.txt 


每次push代码到main分支后ReadTheDocs都会自动构建，下图是我第一本构建好的电子书：
 .. image:: gnu.png


 gitee上托管仓库
-----------------