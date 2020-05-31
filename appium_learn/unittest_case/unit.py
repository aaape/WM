import unittest
from unittest_case.deisred_caps import desired_conf
import logging
from time import sleep

# 封装用例启动结束时的配置

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('setup')
        self.driver = desired_conf()

    def tearDown(self):
        logging.info('tearsdown')
        sleep(5)
        self.driver.close_app()