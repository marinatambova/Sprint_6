import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страницы: {url}")
    def open(self, url):
        """Открывает указанную страницу."""
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск элементов: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Ожидание появления элемента: {locator}")
    def wait_for_element(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_until_visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step("Ввод текста в элемент: {locator}")
    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        element = self.wait_until_visible(locator)
        return element.text

    @allure.step("Проверка наличия элемента: {locator}")
    def is_element_present(self, locator, timeout=2):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Принятие cookies")
    def accept_cookies(self, cookie_locator):
        if self.is_element_present(cookie_locator, timeout=5):
            self.click_element(cookie_locator)

    @allure.step("Ожидание загрузки страницы: {url}")
    def wait_for_page_load(self, url, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url == url)

    @allure.step("Ожидание открытия нового окна")
    def wait_for_new_window(self, number_of_windows):
        self.wait.until(lambda d: len(d.window_handles) == number_of_windows)

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step("Ожидание загрузки URL")
    def wait_for_url_to_load(self):
        self.wait.until(lambda d: d.current_url != "about:blank")

    @allure.step("Проверка наличия строки в текущем URL")
    def is_url_contains(self, string):
        return string in self.driver.current_url
