from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FaqPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_faq_answer(self, question_locator, answer_locator):
        question_element = self.driver.find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        self.driver.execute_script("arguments[0].click();", question_element)
        return self.wait.until(EC.visibility_of_element_located(answer_locator)).is_displayed()