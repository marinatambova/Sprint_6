# tests/test_order.py
import allure
import pytest
from pages.order_page import OrderPage

@allure.feature("Order Scooter")
@allure.story("Scooter order functionality")
class TestOrder:
    @allure.title("Order scooter from top button")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, rent_period",
        [
            ("Иван", "Иванов", "Улица Пушкина, дом Колотушкина", "Киевская", "+79991112233", "20.10.2023", "сутки"),
            ("Пётр", "Петров", "Улица Ленина, дом Сталина", "Арбатская", "+79993334455", "21.10.2023", "двое суток")
        ]
    )
    def test_order_scooter_top_button(self, driver, name, surname, address, metro, phone, date, rent_period):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = OrderPage(driver)
        page.click_order_button_top()
        page.fill_order_form(name, surname, address, metro, phone)
        page.fill_rent_form(date, rent_period)
        page.confirm_order()
        assert "Заказ оформлен" in page.get_confirm_message(), "Подтверждающее сообщение не найдено"

    @allure.title("Order scooter from bottom button")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, rent_period",
        [
            ("Сергей", "Сергеев", "Улица Чехова, дом Гудкова", "Тверская", "+79996667788", "22.10.2023", "четверо суток"),
            ("Алексей", "Алексеев", "Улица Достоевского, дом Книжников", "Садовая", "+79997778899", "23.10.2023", "двое суток")
        ]
    )
    def test_order_scooter_bottom_button(self, driver, name, surname, address, metro, phone, date, rent_period):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        page = OrderPage(driver)
        page.click_order_button_bottom()
        page.fill_order_form(name, surname, address, metro, phone)
        page.fill_rent_form(date, rent_period)
        page.confirm_order()
        assert "Заказ оформлен" in page.get_confirm_message(), "Подтверждающее сообщение не найдено"