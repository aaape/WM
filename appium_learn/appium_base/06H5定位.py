import time
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
# desired_caps['app'] = r'C:\Users\55077\Desktop\app\dr.fone3.2.0.apk'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'
desired_caps['deviceName'] = 'ccc'
desired_caps['udid'] = '8BN0217622004127'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5)

backup = driver.find_element_by_id('btnBackup')
backup.click()

WebDriverWait(driver,20).until(lambda x: x.find_element_by_id('btnRecoverData'))
contact = driver.find_element_by_id('btnRecoverData')
contact.click()

WebDriverWait(driver,20).until(lambda x: x.find_element_by_id('toolBar'))
content = driver.contexts
print(content)

driver.switch_to.context('WEBVIEW_com.wondershare.drfone')

email = driver.find_element_by_id('email')
email.click()
email.send_keys('5454@163.com')

# driver.find_element_by_id('//android.widget.ImageButton[@content-desc="转到上一层级"]')