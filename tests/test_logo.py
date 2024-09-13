import allure


@allure.feature("Logo Functionality")
@allure.story("Verify logo redirects")
class TestLogo:
    @allure.title("Проверка перехода по логотипу 'Яндекса'")
    def test_yandex_logo_redirect(self, faq_page):
        faq_page.open_faq_page()
        faq_page.click_yandex_logo()
        assert faq_page.is_dzen_url_loaded(), "Переход на главную страницу Дзена не произошел"

    @allure.title("Проверка перехода по логотипу 'Самокат'")
    def test_scooter_logo_redirect(self, faq_page):
        faq_page.open_faq_page()
        faq_page.click_scooter_logo()
        assert faq_page.is_scooter_url_loaded(), "Переход на главную страницу Самоката не произошел"
