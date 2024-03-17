# settings.py

import os

# Определяем путь к файлу Excel относительно директории проекта
EXCEL_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenge.xlsx')

# Целевая страница с формой
FORM_URL = 'https://rpachallenge.com/'
