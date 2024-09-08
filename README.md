# Project Sprint_6

Этот проект содержит автотесты для учебного сервиса «Яндекс.Самокат» с использованием Selenium, Page Object Model (POM) и Allure для отчетов.

## Структура проекта

- **locators**: Содержит локаторы для различных элементов страниц.
  - `faq_locators.py`
  - `order_locators.py`
  - `common_locators.py`
- **pages**: Содержит классы Page Object для различных страниц.
  - `base_page.py`
  - `faq_page.py`
  - `order_page.py`
- **tests**: Содержит тестовые классы.
  - `test_faq.py`
  - `test_order.py`
  - `test_logo.py`
- `conftest.py`: Содержит определения фикстур.
- `README.md`: Этот файл, содержит обзор проекта и инструкции.
- `requirements.txt`: Содержит список зависимостей.
- `pytest.ini`: Файл конфигурации для Pytest.

## Запуск проекта

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/marinatambova/Sprint_6.git
   cd Sprint_6
   ```
   
2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запуск тестов выполняется по команде `pytest tests/` или `pytest --alluredir=allure_results`
4. Просмотр отчетов в формате веб-страницы выполняется командой `allure serve allure_results`