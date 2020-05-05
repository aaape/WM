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

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)

WebDriverWait(driver,10).until(lambda x: x.find_element_by_id('mainactivity_radiogroup'))
square = driver.find_element_by_id('mainactivity_radiogroup')
square.click()
