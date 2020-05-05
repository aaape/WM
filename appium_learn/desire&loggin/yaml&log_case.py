from appium import webdriver
import yaml
import logging #导入日志模块，为了脚本正文打印日志方法：loggin.info()
import logging.config #导入日志配置文件

file = open('yaml/desired_cap.yaml','r')
data = yaml.load(file)

CON_LOG='log/log.conf'
logging.config.fileConfig(CON_LOG) #读取log配置文件
logging = logging.getLogger() #定义所使用的记录器getlogger()参数为空，默认使用root级别记录器

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