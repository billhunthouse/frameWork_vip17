import logging
# 获取文件名称
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 设置输出文件到 console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 设置文件输出到file
file = logging.FileHandler(filename='test.log')
file.setLevel(logging.DEBUG)

# 设置输出的格式化样式
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')

ch.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(file)
logger.info("test name")