import pytest
import allure
from pages.order_page import OrderPage


@pytest.mark.usefixtures("driver")
class TestOrder:

    @allure.title("Заказ самоката через верхнюю кнопку")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, rent_period",
        [
            ("Иван", "Иванов", "Улица Пушкина, дом Колотушкина", "Киевская", "+79991112233", "20.10.2023", "сутки"),
            ("Пётр", "Петров", "Улица Ленина, дом Сталина", "Арбатская", "+79993334455", "21.10.2023", "двое суток")
        ]
    )
    def test_order_scooter_top_button(self, driver, name, surname, address, metro, phone, date, rent_period):
        # Открываем страницу
        page = OrderPage(driver)
        page.open('https://qa-scooter.praktikum-services.ru/')

        # Нажимаем на верхнюю кнопку заказа
        page.click_order_button_top()

        # Заполняем форму заказа
        page.fill_order_form(name, surname, address, metro, phone)

        # Заполняем данные аренды
        page.fill_rent_form(date, rent_period)

        # Подтверждаем заказ
        page.confirm_order()

        # Проверяем сообщение о подтверждении
        confirmation_message = page.get_confirm_message()
        assert "Заказ оформлен" in confirmation_message, "Заказ не был успешно подтверждён"

    @allure.title("Заказ самоката через нижнюю кнопку")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, rent_period",
        [
            ("Сергей", "Сергеев", "Улица Чехова, дом Гудкова", "Тверская", "+79996667788", "22.10.2023",
             "четверо суток"),
            ("Алексей", "Алексеев", "Улица Достоевского, дом Книжников", "Тверская", "+79997778899", "23.10.2023",
             "двое суток")
        ]
    )
    def test_order_scooter_bottom_button(self, driver, name, surname, address, metro, phone, date, rent_period):
        # Открываем страницу
        page = OrderPage(driver)
        page.open('https://qa-scooter.praktikum-services.ru/')

        # Нажимаем на нижнюю кнопку заказа
        page.click_order_button_bottom()

        # Заполняем форму заказа
        page.fill_order_form(name, surname, address, metro, phone)

        # Заполняем данные аренды
        page.fill_rent_form(date, rent_period)

        # Подтверждаем заказ
        page.confirm_order()

        # Проверяем сообщение о подтверждении
        confirmation_message = page.get_confirm_message()
        assert "Заказ оформлен" in confirmation_message, "Заказ не был успешно подтверждён"
