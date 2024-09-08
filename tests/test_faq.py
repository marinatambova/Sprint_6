import allure
import pytest


@allure.feature("FAQ Section")
@allure.story("FAQ functionality")
class TestFaq:
    @allure.title("Check FAQ response visibility")
    @pytest.mark.parametrize("question_index", range(8))
    def test_faq_questions(self, faq_page, question_index):
        faq_page.open_faq_page()
        assert faq_page.check_faq_answer(question_index), "Ответ на вопрос не отображается при клике"
