import allure
import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from time import sleep

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@allure.feature('Order Scooter')
@allure.story('User can order a scooter')
@allure.title('Позитивный сценарий заказа самоката: верхняя кнопка заказа')
@pytest.mark.parametrize(
    "name, surname, address, metro, phone, date, rent_period",
    [
        ("Иван", "Иванов", "Улица Пушкина, дом Колотушкина", "Киевская", "+79991112233", "20.10.2023", "четверо суток"),
        ("Пётр", "Петров", "Улица Ленина, дом Сталина", "Арбатская", "+79993334455", "21.10.2023", "сутки")
    ]
)
def test_order_scooter_top_button(driver, name, surname, address, metro, phone, date, rent_period):
    driver.get('https://qa-scooter.praktikum-services.ru/')
    page = OrderPage(driver)

    try:
        page.click_order_button_top()
        page.fill_order_form(name, surname, address, metro, phone)
        sleep(3)
    except Exception as e:
        print(f"Ошибка при заполнении формы заказа: {e}")
        driver.save_screenshot("order_form_error.png")
        raise

    try:
        page.fill_rent_form(date, rent_period)
        sleep(3)
    except Exception as e:
        print(f"Ошибка при заполнении формы аренды: {e}")
        driver.save_screenshot("rent_form_error.png")
        raise

    try:
        page.confirm_order()
        confirm_message = page.get_confirm_message()
        assert "Заказ оформлен" in confirm_message, "Подтверждающее сообщение не найдено"
    except Exception as e:
        print(f"Ошибка при подтверждении заказа: {e}")
        driver.save_screenshot("confirm_order_error.png")
        raise