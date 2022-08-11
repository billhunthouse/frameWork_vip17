import os,time,datetime


import os

def timestamp():
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式
    currentTime = now.strftime("%Y_%m_%d_%H_%M_%S")
    # print(currentTime)
    return currentTime
if __name__ == '__main__':
    pass

def pathFunc():
    currentPath = os.path.dirname(os.path.dirname(__file__))
    return currentPath


print(pathFunc())