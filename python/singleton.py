# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 23:18:15 2017

@author: Hpeng
"""

import os
import time
import datetime
import logging
class Logger :
    logger = None
    def myLogger(self):
        if None == self.logger:
            self.logger=logging.getLogger('ProvisioningPython')
            self.logger.setLevel(logging.DEBUG)
            now = datetime.datetime.now()
            handler=logging.FileHandler('ProvisioningPython'+ now.strftime("%Y-%m-%d") +'.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        return self.logger

s = Logger()
m = s.myLogger()
m2 = s.myLogger()
m.info("Info1")
m2.info("info2")

m.info("Info3")

