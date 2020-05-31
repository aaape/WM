from .my_unit import StartEnd
from businessView.loginView import LoginView
import logging

class Login_case(StartEnd):
    csv_file = '../data/data.csv'
    def account1_login(self):
        self.setUp()
        l = LoginView(self.driver)
        cf = l.get_data(self.csv_file,2)
        l.login(cf[0],cf[1])
        self.assertTrue(l.check_login_status())