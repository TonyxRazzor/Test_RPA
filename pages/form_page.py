from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, data):
        # Ожидание появления элемента 'email' и заполнение его
        wait = WebDriverWait(self.driver, 10) # Ожидание до 10 секунд
        email_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelEmail"]')))
        email_element.send_keys(data['Email'])

        # Ожидание появления элемента 'address' и заполнение его
        address_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelAddress"]')))
        address_element.send_keys(data['Address'])

        # Ожидание появления элемента 'first_name' и заполнение его
        first_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelFirstName"]')))
        first_name_element.send_keys(data['First Name'])

        # Ожидание появления элемента 'company_name' и заполнение его
        company_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]')))
        company_name_element.send_keys(data['Company Name'])

        # Ожидание появления элемента 'role_in_company' и заполнение его
        role_in_company_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelRole"]')))
        role_in_company_element.send_keys(data['Role in Company'])

        # Ожидание появления элемента 'phone_number' и заполнение его
        phone_number_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelPhone"]')))
        phone_number_element.send_keys(data['Phone Number'])

        # Ожидание появления элемента 'last_name' и заполнение его
        last_name_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@ng-reflect-name="labelLastName"]')))
        last_name_element.send_keys(data['Last Name ']) # пробел в эксель таблице (надо поставить проверку на пробелы)

        # добавить задержку для визуальной проверки
        time.sleep(3)

        # Нажатие на кнопку отправки
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]')))
        submit_button.click()
