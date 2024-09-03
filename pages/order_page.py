# pages/order_page.py
import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.order_locators import OrderLocators
import os

class OrderPage(BasePage):
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать')][2]")
    ORDER_CONFIRM_MESSAGE = (By.CLASS_NAME, "Order_Confirmed_text")

    @allure.step("Clicking on the top order button")
    def click_order_button_top(self):
        self.accept_cookies()
        self.click_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step("Clicking on the bottom order button")
    def click_order_button_bottom(self):
        self.accept_cookies()
        self.click_element(OrderLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Filling the order form with name: {0}, surname: {1}, address: {2}, metro: {3}, phone: {4}")
    def fill_order_form(self, name, surname, address, metro, phone):
        self.wait_for_element(OrderLocators.NAME_FIELD).send_keys(name)
        self.wait_for_element(OrderLocators.SURNAME_FIELD).send_keys(surname)
        self.wait_for_element(OrderLocators.ADDRESS_FIELD).send_keys(address)
        self.wait_for_element(OrderLocators.METRO_FIELD).send_keys(metro)
        self.wait_for_element(OrderLocators.PHONE_FIELD).send_keys(phone)
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Filling the rent form with date: {0}, period: {1}")
    def fill_rent_form(self, date, rent_period):
        try:
            date_field = self.wait_for_element(OrderLocators.DATE_FIELD, timeout=20)
            self.scroll_to_element(date_field)
            date_field.send_keys(date)
            self.click_element(OrderLocators.RENT_DROPDOWN)

            rent_option = self.wait_for_element((By.XPATH, f"//*[contains(text(), '{rent_period}')]"))
            self.scroll_to_element(rent_option)
            rent_option.click()
            self.click_element(OrderLocators.ORDER_FINAL_BUTTON)
        except Exception as e:
            self.driver.save_screenshot(os.path.join(os.getcwd(), "error_screenshot.png"))
            with open(os.path.join(os.getcwd(), "error_page.html"), "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise e

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Confirming order")
    def confirm_order(self):
        self.click_element(OrderLocators.CONFIRM_BUTTON)

    @allure.step("Getting confirmation message")
    def get_confirm_message(self):
        return self.get_element_text(OrderLocators.CONFIRM_MESSAGE)