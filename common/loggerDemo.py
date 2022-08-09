import logging
from timeStamp import timestamp
logging.basicConfig(filename='example.log',filemode='w',level=logging.DEBUG)
logging.debug('this message will be add example.log')
logging.info('this info also will add into there')
logging.warning('test warning'+ str(timestamp()))
