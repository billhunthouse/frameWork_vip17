import logging.config

# 配置 root logger
# logging.config.fileConfig(fname='test.ini', disable_existing_loggers=False)
logging.config.fileConfig(fname='test.ini', disable_existing_loggers=False)
# 获取logger 对象
logger = logging.getLogger("sampleLogger")
# 创建日志信息
logger.info("HELLO 智障")

