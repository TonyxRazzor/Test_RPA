import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.form_page import FormPage
from config.settings import EXCEL_FILE_PATH, FORM_URL
from utils.utils import clean_keys, click_start_button, download_excel, read_excel_data

def main():
    # Относительный путь к директории для сохранения файлов
    relative_download_directory = "data"
    
    # Формируем абсолютный путь к директории для сохранения файлов
    download_directory = os.path.join(os.path.dirname(__file__), relative_download_directory)

    # Установка настроек для управления загрузками
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
      "download.default_directory": download_directory,
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "safebrowsing_for_trusted_sources_enabled": False,
      "safebrowsing.enabled": False
    })

    # Установка WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Открытие веб-страницы
    driver.get(FORM_URL)

    # Загрузка Excel файла
    excel_file_path = download_excel(driver, download_directory)
    if not excel_file_path:
        print("Не удалось загрузить Excel файл. Программа завершает работу.")
        driver.quit()
        return

    # Нажатие на кнопку "Start"
    click_start_button(driver)

    # Чтение данных из Excel
    data = read_excel_data(EXCEL_FILE_PATH) # Используем функцию read_excel_data для чтения данных

    # Удаление пробелов из ключей
    data_cleaned = [clean_keys(record) for record in data]

    # Создание экземпляра страницы формы
    form_page = FormPage(driver)

    # Заполнение формы данными из Excel
    for record in data_cleaned:
        form_page.fill_form(record) # Передаем словарь data в метод fill_form

    # Закрытие браузера
    time.sleep(5)
    print("Данные занесены в форму.")
    driver.quit()

if __name__ == "__main__":
    main()
