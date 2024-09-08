import allure
from locators.common_locators import CommonLocators
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
        self.accept_cookies()
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

    @allure.step("Ожидание открытия новой вкладки")
    def wait_for_new_window(self, number_of_windows):
        self.wait.until(lambda d: len(d.window_handles) == number_of_windows)

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step("Ожидание загрузки URL")
    def wait_for_url_to_load(self):
        self.wait.until(lambda d: d.current_url != "about:blank")

    @allure.step("Проверка загрузки страницы Дзена")
    def is_dzen_url_loaded(self):
        self.wait_for_url_to_load()
        return "dzen.ru" in self.driver.current_url

    @allure.step("Проверка загрузки главной страницы Самоката")
    def is_scooter_url_loaded(self):
        return self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
