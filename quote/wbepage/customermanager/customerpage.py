from quote.wbepage.usermanager.loginpage import LoginPage

import time
class CustomerPage:
    def __init__(self):
        self.lp=LoginPage()
        self.lp.login('admin','admin')


    def customer_add(self,**kwargs):
        time.sleep(2)
        self.lp.bo.switch_frame('Links')
        self.lp.bo.element_click('//*[@id="Bar_panel0_b0"]/img')
        self.lp.bo.switch_frame('main')
        self.lp.bo.element_click('/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        time.sleep(2)
        self.lp.bo.switch_window('新增客户信息')
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input',kwargs.get('id',''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/input',kwargs.get('name', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input',kwargs.get('tel', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input',kwargs.get('address', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input',kwargs.get('relationman', ''))
        self.lp.bo.send_keys('/html/body/center/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[4]/input',kwargs.get('other', ''))
        time.sleep(2)
        self.lp.bo.element_click('/html/body/center/form/table[2]/tbody/tr/td/input[1]')


    def customer_modify(self):
        pass

# if __name__=='__main__':
#     cp=CustomerPage()
#     cp.customer_add(id='12345',name='kk')