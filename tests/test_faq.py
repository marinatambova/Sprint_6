# tests/test_faq.py
import allure
import pytest
from pages.faq_page import FaqPage

@allure.feature("FAQ Section")
@allure.story("FAQ functionality")
class TestFaq:
    @allure.title("Check FAQ response visibility")
    @pytest.mark.parametrize("question_locator, answer_locator",
                             list(zip(FaqPage.FAQ_QUESTIONS, FaqPage.FAQ_ANSWERS)))
    def test_faq_questions(self, driver, question_locator, answer_locator):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = FaqPage(driver)
        assert page.check_faq_answer(question_locator, answer_locator), "Ответ на вопрос не отображается при клике"