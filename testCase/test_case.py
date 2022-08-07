#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import pytest
from common.readExcel import ReadData
from common.configHttp import configHttp
import os


re = ReadData()

class TestCase1():
    @pytest.mark.parametrize('dic', re)
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
        ch = ConfigHttp(interfaceUrl, method, value)
        re = ch.run()
        real = re.json()['errorCode']
        # 断言
        assert real == int(expect)
if __name__ == '__main__':
    pytest.main()