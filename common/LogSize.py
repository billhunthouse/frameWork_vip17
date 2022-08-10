import logging
from logging.handlers import RotatingFileHandler
import timeStamp

dd = timeStamp.timestamp()
log_hannder = RotatingFileHandler(filename=f'{dd}.log',maxBytes=1*1024*10,backupCount=3,encoding='utf-8')

log = logging.getLogger('bill')
log.setLevel(logging.DEBUG)
log.addHandler(log_hannder)
log.info('-------asdad')


