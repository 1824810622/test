from crm.base.dboperation import DBoperation
from crm.log.new_log_script import Auto_log
from crm.until.yaml import Yamloption
from crm.webpage.user_manage.user_login_page import Login_page
import time
import re
class Cutomer_page:
    def __init__(self):
        self.lp=Login_page()
        self.lp.login('admin','123456')
        self.yaml = Yamloption('../../config/test.yaml')
        self.log = Auto_log()
        self.dboperation=DBoperation()

    def customer_add(self ,**kwargs):
        self.input_value=kwargs
        time.sleep(2)
        self.dboperation.delet("delete from customer_info where customer_name='burry';")
        self.log.set_message('--添加用户--','info')
        self.lp.bo.switch_frame(self.yaml.get_locat('LoginPage','frame_name'))
        self.lp.bo.element_click(self.yaml.get_locat('LoginPage','cus_button'))
        self.lp.bo.switch_frame('mainFrame')
        self.lp.bo.element_click(self.yaml.get_locat('LoginPage','cus_add'))
        time.sleep(2)
        self.lp.bo.send_keys(self.yaml.get_locat('LoginPage','cus_name')
                             ,kwargs.get('name', ''))
        self.log.set_message('--input客户name--:'+kwargs.get('name', ''), 'info')
        self.lp.bo.send_keys(self.yaml.get_locat('LoginPage','cus_Email')
                             ,kwargs.get('Email', ''))
        self.log.set_message('--input客户Email--:'+kwargs.get('Email', ''), 'info')
        self.lp.bo.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.lp.bo.send_keys(self.yaml.get_locat('LoginPage','cus_birth')
                             ,kwargs.get('birthday', ''))
        self.log.set_message('--input客户birthday--:'+kwargs.get('birthday', ''), 'info')
        self.lp.bo.send_keys(self.yaml.get_locat('LoginPage','cus_addman')
                             ,kwargs.get('AddMan', ''))
        self.log.set_message('--input添加人--:'+kwargs.get('AddMan', ''), 'info')
        time.sleep(2)
        self.lp.bo.element_click(self.yaml.get_locat('LoginPage','add_submit'))

    def cus_search(self):
        alert_text = self.lp.bo.get_alert_text()
        self.lp.bo.alert_clicked()
        self.lp.bo.change_frame(self.lp.yp.get_locator('CustomerPage', 'leftFrame'))
        time.sleep(2)
        self.lp.bo.click_element(self.lp.yp.get_locator('CustomerPage', 'customer_care'))
        time.sleep(2)
        self.lp.bo.change_frame('mainFrame')
        res_s = self.lp.bo.get_text(self.lp.yp.get_locator('CustomerPage', 'result'))
        lst = re.findall('有 (\d+)条', res_s)
        number = int(lst[0])
        print(self.lp.bo.get_text(self.lp.yp.get_locator('CustomerPage', 'form_res').format(str(number))))
        name_text = self.lp.bo.get_text(self.lp.yp.get_locator('CustomerPage', 'form_res').format(str(number)))

        if alert_text == '客户添加成功' and name_text == self.input_value.get('customer_name'):
            return True
        return False