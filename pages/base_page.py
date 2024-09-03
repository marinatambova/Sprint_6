# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def accept_cookies(self):
        try:
            cookie_button = self.wait_for_element((By.CLASS_NAME, 'App_CookieConsent__1yUIN'), timeout=5)
            self.driver.execute_script("arguments[0].click();", cookie_button)
        except Exception:
            pass