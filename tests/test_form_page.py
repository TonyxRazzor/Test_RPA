import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage
from config.settings import FORM_URL

@pytest.fixture(scope="function")
def setup_and_teardown():
    # Установка WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(FORM_URL) # Замените на URL вашей формы
    form_page = FormPage(driver)
    yield form_page
    # Закрытие браузера после теста
    driver.quit()

@pytest.mark.parametrize("test_name", ["Заполнение формы"])
def test_fill_form(setup_and_teardown, test_name):
    # Подготовка данных для теста
    test_data = {
        'First Name': 'John',
        'Last Name': 'Doe',
        'Email': 'john.doe@example.com',
        'Address': '98 North Road',
        'Company Name': 'IT Solutions',
        'Role in Company': 'Programmer',
        'Phone Number': '40716543298',
    }

    # Заполнение формы тестовыми данными
    setup_and_teardown.fill_form(test_data)

@pytest.mark.parametrize("test_name", ["Проверка совместимости сайта"])
@pytest.mark.parametrize("url, expected_result", [
    (FORM_URL, True),
    ("https://www.google.com/", False),
], ids=["test_website_compatibility_form", "test_website_compatibility_google"])
def test_website_compatibility(setup_and_teardown, url, expected_result, test_name):
    setup_and_teardown.driver.get(url)
    page_title = setup_and_teardown.driver.title
    assert page_title != "", "Page title is empty, page might not have loaded correctly"

@pytest.mark.parametrize("test_name", ["Проверка наличия полей"])
def test_multiple_fields_presence(setup_and_teardown, test_name):
    # Словарь с данными для каждого поля
    test_data2 = {
        'labelEmail': 'test.email@example.com',
        'labelAddress': '123 Test Street',
        'labelFirstName': 'John',
        'labelLastName': 'Doe',
        'labelCompanyName': 'Test Company',
        'labelRole': 'Developer',
        'labelPhone': '1234567890',
    }

    # Проверка наличия каждого поля на странице
    for field_name in test_data2.keys():
        wait = WebDriverWait(setup_and_teardown.driver, 10) # Ожидание до 10 секунд
        try:
            field = wait.until(EC.presence_of_element_located((By.XPATH, f'//input[@ng-reflect-name="{field_name}"]')))
            print(f"{field_name} field is present on the page.")
        except TimeoutException:
            assert False, f"{field_name} field is not present on the page."
