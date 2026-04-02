import pandas as pd
import json
import os
import re
import math

# Функция нормализации имени модели
def normalize_model_name(name):
    if not isinstance(name, str):
        return ""
    name = name.lower().strip()
    name = re.sub(r'\bстул\b|\bкресло\b|Кресло UTFC\b', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'с', 'c', name)
    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'н\/п', 'нп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Преобразование пустых значений
def normalize_value(value):
    if isinstance(value, str) and value.strip() in ('', '-', '--'):
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    if value is None:
        return None
    return value

# Чтение Excel
excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 0].dropna().tolist()

for i, model in enumerate(models_excel):
    model_data = {
        "model": model,
        "normalized": normalize_model_name(model),
        "skeleton": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 36')]),
        "minpromtorg": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 37')]),
        "typeofproduct": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 38')])
    }
    excel_data[model] = model_data

# Рекурсивный поиск всех JSON-файлов в папке и подпапках
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# Обновление JSON-файлов
failed_updates = []

for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        model_name = data.get('namefile', [''])[0]
        if not model_name:
            model_name = data.get('name', [''])[0]

        normalized = normalize_model_name(model_name)
        excel_model = None

        for model in excel_data:
            if normalize_model_name(model) == normalized:
                excel_model = model
                break

        if excel_model:
            # Обновляем данные
            data['skeleton'] = excel_data[excel_model]['skeleton']
            data['minpromtorg'] = excel_data[excel_model]['minpromtorg']
            data['typeofproduct'] = excel_data[excel_model]['typeofproduct']

            # Сохраняем обновленный JSON
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            failed_updates.append((json_file, "Модель не найдена в Excel"))

    except Exception as e:
        failed_updates.append((json_file, str(e)))

# Вывод списка файлов, которые не удалось обновить
with open('failed_updates.txt', 'w', encoding='utf-8') as f:
    for file, reason in failed_updates:
        f.write(f"{file}: {reason}\n")

print("Обновление завершено. Список неудачных обновлений в failed_updates.txt")
