from selenium.webdriver.common.by import By


class OrderLocators:
    COOKIE_LOCATOR = (By.ID, "rcc-confirm-button")
    ORDER_CONFIRM_MESSAGE = (By.CLASS_NAME, "Order_Confirmed_text")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(text(), 'Заказать')][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    ORDER_FINAL_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[last()]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    CONFIRM_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    STATION_CHILD = (By.CSS_SELECTOR, "ul.select-search__options > li:first-child button")
    RENT_PERIOD_OPTION = "//div[@class='Dropdown-option' and text()='{}']"
