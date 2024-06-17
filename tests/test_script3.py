import os
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.script3 import Script3
from selenium import webdriver
import pytest

download_folder = "C:\down"

@pytest.fixture()
def browser():
    edge_options = webdriver.EdgeOptions()
    prefs = {"download.default_directory": download_folder}
    edge_options.add_experimental_option("prefs", prefs)
    chrome_browser = webdriver.Edge(options=edge_options)
    return chrome_browser

def test3_test1(browser):
    script3_page=Script3(browser)
    script3_page.open_sbis()
    sleep(1)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[5]')))
    footer = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[5]')
    ActionChains(browser).scroll_to_element(footer).click().perform()
    browser.execute_script("arguments[0].scrollIntoView(true);", footer)
    sleep(1)

    downl=script3_page.down_link()
    downl.click()
    sleep(1)
    installer=script3_page.installer()
    installer.click()
    sleep(10)

    downloaded_file_path = os.path.join(download_folder, "sbisplugin-setup-web.exe")
    assert os.path.exists(downloaded_file_path), "Файл не был установлен"

    file_size = round(os.path.getsize(downloaded_file_path)/(1024*1024),2)
    assert file_size==7.22 , "Размер файла не совпадает"