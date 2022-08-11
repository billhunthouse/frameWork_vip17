import logging
# 获取文件名称
from logging.handlers import RotatingFileHandler
from common.timeStamp import timestamp


def log():
    logger = logging.getLogger('API')
    logger.setLevel(logging.DEBUG)


    # 设置输出文件到 console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 设置文件输出到file
    file_path = '../TestReport'
    # file = logging.FileHandler(filename='API.log')
    # 设置拆分log大小的方法
    file = RotatingFileHandler(filename=f'../TestReport\logRecord\{timestamp()}.log',maxBytes=1*1024*10,backupCount=3,encoding='utf-8')
    file.setLevel(logging.DEBUG)

    # 设置输出的格式化样式
    formatter = logging.Formatter('%(name)s日志-级别:%(levelname)s-模块:%(module)s.py-第%(lineno)d行:%(message)s')

    ch.setFormatter(formatter)
    file.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(file)
    return logger

if __name__ == '__main__':
    # logger = log()
    pass


