from selenium_learn import webdriver
from selenium_learn.webdriver.common.alert import Alert
import unittest

class analog_alert(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("file://C:\\Users\\55077\\Desktop\\test.html")

    def test_compare_products_removal_alert(self):
        search_field = self.driver.find_element_by_id("A")
        search_field.clear()

        search_field.send_keys("phones")
        search_field.submit()

        # self.driver.find_element_by_link_text("Add to Compare").click()

        self.driver.find_element_by_link_text("Clear All").click()

        alert = self.driver.switch_to_alert()

        self.driver.alert.send_keys("can you  hear me")

        alert_text = alert.text

        self.assertEqual("can you  hear me", alert_text)

        alert.accept()

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()