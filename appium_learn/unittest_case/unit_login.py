from unittest_case.unit import StartEnd
from unittest_case.loginView import LoginView
import unittest
import logging

class Testlogin(StartEnd):
    logging.info('test_login_abc')

    def test_login_case(self):
        l = LoginView(self.driver)
        l.login_action('abc123','123456')

    def teest_login_demo(self):
        l = LoginView(self.driver)
        l.login_action('567','1234')

if __name__ == '__main__':
    unittest.main()