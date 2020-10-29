
import  unittest

from quote.base.browser_operation import BrowserOperation
from quote.base.usebrowser import UseBrowser
from quote.wbepage.customermanager.customerpage import CustomerPage


class Customer_test(unittest.TestCase):
    def setUp(self):
        self.cp=CustomerPage()
        self.bo=BrowserOperation(UseBrowser.drive)


    def test_customer_add_only_id(self):
        self.cp.customer_add(id='233qwer')
        text=self.bo.get_text('/html/body/center')
        self.assertEqual(text,'添加记录成功！\n本窗口将在3秒后自动关闭')

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__=='__main__':
    unittest.main()