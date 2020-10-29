import unittest

from crm.base.browser_operation import BrowserOperation
from crm.base.use_browser import UseBrowser
from crm.webpage.customer_manage.customer_page import Cutomer_page


class Cusstomer_Test(unittest.TestCase):
    def setUp(self):
        self.cp=Cutomer_page()
        self.bo=BrowserOperation(UseBrowser.driver)

    def test_require_add(self):
        self.cp.customer_add(name='burry',Email='123@qq.com',birthday='2002-10-28 18:59:02',AddMan='李四')
        alter=self.bo.alert()
        self.assertEqual('客户添加成功',alter)

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__=='__main__':
    unittest.main()