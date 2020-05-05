from appium import webdriver
# appium服务器初始化参数
desired_caps = {}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'ccc'
desired_caps['udid'] = '8BN0217622004127'
desired_caps['appPackage'] = 'com.xag.agri.app'
desired_caps['appActivity'] = 'com.xag.agri.auth.ui.SplashActivity'
# desired_caps['app'] = 'C:\\Users\\55077\Desktop\kaoyanbang.apk'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 启动appium
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
# 注册账号

