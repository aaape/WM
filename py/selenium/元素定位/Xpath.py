from selenium import webdriver

dr = webdriver.Firefox()

# 绝对路径
dr.find_element_by_xpath("/html/body/div/div/")

# 相对路劲
dr.find_element_by_xpath("//input[]")