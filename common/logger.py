import logging
import sys

# Todo sys.stdout方法
stdout_back = sys.stdout

log_file = open('message.log','w')
sys.stdout = log_file

print('now all message will be written to message.log')

log_file.close()

print('now message will be display on screen')

