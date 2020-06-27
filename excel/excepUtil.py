# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date, datetime

# 获取一个Book对象
book = xlrd.open_workbook("D:/test.xls")

# 获取一个sheet对象的列表
sheets = book.sheets()

# 遍历每一个sheet，输出这个sheet的名字（如果是新建的一个xls表，可能是sheet1、sheet2、sheet3）
for sheet in sheets:
    if sheet.name != "考勤记录":
        continue
    print(sheet.name)
    print("=======================================================")

    rows = sheet.get_rows()
    tag = 0
    for row in rows:
        if tag < 3:
            tag = tag + 1
            continue
        if tag % 2 != 0:
            i = 0
            while i < 30:
                print("第", i, "列--> ", row[i].value)
                i = i + 1
        if tag % 2 == 0:
            print("姓名:", row[10].value)
        tag = tag + 1

