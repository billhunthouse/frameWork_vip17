import logging
from timeStamp import timestamp
log_name=timestamp()+'.log'
# print(log_name)
logging.basicConfig(filename=log_name,encoding='utf-8',level=logging.DEBUG)
logging.debug('test')
