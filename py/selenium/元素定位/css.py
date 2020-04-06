from time import sleep

from selenium import webdriver

dr = webdriver.Firefox()

dr.get("http://www.baidu.com")

dr.find_element_by_css_selector("input.s_ipt").send_keys("abc")

sleep(3)

dr.find_element_by_css_selector("input#su").click()

sleep(2)

dr.quit()

# 如果想更精准找到元素，可以按照父子元素关系列出两个选择器