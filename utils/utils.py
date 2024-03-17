# utils.py

import pandas as pd

def read_excel_data(file_path):
    df = pd.read_excel(file_path, header=0, keep_default_na=False)
    # Преобразование всех строк данных в список словарей
    data = df.to_dict('records')
    return data

def clean_keys(data):
    """Удаляет пробелы в начале и конце каждого ключа в словаре."""
    return {k.strip(): v for k, v in data.items()}