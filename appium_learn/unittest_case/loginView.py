import logging
from appium_learn.unittest_case.common_fun import Common
from appium_learn.unittest_case.deisred_caps import desired_conf
from selenium.webdriver.common.by import By

class LoginView(Common):
    #找到要控制元素的id
    username_type = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_btn_type = (By.ID,'com.tal.kaoyan:id/login_login_btn')


    def login_action(self,username,password):
        # 执行登录前 先查看有没有版本更新或者权限设置
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('login')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click login button')
        self.driver.find_element(*self.login_btn_type).click()
        logging.info('loging success')

if __name__ == '__main__':
    driver = desired_conf()
    l = LoginView(driver)
    l.login_action('ak47ak47ak48','12345678')
