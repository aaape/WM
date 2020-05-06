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
    market_ad = (By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')
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

#获取时间
    #strftime是time模块的方法，作用是格式化时间，第一个参数要获取时间的格式,字符串格式传参，第二个参数默认是现在的时间
    def get_time(self):
        now = self.strftime("%Y-%m-%d %H_%M_%S")
        return now

#获取屏幕截图

    def get_screenShort(self,module):
        times = self.get_time()
        #os.time.dirname()方法是获取文件的路径，参数是要获取路径的文件名
        #获取common_fun的根路径，然后拼接screenshort目录，拼接截图所属模块和时间
        img_file = os.time.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
        logging.info("get %s screen short..."% module)
        self.driver.get_screenshot_as_file(img_file)

#检查是否有广告
    def check_ad(self):
        try:
            element = self.driver.find_elemet("market_ad")
        except NoSuchElementException:
            logging.info("not found ad....")
        else:
            element.click()
            return True

#读取CVS数据
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
    def read_data(self,cvs_file,line):
        with open(cvs_file,'r',encoding='utf-8-sign') as file:
            data = self.cvs.reader(file)
            print(data)
            for i,v in enumerate(data,1):
                if i == line:
                    return v

if __name__ == '__main__':
    driver = appium_caps()

