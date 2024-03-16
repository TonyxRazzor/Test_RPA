# main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage
from config.settings import EXCEL_FILE_PATH, FORM_URL
from utils.utils import read_excel_data

import time


def main():
    # Чтение данных из Excel
    data = read_excel_data(EXCEL_FILE_PATH) # Используем функцию read_excel_data для чтения данных

    # Установка WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Открытие веб-страницы
    driver.get(FORM_URL)

    # Создание экземпляра страницы формы
    form_page = FormPage(driver)

    # Заполнение формы данными из Excel
    for record in data:
        form_page.fill_form(record) # Передаем словарь data в метод fill_form

    # Закрытие браузера
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()
