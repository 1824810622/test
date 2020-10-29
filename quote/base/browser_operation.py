from selenium.webdriver.chrome import webdriver

from quote.base.usebrowser import UseBrowser


class BrowserOperation:
    def __init__(self,driver):
        self.driver=driver
        # self.bo=BrowserOperation(UseBrowser.drive)

    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url address error')

    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'element not found')

    def element_click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'element not found')

    def get_text(self,xpath):
        try:
            text=self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'element error')

        return text

    def switch_frame(self,frame_name):
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(frame_name)

    def switch_window(self,window_name):
        for window_hd in self.driver.window_handles:
            self.driver.switch_to.window(window_hd)
            if self.driver.title==window_name:
                break

# if __name__=='__main__':
#     ub=UseBrowser()
#     bo=BrowserOperation(UseBrowser.drive)
#     bo.open_url('http://localhost:8080/JavaPrj_6/')
#     bo.send_keys('//*[@id="UserName"]','admin')
#     bo.send_keys('//*[@id="Password"]','123456')
