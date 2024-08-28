import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.faq_page import FaqPage
from locators.faq_locators import FaqLocators


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.feature('FAQ Section')
@allure.story('Verify FAQ functionality')
@allure.title('Проверка открытия текста FAQ вопросы о важном')
@pytest.mark.parametrize("question_locator, answer_locator",
                         list(zip(FaqLocators.FAQ_QUESTIONS, FaqLocators.FAQ_ANSWERS)))
def test_faq_questions(driver, question_locator, answer_locator):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    page = FaqPage(driver)

    assert page.check_faq_answer(question_locator, answer_locator), "Ответ на вопрос не отображается при клике"