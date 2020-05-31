import unittest
from common.desired_caps import appium_caps
import logging
class StartEnd(unittest):
    def setUp(self):
        logging.info("setUp")
        self.driver = appium_caps()

    def tearsDown(self):
        logging.info("tearsDown")
        self.driver.close_app()