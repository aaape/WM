from appium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['app'] = r'C:\Users\55077\Desktop\app\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = '.ui.activity.SplashActivity'
desired_caps['deviceName'] = 'ccc'
desired_caps['udid'] = '8BN0217622004127'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

WebDriverWait(driver,5).until(lambda x: x.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]'))
button2 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[1]')
button2.click()

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x , y

l = get_size()
# print(x, y)


def leff_swipe():
    l = get_size()
    x1 = int(x * 0.9)
    x2 = int(y * 0.5)


# driver.swipe(int(x * 0.9), int(y * 0.5), int(x * 0.1),int(y * 0.5), 400)