# import time

from quote.base.browser_operation import BrowserOperation
from quote.base.usebrowser import UseBrowser


class LoginPage:

    def __init__(self):
        self.ub=UseBrowser()
        self.bo=BrowserOperation(UseBrowser.drive)
        self.bo.open_url('http://localhost:8080/JavaPrj_6/')

    def login(self,username='',password=''):
        self.bo.send_keys('//*[@id="UserName"]',username)
        self.bo.send_keys('//*[@id="Password"]',password)
        self.bo.element_click('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')

    def login_correct_text(self, frame_name, xpath):
        self.bo.switch_frame(frame_name)
        return self.bo.get_text(xpath)


# if __name__=='__main__':
#     lp=LoginPage()
#     lp.login()
#     time.sleep(3)
#     UseBrowser.quit()