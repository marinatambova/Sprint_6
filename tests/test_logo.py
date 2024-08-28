import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature('Logo Functionality')
@allure.story('Verify logo redirects')
@allure.title('Проверка перехода по логотипу "Яндекса" на главную страницу Дзена')
def test_yandex_logo_redirect(driver):
    base_url = 'https://qa-scooter.praktikum-services.ru/'
    driver.get(base_url)
    page = BasePage(driver)

    page.go_to_yandex_page()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

    WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
    assert "dzen.ru" in driver.current_url, f"Переход на главную страницу Дзена не произошел, текущий URL: {driver.current_url}"