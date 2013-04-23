#-*-coding:utf-8-*-

import logging
import os

print str(os.path)
print str(os.getcwd())

logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
logging.debug('this is a message')
