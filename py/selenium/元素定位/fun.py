import unittest
from selenium import webdriver
class ST(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_catagory(self):
# get the search box
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

# enter search keyword and submit
        self.search_field.send_keys("phones")
        self.search_field.submit()

# get all the anchor elements which have
# product names displayed
# currently on result page using
# find_elements_by_Xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))

    def tearDown(self):
# close the browser window
        self.driver.quit()