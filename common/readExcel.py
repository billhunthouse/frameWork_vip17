#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import xlrd,xlwt
import os
from common.log import log
logger = log()

class ReadData():
    def __init__(self):

        # 1.读取excel
        self.excel = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        # print(f"-----文件名称是{self.excel}")
        self.wb = xlrd.open_workbook(self.excel)


        # 2.获取文件的索引，最大行数和列数，获取某个单元格的值，获取某行某列的值
        self.sh = self.wb.sheet_by_index(0)
        # print(f"-----sheet名字:{self.sh}")

        # 最大列数
        self.colnum = self.sh.ncols
        # 最大行数
        self.rownum = self.sh.nrows
        # print(f"最大的列数和行数是{self.colnum},{self.rownum}")

    def read_excel(self):
        data = []
        # 以最大的列数为循环,从第1列开始遍历
        for i in range(1,self.rownum):
            # 第0行的数据是title, 以title为列
            keylist = self.sh.row_values(0)
            # 从第一行开始读取数据,逐行读取行的值
            valueList = self.sh.row_values(i)
            # print(f"valuelist{valueList}")

            # 列表推导式,生成test Data
            dict1 = {keylist[j]:valueList[j] for j in range(len(keylist))}
            data.append(dict1)

        return data

if __name__ == '__main__':
    test = ReadData()
    logger.info(test.read_excel())