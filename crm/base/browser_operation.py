from selenium.webdriver.common.alert import Alert


class BrowserOperation:
    def __init__(self,driver):
        self.driver=driver


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e, 'url address error')

    def element_click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e,'click error')

    def send_keys(self,path,content):
        try:
            self.driver.find_element_by_xpath(path).send_keys(content)
        except Exception as e:
            print(e,'element not found')

    def get_text(self,path):
        try:
            text=self.driver.find_element_by_xpath(path).text
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

    def get_image(self,xpath):
        image = self.driver.find_element_by_xpath(xpath).value_of_css_property('background')
        return image
    def alert(self):
        alert=Alert(self.driver).text
        return alert

    def get_alert_text(self):
        pass

