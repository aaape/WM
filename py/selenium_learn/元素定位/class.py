from time import sleep

from selenium_learn import webdriver

dr = webdriver.Firefox()

dr.get("http://www.baidu.com")

dr.find_Element_by_class_name("s_ipt").send_keys("琦生若梦 is a gay")

sleep(3)

dr.find_element_by_class_name("toindex").click()

sleep(3)



dr.quit()