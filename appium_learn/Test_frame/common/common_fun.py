from .desired_caps import appium_caps
from ..baseView.baseView import BaseView
import logging.config
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import time
import csv

#需求：取消版本更新，获取系统权限，获取屏幕尺寸

#公共模块封装一些通用的方法
class Common(BaseView):
    cancelBtn = (By.ID,'android:id/button2')
    skipBtn = (By.ID,'com.tal.kaoyan:id/tv_skip')

#取消升级按钮
    logging.info("===========check cancel button===========")
    def check_cancelBtn(self):
        try:
            element = self.driver.find_elemet(self.cancelBtn)
        except NoSuchElementException:
            logging.info('not found cancel button')
        else:
            element.click()
            return True

#跳过广告页
    logging.info("================check skip buttong=====================")
    def check_skipBtn(self):
        try:
            element = self.driver.find_elemet(self.skipBtn)
        except NoSuchElementException:
            logging.info("not found skip button...")
        else:
            element.click()
            return True


#获取屏幕尺寸
    logging.info("====================get screen size=======================")
    def get_screenSize(self):
        #get_window_size()是webdriver获取屏幕尺寸的方法，
        print(self.driver.get_window_size())
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)

#封装向上滑动屏幕函数
    def swipeUp(self):
        size = self.get_screenSize()
        y1 = int(size[0] * 0.2)
        x1 = int(size[1] * 0.5)
        y2 = int(size[0] * 0.9)
        self.swipe(x1,y1,x1,y1,1000)
