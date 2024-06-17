import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    edge_browser = webdriver.Edge()
    edge_browser.maximize_window()
    return edge_browser