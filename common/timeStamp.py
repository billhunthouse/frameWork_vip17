import os,time,datetime


def timestamp():
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式
    currentTime = now.strftime("%Y-%m-%d %H:%M:%S")
    # print(currentTime)
    return currentTime


