# author: HR
# date: 2017/10/9
__author__ = 'haoran.liang'
import os
import shutil

# file = open("");
print(os.name, "--", os.environ)
print("abs path:", os.path.abspath("."))

os.mkdir("D:/gitSpace/python/file/test")
# os.rmdir("D:/gitSpace/python/file/test")

shutil.copy("D:/gitSpace/python/file/file_base_operation.py", "D:/gitSpace/python/file/test/copy.py")