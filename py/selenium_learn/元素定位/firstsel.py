# 导入selenium包
from time import sleep

from selenium_learn import webdriver
import time

# from time import sleep
# 指定浏览器
driver = webdriver.Firefox()
# 打开链接
driver.get("http://www.baidu.com")
# 寻找操操作元素
el = driver.find_element_by_id('kw')
# 传值
el.send_keys('淘宝网')
# 暂停
sleep(3)

# 关闭浏览器
driver.quit()
# 绝对路径写法
#
# r的作用：被r修饰的字符串，字符串中的转义符不做转义使用
# 除号/
# 目录结构\baiba

