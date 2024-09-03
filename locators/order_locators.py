# locators/order_locators.py
from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать')][2]")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CLASS_NAME, "select-search__input")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    ORDER_FINAL_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')][2]")  # Исправьте, если позиция не верная
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    CONFIRM_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")