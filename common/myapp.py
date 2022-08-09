import logging
import mylib
import testMultiple

def main():
    logging.basicConfig(format='%(asctime)s-%(levelname0s-%(message)s',filename='myapp.log',level=logging.INFO)
    # logging.info("start")
    # mylib.do_something()
    # testMultiple.manyThread()
    # logging.info('test')
    logging.warning('This message will appear in python console.')


# main()

def ggod():
    # if not wirte filename to log -> will output console
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)
    # add filename --> write to log
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO,filename='%(asctime)s.log')

    logging.warning('This message will appear in python console.')
ggod()