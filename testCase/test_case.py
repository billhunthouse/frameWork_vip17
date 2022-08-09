#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import pytest
from common.readExcel import ReadData
from common.configHttp import configHttp
import os
import allure


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
    pytest.main(['-v','--alluredir=D:\\frameWork_vip17\\testReport\\allure'])
