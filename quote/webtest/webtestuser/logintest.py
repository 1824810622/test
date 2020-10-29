import sys
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

from quote.base.browser_operation import BrowserOperation
from quote.base.usebrowser import UseBrowser
from quote.wbepage.usermanager.loginpage import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
       self.login=LoginPage()
       self.bo=BrowserOperation(UseBrowser.drive)

    def test_null(self):
        self.login.login('','')
        self.assertEqual(self.bo.get_text('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td'),'请勿非法登录！')

    def test_suessed(self):
        self.login.login('admin', 'admin')
        value=self.login.login_correct_text('main','/html/body/table/tbody/tr[1]/td/span')
        self.assertEqual(value,'欢迎使用报价管理系统')

    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__=='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    data_time = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
        runner.run(suite)