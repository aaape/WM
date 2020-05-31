from appium import webdriver
import logging.config
import yaml
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)#读取log配置
logging = logging.getLogger()#创建一个getLogger实例

def appium_caps():
    #读取yaml文件，是用with open防止yaml文件一直被占用
    with open('../config/kyb_caps.yaml','r') as file: data = yaml.load(file,Loader= yaml.FullLoader)

    #配置capabilities
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = data['udid']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    # desired_caps['app'] = data['app']

    logging.info("start run app...")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)

    return driver
# if __name__ == '__main__':
#     appium_caps()