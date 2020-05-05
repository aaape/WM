from appium import webdriver
import yaml
import logging
import logging.config

CONLOG = 'log/log.conf'
logging.config.fileConfig(CONLOG)
logging = logging.getLogger()

def desired_conf():
    file = open('yaml/desireds_cap.yaml','r')
    data = yaml.load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = data['udid']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)

    return driver
if __name__ == '__main__':
    desired_conf()
