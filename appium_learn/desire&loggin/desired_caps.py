from appium import webdriver
import yaml

file = open('yaml/desired_cap.yaml', 'r')
#python文件中打开yaml配置文件
data = yaml.load(file)
#将yaml文件转换为python的字典格式

desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']
desired_caps['udid'] = data['udid']
desired_caps['appPackage']= data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
desired_caps['resetKeyborad'] = data['resetKeyboard']

driver = webdriver.Remote('http://'+str(data['ip']) + ':' +  str(data['port']) +'/wd/hub',desired_caps)
driver.implicitly_wait(5)