from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'ccc'
desired_caps['udid'] = '8BN0217622004127'
# desired_caps['app'] = ''
desired_caps['appPackage'] = 'com.xag.agri.app'
desired_caps['appActivity'] = 'com.xag.agri.auth.ui.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = False
desired_caps['noReset'] = True#appium预置功能，当你执行值为False，执行完脚本后；刷新截图获取不了手机当前的页面

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
print(type(driver))
driver.implicitly_wait(5)

def login():
    try:
        username = driver.find_element_by_id('auth_et_login_user_name')
        username.click()
        username.send_keys(15113738093)
        driver.implicitly_wait(5)

        password = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.EditText')
        password.click()
        password.send_keys(123456)
        driver.implicitly_wait(5)

        username.click()
        driver.implicitly_wait(5)

        login_btn = driver.find_element_by_id('btn_login')
        login_btn.click()
    except:
        print('already login')
login()

def check_update():
    try :
        check_update = driver.find_element_by_id('btn_no')
        print(type(check_update))
        check_update.click()
    except:
        print("the latest version")
check_update()