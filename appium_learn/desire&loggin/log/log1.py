from appium import webdriver
import logging

logging.basicConfig(filename="log1.log",level='INFO',format='%(asctime)s[line:%(lineno)d]%(message)s')

logging.info('abc')