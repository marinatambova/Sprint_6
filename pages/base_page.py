import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы: {url}")
    def open(self, url):
        """Открывает указанную страницу."""
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск элементов: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание появления элемента: {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        self.wait_for_element(locator).click()

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        else:
            raise Exception("Элемент не найден для скролла")

    @allure.step("Принятие cookies")
    def accept_cookies(self):
        try:
            cookie_button = self.wait_for_element((By.CLASS_NAME, 'App_CookieConsent__1yUIN'), timeout=5)
            self.driver.execute_script("arguments[0].click();", cookie_button)
        except Exception:
            pass

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_for_page_load(self, url, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == url)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
