from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ford(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")

    def bfr(self):
        driver = self.driver
        search_field = driver.find_element_by_id("kw")
        search_field.clear()

        search_field.send_keys("taobao")
        search_field.submit()

        se_wd_link = driver.find_element_by_link_text("淘宝网 - 淘！我喜欢")
        se_wd_link.click()
        self.assertTrue("淘宝网 - 淘！我喜欢", driver.title)

        driver.back()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("淘宝_百度搜索")))

        driver.forward()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("淘宝网 - 淘！我喜欢")))

        driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("淘宝网 - 淘！我喜欢")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()