from selenium import webdriver
import unittest

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://baidu.com")

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_id("kw")
        self.search_field.clear()

        self.search_field.send_keys("abc")
        self.search_field.submit()

        products = self.driver.find_element_by_name("wd")
        self.assertEqual(2,len(products));


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)