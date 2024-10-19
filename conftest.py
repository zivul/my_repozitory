import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def set_up():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(60)
    driver.maximize_window()
    yield driver
    driver.quit()
