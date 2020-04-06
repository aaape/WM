from selenium_learn import webdriver

# 显 式 等待 可以 只作 用于 仅有 同步 需求 的 测 试用 例。

# expected_conditions & webdriverwaits

# expented_conditions需要一些预置条件，来作为下一步测试的判断依据
from selenium_learn import webdriver
from selenium_learn.webdriver.common.by import By
from selenium_learn.webdriver.support.ui import WebDriverWait
from selenium_learn.webdriver.support import  expected_conditions
import unittest

class ExplicitWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("")

    def test_account_link(self):
        # lambda argument_list: expression 。这个函数叫做lambda函数，mbda函数是匿名的，lambda函数有输入和输出，lambda函数一般功能简单。将lambda函数作为参数传递给其他函数
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
        account = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(By.LINK_TEXT, "ACCOUNT"))
        account.click()



    def tearDown(self) :
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)