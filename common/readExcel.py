#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import xlrd,xlwt
import os

class ReadData():
    def __init__(self):

        # 1.读取excel
        self.excel = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        print(f"-----文件名称是{self.excel}")
        self.wb = xlrd.open_workbook(self.excel)


        # 2.获取文件的索引，最大行数和列数，获取某个单元格的值，获取某行某列的值
        self.sh = self.wb.sheet_by_index(0)
        print(f"-----sheet名字:{self.sh}")

        # 最大列数
        self.colnum = self.sh.ncols
        # 最大行数
        self.rownum = self.sh.nrows
        print(f"最大的列数和行数是{self.colnum},{self.rownum}")

    def read_excel(self):
        data = []
        for i in range(1,self.rownum):
            keylist = self.sh.row_values(0)
            print(f"keylist的值是{keylist}")
            valueList = self.sh.row_values(i)
            print(f"valuelist{valueList}")

            dict1 = {keylist[j]:valueList[j] for j in range(len(keylist))}
            data.append(dict1)

        return data

if __name__ == '__main__':
    test = ReadData()
    print(test.read_excel())