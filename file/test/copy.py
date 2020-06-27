# author: HR
# date: 2017/10/9
# *-* utf-8 *-*
__author__ = 'haoran.liang'
import os
import shutil

# file = open("");
# print(os.name, "--", os.environ)
# print("abs path:", os.path.abspath("."))
#
# # os.mkdir("D:/gitSpace/python/file/test")
# os.rmdir("D:/gitSpace/python/file/test")

# shutil.copy("D:/gitSpace/python/file/file_base_operation.py", "D:/gitSpace/python/file/test/copy.py")

# 大文件复制 gbk编码的文件错误：UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 36: illegal multibyte sequence
file_read = None
file_write = None
try:
    file_read = open("D:\\gitSpace\\python\\file\\test\\copy_test_origin", "r")
    file_write = open("D:\\gitSpace\\python\\file\\test\\copy_test", "w")

    while True:
        text = file_read.readline()
        if not text:
            break
        file_write.write(text)
finally:
    file_read.close()
    file_write.close()

str_show = u"I'm 大世界"
for c in str_show:
    print("char: ", c)