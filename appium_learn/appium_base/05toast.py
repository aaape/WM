#coding = uft-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
# desired_caps['app'] = r'C:\Users\55077\Desktop\app\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
desired_caps['deviceName'] = 'ccc'
desired_caps['udid'] = '8BN0217622004127'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['automationName'] = 'uiautomator2'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)

# self_btn = driver.find_element_by_id('mainactivity_button_mysefl')
# self_btn.click()
# time.sleep(1)
#
# head_btn = driver.find_element_by_id('activity_usercenter_userheader')
# head_btn.click()
# time.sleep(2)

WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('login_email_edittext'))
user_name = driver.find_element_by_id('login_email_edittext')
user_name.send_keys('ak47ak47ak45')

password = driver.find_element_by_id('login_password_edittext')
password.click()
password.send_keys('qq123456789')
user_name.click()

login_btn = driver.find_element_by_id('login_login_btn')
login_btn.click()

error_message = '账号不存在'

message = '//*[@text = \'{}\']'.format(error_message)

WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath(message))
toast_element = driver.find_element_by_xpath(message)
print(toast_element.text)