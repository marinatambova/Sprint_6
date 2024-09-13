from selenium.webdriver.common.by import By


class FaqLocators:
    FAQ_QUESTIONS = [
        (By.XPATH, f"//div[contains(@class, 'accordion__item')][{i}]//div[contains(@class, 'accordion__button')]")
        for i in range(1, 9)
    ]
    FAQ_ANSWERS = [
        (By.XPATH, f"//div[contains(@class, 'accordion__item')][{i}]//div[contains(@class, 'accordion__panel')]")
        for i in range(1, 9)
    ]
