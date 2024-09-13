import os
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Нажатие на верхнюю кнопку заказа")
    def click_order_button_top(self):
        self.accept_cookies(OrderLocators.COOKIE_LOCATOR)
        self.click_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажатие на нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        self.accept_cookies(OrderLocators.COOKIE_LOCATOR)
        self.click_element(OrderLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнение формы заказа: имя - {0}, фамилия - {1}, адрес - {2}, метро - {3}, телефон - {4}")
    def fill_order_form(self, name, surname, address, metro, phone):
        self.send_keys(OrderLocators.NAME_FIELD, name)
        self.send_keys(OrderLocators.SURNAME_FIELD, surname)
        self.send_keys(OrderLocators.ADDRESS_FIELD, address)
        self.click_element(OrderLocators.METRO_FIELD)
        self.send_keys(OrderLocators.METRO_FIELD, metro)
        self.click_element(OrderLocators.STATION_CHILD)
        self.send_keys(OrderLocators.PHONE_FIELD, phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнение формы аренды: дата - {0}, срок - {1}")
    def fill_rent_form(self, date, rent_period):
        try:
            self.send_keys(OrderLocators.DATE_FIELD, date)
            self.send_keys(OrderLocators.DATE_FIELD, Keys.RETURN)
            self.click_element(OrderLocators.RENT_DROPDOWN)
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
        screenshot_path = os.path.join(os.getcwd(), "error_screenshot.png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name='Скриншот', attachment_type=allure.attachment_type.PNG)

        html_path = os.path.join(os.getcwd(), "error_page.html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        allure.attach.file(html_path, name='Исходный код страницы', attachment_type=allure.attachment_type.HTML)
