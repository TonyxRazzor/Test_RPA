# utils.py

import pandas as pd
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_excel_data(file_path):
    # Чтение файла exel
    df = pd.read_excel(file_path, header=0, keep_default_na=False)
    # Преобразование всех строк данных в список словарей
    data = df.to_dict('records')
    return data

def clean_keys(data):
    # Удаляет пробелы в начале и конце каждого ключа в словаре
    return {k.strip(): v for k, v in data.items()}

def download_excel(driver, download_directory):
    # Находим ссылку для скачивания Excel файла
    download_link = driver.find_element(By.XPATH, '//a[contains(text(), "Download Excel")]')
    
    # Изменяем атрибут href ссылки, добавляя атрибут download с указанным путем
    download_link.click()

    # Ожидаемое имя файла
    expected_file_name = "challenge.xlsx"

    # Максимальное количество попыток поиска файла
    max_attempts = 3
    # Задержка между попытками в секундах
    delay_between_attempts = 5

    # Проверяем наличие файла с ожидаемым именем
    for attempt in range(max_attempts):
        for file_name in os.listdir(download_directory):
            if file_name == expected_file_name:
                print(f"Файл {expected_file_name} найден.")
                return os.path.join(download_directory, expected_file_name)
        else:
            # Если файл не найден, ждем перед следующей попыткой
            print(f"Файл {expected_file_name} не найден. Попытка {attempt + 1} из {max_attempts}.")
            time.sleep(delay_between_attempts)
            continue
        break
    else:
        print(f"Файл {expected_file_name} не найден после {max_attempts} попыток.")
        return None
    
def click_start_button(driver):
    # Нажатие на кнопку "start"
    try:
        start_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Start")]'))
        )
        start_button.click()
        print("Кнопка 'Start' нажата.")
    except Exception as e:
        print("Ошибка при нажатии кнопки 'Start':", e)