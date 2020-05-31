from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_caps
from selenium.webdriver.common.by import By
import random,time
import logging

class RegesiterView(Common):

    # 注册按钮
    regesiter_btn = (By.ID,"com.tal.kaoyan:id/login_register_text")

    #填写注册信息页面
    reg_head_btn = (By.ID,"com.tal.kaoyan:id/activity_register_userheader")
    reg_head_pic = (By.ID,"com.tal.kaoyan:id/item_image")
    reg_head_save = (By.ID,"com.tal.kaoyan:id/save")

    reg_user_box = (By.ID,"com.tal.kaoyan:id/activity_register_username_edittext")
    reg_pass_box = (By.ID,"com.tal.kaoyan:id/activity_register_password_edittext")
    reg_email_box = (By.ID,"com.tal.kaoyan:id/activity_register_email_edittext")
    reg_comfirm_btn = (By.ID,"com.tal.kaoyan:id/activity_register_register_btn")

    reg_abnormal_btn =(By.ID,"")

    #选择院校按钮
    chose_year_btn = (By.ID,"")
    chose_year = (By.ID,"")

    chose_univ_btn = (By.ID,"")
    chose_city_btn = (By.ID,"")
    chose_univs_btn = (By.ID,"")

    chose_major_btn = (By.ID,"")
    chose_major = (By.ID,"")
    chose_major_in = (By.ID,"")

    chose_go = (By.ID,"")

    #个人信息
    myself = (By.ID,"")
    user_info = (By.ID,"")

    def register_before(self):
        self.check_cancelBtn()
        self.check_skipBtn()


        logging.info("click the regesiter btn")
        self.find_element(*self.regesiter_btn).click()

    def register(self,reg_username,reg_password,reg_email):
        logging.info("start regesiter...")
        #选择注册头像
        self.driver.find_element(*self.reg_head_btn).click()
        time.sleep(15)
        self.driver.find_elements(*self.reg_head_pic)[10].click()
        self.driver.find_element(*self.reg_head_save).click()
        #填写注册信息
        self.driver.find_element(*self.reg_user_box).send_keys(reg_username)
        logging.info("the regesiter username is: %s " %reg_username)
        self.driver.find_element(*self.reg_pass_box).send_keys(reg_password)
        logging.info("the regesiter password is: %s" %reg_password)
        self.driver.find_element(*self.reg_email_box).send_keys(reg_email)
        logging.info("the regesit email is: %s" %reg_email)
        #提交注册信息
        self.find_element(*self.reg_comfirm_btn).click()

        try:
            self.find_element(*self.chose_year_btn)
        except NoSuchElementException:
            logging.info("regist fail..")
            self.get_screenShort("regist fail")
            return False
        else:
            #检测注册成功孩有关键的一步，调用添加院校的方法
            self.chose_university()
            if self.check_regesit_status():
                return True
            else:
                return False


    def chose_university(self):
        logging.info("start chose university...")
        #选择年份
        self.driver.find_element(*self.chose_year_btn).click()
        self.driver.find_elements(*self.chose_year)[3].click()
        logging.info("the year is: %s " %self.driver.find_elements(*self.chose_year)[3])

        #选择院校
        self.driver.find_element(*self.chose_univ_btn).click()
        self.driver.find_elements(*self.chose_city_btn)[5].click()
        self.driver.find_elements(*self.chose_univs_btn)[6].click()

        #选择专业
        self.driver.find_element(*self.chose_major_btn).click()
        self.driver.find_elements(*self.chose_major)[4].click()
        self.driver.find_elements(*self.chose_major_in)[2].click()

        #进入考研帮
        self.driver.find_element(*self.chose_go).click()

    def check_regesit_status(self):
        logging.info("check regesit status....")

        try:
            self.find_element(*self.myself).click()
            self.find_element(*self.user_info)
        except NoSuchElementException:
            logging.info("regist fail")
            self.get_screenShort("regist fail")
            return False
        else:
            logging.info("regist success")
            return True

if __name__ == '__main__':
    driver = appium_caps()
    reg = RegesiterView(driver)


    username = "ak47" + str(random.randint(0000,9999))
    password = "wechat" + str(random.randint(0000,9999))
    email = "550770138@163.com"

    # username = 'zxw2018' + 'fly' + str(random.randint(1000, 9000))
    # password = 'zxw2018' + str(random.randint(1000000, 9000000))
    # email = str(random.randint(100000000, 900000000)) + '@163.com'

    reg.register_before()
    reg.register(username,password,email)