from selenium import webdriver
import time
class UseBrowser:
    drive = None

    def __init__(self):
        self.drive = webdriver.Chrome('../chromedriver.exe')
        self.drive.maximize_window()
        self.drive.implicitly_wait(10)
        UseBrowser.drive=self.drive

    @classmethod
    def quit(cls):
        UseBrowser.drive.quit()

# if __name__ == '__main__':
#     ub=UseBrowser()
#     time.sleep(2)



