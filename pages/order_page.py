import os

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Нажатие на верхнюю кнопку заказа")
    def click_order_button_top(self):
        self.accept_cookies()
        self.click_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажатие на нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        self.accept_cookies()
        # self.scroll_to_element(OrderLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(OrderLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнение формы заказа: имя - {0}, фамилия - {1}, адрес - {2}, метро - {3}, телефон - {4}")
    def fill_order_form(self, name, surname, address, metro, phone):
        self.wait_for_element(OrderLocators.NAME_FIELD).send_keys(name)
        self.wait_for_element(OrderLocators.SURNAME_FIELD).send_keys(surname)
        self.wait_for_element(OrderLocators.ADDRESS_FIELD).send_keys(address)
        self.click_element(OrderLocators.METRO_FIELD)
        self.wait_for_element(OrderLocators.METRO_FIELD).send_keys(metro)
        self.wait_for_element(OrderLocators.STATION_CHILD).click()
        self.wait_for_element(OrderLocators.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнение формы аренды: дата - {0}, срок - {1}")
    def fill_rent_form(self, date, rent_period):
        try:
            date_field = self.wait_for_element(OrderLocators.DATE_FIELD, timeout=20)
            self.scroll_to_element(date_field)
            date_field.send_keys(date)
            date_field.send_keys(Keys.RETURN)
            self.click_element(OrderLocators.RENT_DROPDOWN)

            rent_option = self.wait_for_element((By.XPATH, OrderLocators.RENT_PERIOD_OPTION.format(rent_period)))
            self.scroll_to_element(rent_option)
            self.click_element((By.XPATH, OrderLocators.RENT_PERIOD_OPTION.format(rent_period)))
            self.click_element(OrderLocators.ORDER_FINAL_BUTTON)
        except Exception as e:
            self.take_screenshot_and_html()
            raise e

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_element(OrderLocators.CONFIRM_BUTTON)

    @allure.step("Получение сообщения о подтверждении заказа")
    def get_confirm_message(self):
        return self.get_element_text(OrderLocators.CONFIRM_MESSAGE)

    @allure.step("Создание скриншота и сохранение HTML при ошибке")
    def take_screenshot_and_html(self):
        # Сделать скриншот
        screenshot_path = os.path.join(os.getcwd(), "error_screenshot.png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name='Скриншот', attachment_type=allure.attachment_type.PNG)

        # Сохранить исходный код страницы
        html_path = os.path.join(os.getcwd(), "error_page.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(html_path, name='Исходный код страницы', attachment_type=allure.attachment_type.HTML)

    @allure.step("Принятие cookies")
    def accept_cookies(self):
        if self.is_element_present(OrderLocators.COOKIE_LOCATOR):
            self.click_element(OrderLocators.COOKIE_LOCATOR)

    @allure.step("Проверка наличия элемента: {locator}")
    def is_element_present(self, locator, timeout=2):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
