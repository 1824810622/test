

from crm.base.browser_operation import BrowserOperation
from crm.base.use_browser import UseBrowser
from crm.log.new_log_script import Auto_log

from crm.until.yaml import Yamloption


class Login_page:

    def __init__(self):
        self.log = Auto_log()
        self.ub=UseBrowser()
        self.bo=BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://localhost:8080/crm/login.jsp')
        self.yaml = Yamloption('../../config/test.yaml')


    def login(self,username='',password=''):
        self.log.set_message('--登录开始--','info')
        self.bo.send_keys(self.yaml.get_locat('LoginPage','username'),username)
        self.log.set_message('input username:'+username,'info')
        self.bo.send_keys(self.yaml.get_locat('LoginPage','password'),password)
        self.log.set_message('input password:'+password,'info')
        self.bo.element_click(self.yaml.get_locat('LoginPage','login'))

    def login_correct_text(self, frame_name, xpath):
        self.bo.switch_frame(frame_name)
        return self.bo.get_text(xpath)














