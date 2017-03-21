# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 23:20:15 2017

@author: Hpeng
"""
import logging

logger_lb = logging.getLogger('liubangxxasdfasdfgaasdfasdf')
logger_hx = logging.getLogger('hanxin')
logger_xh = logging.getLogger('xiaohe')
logger_zl = logging.getLogger('zhangliang')
logger_lb.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add the handlers to logger
#logger_lb.addHandler(ch)
if not len(logger_lb.handlers):
    logger_lb.addHandler(ch)
#if not logger_lb.hasHandlers:
#    logger_lb.addHandler(fh)
logger_hx.addHandler(fh)
# 'application' code
logger_lb.debug('debug message')
logger_lb.info('info message')
logger_lb.warn('warn message')
logger_lb.error('error message')
logger_lb.critical('critical message')

logger_hx.info('info message')