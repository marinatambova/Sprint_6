from selenium.webdriver.common.by import By

class FaqLocators:
    FAQ_QUESTIONS = [
        (By.XPATH, "//div[@id='accordion__heading-0']"),
        (By.XPATH, "//div[@id='accordion__heading-1']"),
        (By.XPATH, "//div[@id='accordion__heading-2']"),
        (By.XPATH, "//div[@id='accordion__heading-3']"),
        (By.XPATH, "//div[@id='accordion__heading-4']"),
        (By.XPATH, "//div[@id='accordion__heading-5']"),
        (By.XPATH, "//div[@id='accordion__heading-6']"),
        (By.XPATH, "//div[@id='accordion__heading-7']"),
    ]
    FAQ_ANSWERS = [
        (By.XPATH, "//div[@id='accordion__panel-0' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-1' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-2' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-3' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-4' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-5' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-6' and not(@hidden)]"),
        (By.XPATH, "//div[@id='accordion__panel-7' and not(@hidden)]"),
    ]