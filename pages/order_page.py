from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # Увеличение таймаута

    def click_order_button_top(self):
        print("Нажатие верхней кнопки 'Заказать'.")
        self.wait.until(EC.element_to_be_clickable(OrderLocators.ORDER_BUTTON_TOP)).click()

    def click_order_button_bottom(self):
        print("Нажатие нижней кнопки 'Заказать'.")
        self.wait.until(EC.element_to_be_clickable(OrderLocators.ORDER_BUTTON_BOTTOM)).click()

    def fill_order_form(self, name, surname, address, metro, phone):
        print("Заполнение формы заказа...")
        try:
            self.wait.until(EC.visibility_of_element_located(OrderLocators.NAME_FIELD)).send_keys(name)
            self.wait.until(EC.visibility_of_element_located(OrderLocators.SURNAME_FIELD)).send_keys(surname)
            self.wait.until(EC.visibility_of_element_located(OrderLocators.ADDRESS_FIELD)).send_keys(address)
            self.wait.until(EC.visibility_of_element_located(OrderLocators.METRO_FIELD)).send_keys(metro)
            self.wait.until(EC.visibility_of_element_located(OrderLocators.PHONE_FIELD)).send_keys(phone)
            self.wait.until(EC.element_to_be_clickable(OrderLocators.NEXT_BUTTON)).click()
            print("Форма заказа заполнена и отправлена.")
            self.driver.save_screenshot("order_form_filled.png")
        except TimeoutException as e:
            print(f"TimeoutException при заполнении формы заказа: {e}")
            self.driver.save_screenshot("order_form_error.png")
            raise

    def fill_rent_form(self, date, rent_period):
        print(f"Форма аренды. Ожидание даты: {date}, периода аренды: {rent_period}")
        self.driver.save_screenshot("pre_rent_form.png")

        # Прокрутка страницы вниз для видимости элемента
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)  # Добавление промежуточного ожидания после прокрутки

        # Проверим, существует ли элемент и виден ли он
        try:
            all_inputs = self.driver.find_elements(By.XPATH, "//input")
            print(f"Все поля ввода на текущей странице: {[input.get_attribute('placeholder') for input in all_inputs]}")
            date_field = self.wait.until(EC.visibility_of_element_located(OrderLocators.DATE_FIELD))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", date_field)  # Прокрутка к элементу
            print("Элемент DATE_FIELD отображается.")
            self.driver.save_screenshot("pre_rent_form_scroll.png")

            date_field.send_keys(date)
            print(f"Форма аренды. Введена дата: {date}")
            self.driver.save_screenshot("date_field_filled.png")

            self.wait.until(EC.element_to_be_clickable(OrderLocators.RENT_DROPDOWN)).click()
            rent_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{rent_period}']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", rent_option)
            rent_option.click()
            print(f"Форма аренды. Введен период: {rent_period}")
            self.driver.save_screenshot("rent_period_selected.png")
            self.wait.until(EC.element_to_be_clickable(OrderLocators.ORDER_FINAL_BUTTON)).click()
        except TimeoutException as e:
            print(f"TimeoutException при заполнении формы аренды: {e}")
            self.driver.save_screenshot("rent_form_error.png")
            raise

    def confirm_order(self):
        print("Подтверждение заказа.")
        try:
            self.wait.until(EC.element_to_be_clickable(OrderLocators.CONFIRM_BUTTON)).click()
        except TimeoutException as e:
            print(f"TimeoutException при подтверждении заказа: {e}")
            self.driver.save_screenshot("confirm_order_error.png")
            raise

    def get_confirm_message(self):
        return self.wait.until(EC.visibility_of_element_located(OrderLocators.CONFIRM_MESSAGE)).text