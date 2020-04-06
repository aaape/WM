# 文件名和类名不能一样
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest

class new_opt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("file://C:\\Users\\55077\\Desktop\\test.html")

    def test_language_options(self):
        exp_options = ["English", "French", "German"]
        act_options = []

        select_language = Select(self.driver.find_element_by_id("select-language"))
        self.assertEqual(2, len(select_language.options))

        for options in exp_options:
            act_options.append(options)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual("English", select_language.first_selected_option.text)
        select_language.select_by_visible_text("French")

        self.assertTrue("store=german"in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)

if __name__ == "__main__":
    unittest.main(verbosity=2)