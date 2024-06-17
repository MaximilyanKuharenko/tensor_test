from selenium.webdriver.common.by import By
from pages.base_page import BasePage

down_selector=(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a')
installer_selector=(By.XPATH, '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')

class Script3(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open_sbis(self):
        self.browser.get('https://sbis.ru/')

    def open_tensor(self):
        self.browser.get('https://tensor.ru/')

    def down_link(self):
        return self.find(down_selector)

    def installer(self):
        return self.find(installer_selector)