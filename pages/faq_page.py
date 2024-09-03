# pages/faq_page.py
import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FaqPage(BasePage):
    FAQ_QUESTIONS = [
        (By.XPATH, f"//div[contains(@class, 'accordion__item')][{i}]//div[contains(@class, 'accordion__button')]") for i
        in range(1, 9)]
    FAQ_ANSWERS = [
        (By.XPATH, f"//div[contains(@class, 'accordion__item')][{i}]//div[contains(@class, 'accordion__panel')]") for i
        in range(1, 9)]

    @allure.step("Returning {0} response visibility status.")
    def check_faq_answer(self, question_locator, answer_locator):
        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        self.accept_cookies()
        self.driver.execute_script("arguments[0].click();", question_element)
        # Добавим ожидание, чтобы убедиться, что ответ открыт
        answer_element = self.wait_until_visible(answer_locator)
        return answer_element.is_displayed()

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))