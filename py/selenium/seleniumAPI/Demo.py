# 创建一个测试脚本，验证程序能否正确创建一个新的账户

# 导入unittest测试框架：用于创建用例，执行用例（操作webdriverAPI），导出测试结果
import unittest

# webdriver包
from selenium import webdriver

# 创建一个测试类（个人理解：一个测试用例，unittest里的最小执行单位）
# 此句应为unittest框架创建一个测试类的格式，参数为
class RegisterNewUser(unittest.TestCase):

# 添加测试治具，利用setup()方法，创建一个Firefox实例
# 当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
# navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com")


#         添加一个测试方法到test_register_new_user(self) 到RegisterNewUser 类中
    def test_register_new_user(self):
        driver = self.driver

#         click on log in link to open Login page 打开主页后，点击登录按钮
        driver.find_element_by_link_text("My Account").click()

#         创建新账户按钮对用户是否可见且可用
        create_account_button = driver.find_element_by_xpath("//button[@type='button']")
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

#         点击创建账户按钮，通过检查title属性（属于浏览器）
        create_account_button.click()
        self.assertTrue("Create New Customer Account", driver.title)

#         在创建新账户页面，定位所有的元素
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_address = driver.find_element_by_id("email_address")
        news_letter_subscription = driver.find_element_by_id("agree_terms")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmation")
        submit_button = driver.find_element_by_xpath("//button[@title='Submit']")
        customer_company = driver.find_element_by_id("customer_company")
        customer_individual = driver.find_element_by_id("customer_individual")

#        通过get_attribute()方法获取元素的属性值，以及确保元素对用户是可见可用的
#         self.assertEqual("255", first_name.get_attribute("maxlength"))
#         self.assertEqual("255", last_name.get_attribute("maxlength"))
        self.assertTrue(first_name.is_displayed() and last_name.is_displayed() and email_address.is_displayed() and news_letter_subscription.is_displayed() and password.is_displayed() and confirm_password.is_displayed() and news_letter_subscription.is_displayed())
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_address.is_enabled() and news_letter_subscription.is_enabled() and password.is_enabled() and confirm_password.is_enabled() and news_letter_subscription.is_enabled())

#       检查订阅按钮是否被选中，使用is_selected()方法
        self.assertFalse(news_letter_subscription.is_selected())

#       使用clear()清除文本框文本域的内容，使用send_keys()模拟用户输入文本信息

        first_name.send_keys("skr")
        last_name.send_keys("ouch")
        email_address.send_keys("potato@banana.com")
        password.send_keys("abcdefGH123`")
        confirm_password.send_keys("abcdefGH123`")
        news_letter_subscription.click()
        submit_button.click()

#       校验是否注册成功，通过检查text属性

        # self.assertTrue("Hello."+ user +"", driver.find_element_by_css_selector("P.hello > strong").text)
        self.assertTrue(driver.find_element_by_link_text("LogOut").is_displayed())

#       关闭用例

    def tearDown(self):
        self.driver.quit()

#       __name__是指示当前py文件调用方式的方法。如果它等于"__main__"就表示是直接执
if __name__ == "__main__":
    unittest.main(verbosity=2)
