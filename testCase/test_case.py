#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:
import time

import pytest
import os
import allure

from common.readExcel import ReadData
from common.configHttp import configHttp
from common.commonMethod import timestamp
from common.commonMethod import pathFunc
from common.log import log

logger = log()
re = ReadData()
testdata = re.read_excel()

class TestCase1():
    # parametrize参数化作为name和value
    # dic是name,testData是实际的value的值
    # 整个allTestData是value
    @pytest.mark.parametrize('dic', testdata)
    def test_run(self, dic):
        print("=========>", dic)
        # 数据  id, interfaceUrl, name, method, value, expect,auth
        id = dic["id"]
        interfaceUrl = dic["interfaceUrl"]
        name = dic["name"]
        method = dic["method"]
        value = dic["value"]
        expect = dic["expect"]
        auth = dic["auth"]
        # 实例化
        ch = configHttp(interfaceUrl, method, value,auth)
        re = ch.run()
        print('-----------------'+f"re的值是{re}")
        status = re.status_code
        # 断言
        assert status == int(expect)
if __name__ == '__main__':
    # 生成allure 报告,定义报告路径
    JsonFilePath = pathFunc()+r'\testReport\AllureJsonResult'
    HtmlFilePath = pathFunc()+r'\testReport\AllureHtmlReport'

    t1 = timestamp()
    # 以日期为格式生成json报告路径
    pytest.main(['-v',f'--alluredir={JsonFilePath}\\{t1}'])
    # 生成html 报告路径    -c 参数为输出文件位置，  -o 参数为 json 路径位置
    os.system(f'allure generate -c -o {HtmlFilePath}\\{t1} {JsonFilePath}\\{t1}  ')