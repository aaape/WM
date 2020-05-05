from appium import webdriver
import time
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


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

reg_btn = driver.find_element_by_id('login_register_text')
reg_btn.click()
driver.implicitly_wait(5)

add_tou = driver.find_element_by_id('activity_register_userheader')
add_tou.click()
time.sleep(20)

chose_picture = driver.find_elements_by_class_name('android.widget.ImageView')
for i in chose_picture:
    print(i)
chose_picture[3].click()
driver.implicitly_wait(5)

save = driver.find_element_by_id('save')
save.click()
driver.implicitly_wait('5')

user_name = driver.find_element_by_id('activity_register_username_edittext')
user_name.send_keys('ak47ak47ak49')

password = driver.find_element_by_id('activity_register_password_edittext')
password.click()
password.send_keys('qq123456789')
user_name.click()

email = driver.find_element_by_id('activity_register_email_edittext')
email.click()
email.send_keys('0668555@qq.com')
driver.implicitly_wait(5)

reg = driver.find_element_by_id('activity_register_register_btn')
reg.click()
driver.implicitly_wait(5)

years = driver.find_element_by_id('activity_perfectinfomation_time')
years.click()
time.sleep(2)
ye = driver.find_elements_by_class_name('android.widget.TextView')
ye[3].click()

school = driver.find_element_by_id('perfectinfomation_edit_school_name')
school.click()
time.sleep(2)
sheng = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.TextView[1]")
sheng.click()
university = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[5]/android.widget.TextView')
university.click()

major = driver.find_element_by_id('activity_perfectinfomation_major')
major.click()
time.sleep(2)
xueke = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView')
xueke.click()
makesi = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.TextView')
makesi.click()

acess = driver.find_element_by_id('activity_perfectinfomation_goBtn')
acess.click()