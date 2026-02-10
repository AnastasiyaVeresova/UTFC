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
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'с', 'c', name)
    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'н\/п', 'нп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)
    # Удаляем слова "стул" и "кресло"
    name = re.sub(r'\bстул\b|\bкресло\b', '', name)
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

# Преобразование строки в число
def convert_to_float(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# 1. Чтение Excel
excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

# Определение отображения колонок
columns_mapping = {
    'Unnamed: 1': ('chair_height', 'min', 'max'),
    'Unnamed: 3': ('headrest_height', 'min', 'max'),
    'Unnamed: 5': ('seat_to_floor_height', 'min', 'max'),
    'Unnamed: 11': ('armrest_height_from_seat', 'min', 'max'),
    'Unnamed: 16': ('chair_depth', 'min', None),
    'Unnamed: 18': ('seat_depth', 'min', 'max'),
    'Unnamed: 21': ('backrest_height', None, 'max'),
    'Unnamed: 22': ('backrest_to_seat_height', 'min', 'max'),
    'Unnamed: 26': ('seat_width_with_armrests', 'min', 'max'),
    'Unnamed: 28': ('seat_width', None, 'max'),
    'Unnamed: 31': ('diameter_cross', None, 'max'),
    'Unnamed: 32': ('runners_width', None, 'max'),
    'Unnamed: 33': ('runners_depth', None, 'max'),
    'Unnamed: 34': ('netto', None, None),
    'Unnamed: 35': ('brutto', None, None),
    'Unnamed: 36': ('package_length', None, None),
    'Unnamed: 37': ('package_width', None, None),
    'Unnamed: 38': ('package_height', None, None),
    'Unnamed: 39': ('volume', None, None)
}

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 0].dropna().tolist()

for i, model in enumerate(models_excel):
    model_data = {
        "model": model,
        "normalized": normalize_model_name(model),
        "dimensions_details": {},
        "additional_info": {}
    }

    for col, (key, min_key, max_key) in columns_mapping.items():
        if min_key is not None and max_key is not None:
            model_data["dimensions_details"][key] = {
                "min": normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]),
                "max": normalize_value(df.iloc[i + 3, df.columns.get_loc(col) + 1])
            }
        elif min_key is not None:
            model_data["dimensions_details"][key] = {
                "min": normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]),
                "max": None
            }
        elif max_key is not None:
            model_data["dimensions_details"][key] = {
                "max": normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])
            }
        else:
            model_data["dimensions_details"][key] = normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])

    model_data["additional_info"]["package_dimensions"] = {
        "length": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 36')]),
        "width": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 37')]),
        "height": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 38')])
    }
    model_data["additional_info"]["volume"] = normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 39')])

    excel_data[model] = model_data

# 2. Рекурсивный поиск всех JSON-файлов в папке и подпапках
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# 3. Сбор нормализованных имен моделей из JSON
models_json = {}
for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    model_name = data.get('namefile', [''])[0]
    if not model_name:
        model_name = data.get('name', [''])[0]
    if model_name:
        normalized = normalize_model_name(model_name)
        models_json[normalized] = {"file": json_file, "data": data, "original": model_name}

# 4. Функция для вывода сообщений
def log_message(message, out_file):
    print(message)
    out_file.write(message + '\n')

# 5. Сравнение и вывод результатов
with open('discrepancies.txt', 'w', encoding='utf-8') as out:
    # Проверка моделей из Excel, которых нет в JSON
    for model in models_excel:
        normalized = normalize_model_name(model)
        if normalized not in models_json:
            log_message(f"Модель '{model}' из Excel отсутствует в папке products и её подпапках!", out)

    # Сравнение данных для моделей, которые есть в обоих источниках
    for normalized, json_info in models_json.items():
        # Ищем соответствующую модель в Excel
        excel_model = None
        for model in excel_data:
            if normalize_model_name(model) == normalized:
                excel_model = model
                break
        if not excel_model:
            log_message(f"Модель '{json_info['original']}' из JSON отсутствует в Excel!", out)
            continue

        data = json_info['data']
        discrepancies_found = False

        # Сравнение dimensions_details
        json_dims = data.get('dimensions_details', [{}])[0]
        excel_dims = excel_data[excel_model]['dimensions_details']
        for key in set(json_dims) | set(excel_dims):
            json_val = json_dims.get(key, {})
            excel_val = excel_dims.get(key, {})
            if isinstance(json_val, dict) and isinstance(excel_val, dict):
                for subkey in set(json_val) | set(excel_val):
                    json_subval = normalize_value(json_val.get(subkey))
                    excel_subval = normalize_value(excel_val.get(subkey))
                    if json_subval != excel_subval:
                        log_message(
                            f"Модель '{excel_model}': несовпадение по {key}.{subkey} "
                            f"(JSON: {json_subval}, Excel: {excel_subval})",
                            out
                        )
                        discrepancies_found = True
            elif normalize_value(json_val) != normalize_value(excel_val):
                log_message(
                    f"Модель '{excel_model}': несовпадение по {key} "
                    f"(JSON: {json_val}, Excel: {excel_val})",
                    out
                )
                discrepancies_found = True

        # Сравнение additional_info (упаковка, объем)
        json_package = data.get('transportation', [{}])[0].get('packaging', {}).get('size', {})
        excel_package = excel_data[excel_model]['additional_info']['package_dimensions']

        for key in set(json_package) | set(excel_package):
            json_value = normalize_value(json_package.get(key, None))
            excel_value = normalize_value(excel_package.get(key, None))
            if json_value != excel_value:
                log_message(
                    f"Модель '{excel_model}': несовпадение по package_{key} "
                    f"(JSON: {json_value}, Excel: {excel_value})",
                    out
                )
                discrepancies_found = True

        # Сравнение dimensions (вес, объем)
        json_dims_block = data.get('dimensions', [{}])[0]
        excel_dims_block = {
            'brutto': convert_to_float(normalize_value(excel_data[excel_model]['dimensions_details'].get('brutto', None))),
            'netto': convert_to_float(normalize_value(excel_data[excel_model]['dimensions_details'].get('netto', None))),
            'volume': convert_to_float(normalize_value(excel_data[excel_model]['additional_info'].get('volume', None)))
        }

        # Извлечение значений из JSON
        json_brutto = convert_to_float(normalize_value(json_dims_block.get('brutto', None)))
        json_netto = convert_to_float(normalize_value(json_dims_block.get('netto', None)))
        json_volume = convert_to_float(normalize_value(json_dims_block.get('volume', None)))

        # Сравнение значений
        if json_brutto != excel_dims_block['brutto']:
            log_message(
                f"Модель '{excel_model}': несовпадение по brutto "
                f"(JSON: {json_dims_block.get('brutto')}, Excel: {excel_dims_block['brutto']})",
                out
            )
            discrepancies_found = True

        if json_netto != excel_dims_block['netto']:
            log_message(
                f"Модель '{excel_model}': несовпадение по netto "
                f"(JSON: {json_dims_block.get('netto')}, Excel: {excel_dims_block['netto']})",
                out
            )
            discrepancies_found = True

        if json_volume != excel_dims_block['volume']:
            log_message(
                f"Модель '{excel_model}': несовпадение по volume "
                f"(JSON: {json_dims_block.get('volume')}, Excel: {excel_dims_block['volume']})",
                out
            )
            discrepancies_found = True

        if not discrepancies_found:
            log_message(f"Модель '{excel_model}': все данные совпадают.", out)

print("Сравнение завершено. Результаты в discrepancies.txt и в консоли.")
