import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.script1 import Script1

def test_test1(browser):
    script1_page = Script1(browser)
    script1_page.open_sbis()
    contacs = script1_page.contacs()
    contacs.click()
    baner = script1_page.baner()
    baner.click()
    script1_page.open_tensor()
    assert script1_page.block().is_displayed(),"Блок 'Сила в людях' не найден"

def test_test2(browser):
    script1_page = Script1(browser)
    script1_page.open_tensor()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div')))
    detail = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div')
    ActionChains(browser).scroll_to_element(detail).click().perform()
    sleep(2)
    detail = script1_page.detail()
    detail.click()
    sleep(2)
    get_url=browser.current_url
    assert get_url == "https://tensor.ru/about", "url не совпадает"
    detail = script1_page.container()
    ActionChains(browser).scroll_to_element(detail).click().perform()
    sleep(2)
    image1 = script1_page.image1()
    image2 = script1_page.image2()
    image3 = script1_page.image3()
    image4 = script1_page.image4()
    assert image1.size == image2.size == image3.size == image4.size, "Размеры фотографий разные"




