#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import pytest
from common.readExcel import ReadData
from common.configHttp import configHttp
import os
import allure
from common.timeStamp import timestamp



re = ReadData()
testdata = re.read_excel()

class TestCase1():
    @pytest.mark.parametrize('dic', testdata)
    def test_run(self, dic):
        print("=========>", dic)
        # 数据  id, interfaceUrl, name, method, value, expect
        id = dic["id"]
        interfaceUrl = dic["interfaceUrl"]
        name = dic["name"]
        method = dic["method"]
        value = dic["value"]
        expect = dic["expect"]
        # 实例化
        ch = configHttp(interfaceUrl, method, value)
        re = ch.run()
        real = re.json()['errorCode']
        # 断言
        assert real == int(expect)
if __name__ == '__main__':
    # 生成allure 报告,定义报告路径
    JsonFilePath = './testReport/AllureJsonResutlt'
    HtmlFilePath = './testReport/AllureHtmlResult'
    t1 = timestamp()
    # 以日期为格式生成json报告路径
    pytest.main(['-v',f'--alluredir={JsonFilePath}//{t1}'])
    print("生成json格式完成")
    # 生成html 报告路径
    os.system(f'allure generate -c -o {JsonFilePath}//{t1} {HtmlFilePath}//{t1} ')
    print("生成html完成")