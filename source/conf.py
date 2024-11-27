# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('./my_theme'))  # 指定主题目录


project = '黑猫图书馆'
copyright = '2024, heimao'
author = 'heimao'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark','sphinx_markdown_tables']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' #'alabaster' 
html_static_path = ['_static']

# 使用自定义主题
# html_theme = 'my_theme' 
# # 设置主题的路径
# html_theme_path = ['my_theme']  # 主题路径 
# # 如果需要使用自定义CSS文件，确保 Sphinx 能找到它
# html_static_path = ['_static', 'my_theme/static']  # 静态资源路径 
# # 其他配置（可根据需要调整）
# html_css_files = [
#     'css/main.css',  # 引用自定义的CSS文件
# ]
