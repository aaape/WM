from time import  sleep

from selenium import  webdriver

# elements  会返回查找元素的list，哪怕只有一个元素，要调用需要加索引
webdriver.Firefox.find_elements_by_class_name("s_ipt")[0].send_keys("weibo")