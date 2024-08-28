from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class, 'Button_Button__ra12g')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class, 'Button_Middle__1CSJM')]")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    ORDER_FINAL_BUTTON = (By.XPATH, "//button[contains(text(),'Заказать') and contains(@class, 'Button_Middle__1CSJM')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRM_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")