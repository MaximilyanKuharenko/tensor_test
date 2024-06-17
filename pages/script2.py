from selenium.webdriver.common.by import By
from pages.base_page import BasePage

contacs_selector=(By.LINK_TEXT, 'Контакты')
base_region_selector=(By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
partners_selector=(By.XPATH,'//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
city_selector=(By.XPATH,'//*[@id="city-id-2"]')
change_reg_selector=(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[42]/span')

class Script2(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open_sbis(self):
        self.browser.get('https://sbis.ru/')

    def open_tensor(self):
        self.browser.get('https://tensor.ru/')

    def contacs(self):
        return self.find(contacs_selector)

    def base_region(self):
        return self.find(base_region_selector)

    def partners(self):
        return self.find(partners_selector)

    def city(self):
        return self.find(city_selector)

    def change_reg(self):
        return self.find(change_reg_selector)
