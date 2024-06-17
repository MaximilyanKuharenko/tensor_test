from selenium.webdriver.common.by import By
from pages.base_page import BasePage

contacs_selector=(By.LINK_TEXT, 'Контакты')
baner_selector=(By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
block_selector=(By.XPATH,'//*[text()="Сила в людях"]')
detail_selector=(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
images_container_selector=(By.XPATH, '//*[@id="container"]/div[1]/div/div[4]')
images_selector=[
    (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/div'),
    (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/div'),
    (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/div'),
    (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/div')
]

class Script1(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open_sbis(self):
        self.browser.get('https://sbis.ru/')

    def open_tensor(self):
        self.browser.get('https://tensor.ru/')

    def contacs(self):
        return self.find(contacs_selector)

    def block(self):
        return self.find(block_selector)

    def baner(self):
        return self.find(baner_selector)

    def detail(self):
        return self.find(detail_selector)

    def container(self):
        return self.find(images_container_selector)

    def image1(self):
        return self.find(images_selector[0])

    def image2(self):
        return self.find(images_selector[1])

    def image3(self):
        return self.find(images_selector[2])

    def image4(self):
        return self.find(images_selector[3])