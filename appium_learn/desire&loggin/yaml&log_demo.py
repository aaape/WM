from appium import webdriver
import time
import logging
import yaml

file = open('yaml/desired_cap.yaml','r')
data = yaml.load(file)
logging.basicConfig(filename='demo.log',level='DEBUG',format='%(asctime)s[line:%(lineno)d]%(message)s')

desired_cpas = {}
desired_cpas['platformName'] = data['platformName']
desired_cpas['platformVersion'] = data['platformVersion']
desired_cpas['deviceName'] = data['deviceName']
desired_cpas['udid'] = data['udid']
desired_cpas['appPackage']=data['appPackage']
desired_cpas['appActivity']=data['appActivity']

logging.info('start app')
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) +'/wd/hub',desired_cpas)
driver.implicitly_wait(5)



