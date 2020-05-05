#封装公共类：为了处理app更新弹窗和权限弹窗

from appium_learn.unittest_case.baseView import BaseView
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium_learn.unittest_case.deisred_caps import desired_conf

class Common(BaseView):
    cancelBtn = (By.ID,'android:id/button2')
    skipBtn = (By.ID,'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info('check cancel button')
        try:
           element =  self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('update button is not found')
        else:
            logging.info('click cancel button')
            element.click()

    def check_skipBtn(self):
        logging.info('check skip button')
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skip button is not found')
        else:
            logging.info('click the skip button')
            element.click()

if __name__ == '__main__':
    driver = desired_conf()
    com = Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()
