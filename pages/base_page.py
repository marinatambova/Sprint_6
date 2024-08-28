from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Header_LogoScooter__3lsAR'))).click()

    def go_to_yandex_page(self):
        yandex_logo = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Header_LogoYandex__3TSOI')))
        self.driver.execute_script("arguments[0].click();", yandex_logo)