#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import requests
import json
from common.readExcel import ReadData
from requests.auth import HTTPBasicAuth
from common.readExcel import ReadData

class configHttp():

    def __init__(self,interfaceUrl,method,value,auth):
        self.interfaceUrl = interfaceUrl
        self.method = method
        self.value = value
        self.auth = auth

    def __get(self):
        try:
            re = requests.get(url=self.interfaceUrl,params=eval(self.value),HTTPBasicAuth=self.auth)
        except Exception as msg:
            print("接口报错")
        else:
            return re

    def __post(self):
        try:
            re = requests.post(url=self.interfaceUrl, data=eval(self.value),HTTPBasicAuth=self.auth)
        except Exception as msg:
            print('接口请求失败，系统提示：%s' % msg)
        else:
            return re

    def __put(self):
        try:
            re = requests.put(url=self.interfaceUrl, data=eval(self.value),HTTPBasicAuth=self.auth)
        except Exception as msg:
            print('接口请求失败，系统提示：', msg)
        else:
            return re

    def __delete(self):
        try:
            re = requests.put(url=self.interfaceUrl,HTTPBasicAuth=self.auth)
        except Exception as msg:
            print('接口请求失败，系统提示：', msg)
        else:
            return re

    def run(self):
        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()
        elif self.method.lower() == 'put':
            return self.__put()
        elif self.method.lower() == 'delete':
            return self.__delete()
        else:
            print('未找到匹配的请求方式，请检查！')
if __name__ == '__main__':
    # testData = ReadData()
    # allData = testData.read_excel()
    # print(allData[3]['auth'])
    # {"username":"welab","password":"r[BcgS4Uyk5[K3&"}
    pass