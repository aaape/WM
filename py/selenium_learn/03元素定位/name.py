from time import sleep

from selenium_learn import webdriver

driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

el = driver.find_element_by_name("tj_settingicon")

el.click()

sleep(3)