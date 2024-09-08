# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from pages.faq_page import FaqPage


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Укажите правильный путь к Firefox
    service = Service(executable_path=r'geckodriver.exe')
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def faq_page(driver):
    return FaqPage(driver)
