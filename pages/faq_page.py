import allure
from locators.common_locators import CommonLocators
from locators.order_locators import OrderLocators
from locators.faq_locators import FaqLocators
from pages.base_page import BasePage


class FaqPage(BasePage):

    @allure.step("Открытие страницы FAQ")
    def open_faq_page(self):
        self.open("https://qa-scooter.praktikum-services.ru/")

    @allure.step("Проверка видимости ответа на вопрос {question_index}")
    def check_faq_answer(self, question_index):
        question_locator = FaqLocators.FAQ_QUESTIONS[question_index]
        answer_locator = FaqLocators.FAQ_ANSWERS[question_index]

        question_element = self.find_element(question_locator)
        self.scroll_to_element(question_element)
        self.accept_cookies(OrderLocators.COOKIE_LOCATOR)
        self.click_element(question_locator)
        answer_element = self.wait_until_visible(answer_locator)
        return answer_element.is_displayed()

    @allure.step("Нажатие на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(CommonLocators.YANDEX_LOGO)
        self.wait_for_new_window(2)
        self.switch_to_new_window()

    @allure.step("Нажатие на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(CommonLocators.SCOOTER_LOGO)

    @allure.step("Проверка загрузки страницы Дзена")
    def is_dzen_url_loaded(self):
        self.wait_for_url_to_load()
        return self.is_url_contains("dzen.ru")
