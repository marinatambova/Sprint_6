# tests/test_logo.py
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.common_locators import CommonLocators


@allure.feature("Logo Functionality")
@allure.story("Verify logo redirects")
class TestLogo:
    @allure.title("Проверка перехода по логотипу 'Яндекса'")
    def test_yandex_logo_redirect(self, driver):
        base_url = 'https://qa-scooter.praktikum-services.ru/'
        driver.get(base_url)
        page = BasePage(driver)

        # Исправление имени атрибута
        page.click_element(CommonLocators.YANDEX_LOGO)

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])

        WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
        assert "dzen.ru" in driver.current_url, f"Переход на главную страницу Дзена не произошел, текущий URL: {driver.current_url}"

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_scooter_logo_redirect(self, driver):
        base_url = 'https://qa-scooter.praktikum-services.ru/'
        driver.get(base_url)
        page = BasePage(driver)
        page.click_element(CommonLocators.SCOOTER_LOGO)

        assert driver.current_url == base_url, f"Переход на главную страницу Самоката не произошел, текущий URL: {driver.current_url}"