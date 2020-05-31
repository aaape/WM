from common.common_fun import Common
from common.desired_caps import appium_caps
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging,time,csv

class LoginView(Common):
    #登录页面按钮
    username_box = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_box = (By.ID,"com.tal.kaoyan:id/login_password_edittext")
    login_btn = (By.ID,"com.tal.kaoyan:id/login_login_btn")

    #账号已登录弹窗按钮
    account_alert_btn = (By.ID,"com.tal.kaoyan:id/tip_commit")

    #个人信息页面按钮
    myself_btn = (By.ID,"com.tal.kaoyan:id/mainactivity_button_mysefl")
    user_info_btn = (By.ID,"com.tal.kaoyan:id/activity_usercenter_username")

    #退出登录按钮
    setting_btn = (By.ID,"com.tal.kaoyan:id/myapptitle_RightButton_textview")
    logout_btn =  (By.ID,"com.tal.kaoyan:id/setting_logout_text")
    logout_commit = (By.ID,"com.tal.kaoyan:id/tip_commit")

    def login(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("start login.....")
        #这里的self.driver.find_element是父类的方法
        self.driver.find_element(*self.username_box).send_keys(username)
        logging.info("the username:%s" % username)
        self.driver.find_element(*self.password_box).send_keys(password)
        logging.info("the password:%s" % password)
        self.driver.find_element(*self.login_btn).click()
        return True

#检查是否有账户已经登陆警告，该方法给check_login_status调用
    def check_account_alert(self):
        logging.info("check acoount alert...")
        try:
            elemenet = self.driver.find_element(*self.account_alert_btn)
        except NoSuchElementException:
            pass
        else:
            logging.info("click login button...")
            elemenet.click()
            return True

#检查是否已经登录
    def check_login_status(self):
        self.check_ad()
        self.check_account_alert()

        logging.info("check loging status")
        try:
            myself = self.find_element(*self.myself_btn)
            # user_info = self.find_element(*self.user_info_btn)
        except NoSuchElementException:
            logging.info("login fail")
            self.get_screenShort("login fail")
            return False
        else:
            myself.click()
            logging.info("login success")
            self.logout()
            return True

#登录成功后登出
    def logout(self):
        logging.info("loginout...")
        self.driver.find_element(*self.setting_btn).click()
        self.driver.find_element(*self.logout_btn).click()
        self.driver.find_element(*self.logout_commit).click()

if __name__ == '__main__':
    driver = appium_caps()
    time.sleep(10)
    l = LoginView(driver)
    l.login("ak47ak47ak49","qq123456789")
    l.check_login_status()