from time import sleep
from selenium.webdriver.common.by import By
from pages.script2 import Script2


def test2_test1(browser):
    script2_page=Script2(browser)
    script2_page.open_sbis()
    contacs = script2_page.contacs()
    contacs.click()
    region=script2_page.base_region()
    assert region.text == "Калининградская обл.", "Определился другой регион"

    partners=script2_page.partners()
    assert partners.is_enabled(), "Списка партнеров нет"

    city=script2_page.city()
    partners_city=[city.text]
    region.click()
    sleep(0.5)
    change=script2_page.change_reg()
    reg_number=change.text[:2]
    reg_number=str(reg_number)
    new_reg=change.text[3:]
    new_reg = new_reg.split(" ")[0]
    change.click()
    sleep(0.5)
    city=script2_page.city()
    partners_city.append(city.text)
    assert partners_city[0] != partners_city[1], "Выбранный регион не подставился"

    page_titel=browser.title
    assert new_reg in page_titel, "title содержит информацию выбранного региона"

    page_url=str(browser.current_url)
    assert reg_number in page_url, "url содержит информацию выбранного региона"