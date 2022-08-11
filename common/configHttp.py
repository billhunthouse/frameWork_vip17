#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# DateTime:

import requests
import json
from common.readExcel import ReadData

class configHttp():

    def __init__(self,interfaceUrl,method,value):
        self.interfaceUrl = interfaceUrl
        self.method = method
        self.value = value


    def __get(self):
        try:
            re = requests.get(url=self.interfaceUrl,params=eval(self.value))
        except Exception as msg:
            print("接口报错")
        else:
            return re

    def __post(self):
        try:
            re = requests.post(url=self.interfaceUrl, data=eval(self.value))
        except Exception as msg:
            print('接口请求失败，系统提示：%s' % msg)
        else:
            return re

    def __put(self):
        try:
            re = requests.put(url=self.interfaceUrl, data=eval(self.value))
        except Exception as msg:
            print('接口请求失败，系统提示：', msg)
        else:
            return re

    def __delete(self):
        try:
            re = requests.put(url=self.interfaceUrl)
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
    url = 'https://www.wanandroid.com/login'
    method = 'post'
    value = "{'username':'liangchao','password':'123456'}"
    ch = configHttp(url,method,value)
    print(ch.run())