"""
导入logging模块，给其他方法使用
"""

import logging

def log():
    logging.basicConfig(level=logging.DEBUG,format='%(name)s日志-级别:%(levelname)s-模块:%(module)s.py-第%(lineno)d行:%(message)s')
    logger = logging.getLogger('InterFace')
    return logger


logger = log()