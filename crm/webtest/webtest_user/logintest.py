import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('C:\\Users\\ASUS\\PycharmProjects\\pythonProject')
import re
from crm.base.browser_operation import BrowserOperation
from crm.base.use_browser import UseBrowser
from crm.until.excel_1 import OperationExcel
from crm.webpage.user_manage.user_login_page import Login_page
import time

class Logintest(unittest.TestCase):
    def setUp(self) -> None:
        self.login=Login_page()
        self.bo=BrowserOperation(UseBrowser.driver)
        self.op = OperationExcel('../../config/test.xlsx', '用例参数')

    def test_login_1(self):
        self.login.login(self.op.get_cell(1, 2), self.op.get_cell(1, 3))
        self.assertEqual(self.op.get_cell(1, 4),self.bo.alert())

    def test_login_2(self):
        self.login.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
        self.assertEqual(self.op.get_cell(2, 4),self.bo.alert())
    #
    def test_login_3(self):
        self.login.login(self.op.get_cell(3, 2), self.op.get_cell(3, 3))
        self.assertEqual(self.op.get_cell(3, 4), self.bo.alert())

    def test_login_4(self):
        self.login.login(self.op.get_cell(4, 2), self.op.get_cell(4, 3))
        self.assertEqual(self.op.get_cell(4, 4), self.bo.alert())

    def test_login_5(self):
        self.login.login(self.op.get_cell(5, 2), self.op.get_cell(5, 3))
        # text=self.login.login_correct_text('mainFrame','/html/body/form/table/tbody/tr[1]/td[1]')
        # self.assertEqual('关怀提醒',text)
        self.bo.switch_frame('topFrame')
        image = self.bo.get_image('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]')
        image_info = re.search('main_09.gif',image).group()
        self.assertEqual('main_09.gif', image_info)

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__=='__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(Logintest)
    suite.addTests(test_case)
    data_time = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
        runner.run(suite)