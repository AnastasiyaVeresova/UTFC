import pandas as pd
import json
import os
import re
import math
from collections import defaultdict

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

# Преобразование строки в число
def convert_to_float(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# Форматирование значения для вывода
def format_value(value):
    if value is None:
        return '-'
    if isinstance(value, str) and value.strip() in ('', '-', '--'):
        return '-'
    if isinstance(value, dict) and not value:
        return '-'
    if isinstance(value, (list, dict)):
        return str(value)
    return str(value)

# Безопасное сравнение значений
def safe_compare_values(json_val, excel_val):
    def is_empty(value):
        if value is None:
            return True
        if isinstance(value, str) and not value.strip():
            return True
        return False

    if is_empty(json_val) and is_empty(excel_val):
        return True
    if is_empty(json_val) or is_empty(excel_val):
        return False

    try:
        json_str = str(json_val).replace(',', '.').strip()
        excel_str = str(excel_val).replace(',', '.').strip()
    except:
        return False

    try:
        json_float = float(json_str) if json_str else None
    except (ValueError, TypeError):
        json_float = None

    try:
        excel_float = float(excel_str) if excel_str else None
    except (ValueError, TypeError):
        excel_float = None

    if json_float is not None and excel_float is not None:
        return abs(json_float - excel_float) < 0.01

    return str(json_val) == str(excel_val)


# Сравнение min/max значений
def compare_min_max(json_min, json_max, excel_min, excel_max):
    # Нормализуем значения
    json_min = normalize_value(json_min)
    json_max = normalize_value(json_max)
    excel_min = normalize_value(excel_min)
    excel_max = normalize_value(excel_max)

    # Если оба значения min и max пустые или равны "-", считаем их одинаковыми
    if (json_min is None or json_min == "-") and (json_max is None or json_max == "-"):
        return (excel_min is None or excel_min == "-") and (excel_max is None or excel_max == "-")
    if (excel_min is None or excel_min == "-") and (excel_max is None or excel_max == "-"):
        return (json_min is None or json_min == "-") and (json_max is None or json_max == "-")

    # Собираем множества значений, игнорируя пустые или "-"
    json_values = {v for v in [json_min, json_max] if v is not None and v != "-"}
    excel_values = {v for v in [excel_min, excel_max] if v is not None and v != "-"}

    # Если оба множества пустые, значения совпадают
    if not json_values and not excel_values:
        return True

    # Если одно из множеств пустое, значения не совпадают
    if not json_values or not excel_values:
        return False

    # Сравниваем множества значений
    return json_values == excel_values

# Определение, нужно ли исправлять значение
def need_to_fix(json_val, excel_val, is_min_max=False):
    if is_min_max:
        return False
    if safe_compare_values(json_val, excel_val):
        return False
    return True

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
    'Unnamed: 36': ('package_width', None, None),
    'Unnamed: 37': ('package_depth', None, None),
    'Unnamed: 38': ('package_height', None, None),
    'Unnamed: 39': ('volume', None, None)
}

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 0].dropna().tolist()

for i, model in enumerate(models_excel):
    model_data = {
        "model": model,
        "normalized": normalize_model_name(model),  # Исправлено
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
        "width": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 36')]),
        "depth": normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 37')]),
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
        normalized = normalize_model_name(model_name)  # Исправлено
        models_json[normalized] = {"file": json_file, "data": data, "original": model_name}

# 4. Сравнение и вывод результатов
with open('discrepancies.txt', 'w', encoding='utf-8') as out:
    # 4.1. Модели, отсутствующие в JSON (но есть в Excel)
    missing_in_json = []
    for model in models_excel:
        normalized = normalize_model_name(model)  # Исправлено
        if normalized not in models_json:
            missing_in_json.append({"Модель": model, "Источник": "Excel"})
    if missing_in_json:
        df_missing_in_json = pd.DataFrame(missing_in_json)
        out.write("=== Модели, отсутствующие в JSON (но есть в Excel) ===\n")
        out.write(df_missing_in_json.to_string(index=False) + "\n\n")
    else:
        out.write("=== Модели, отсутствующие в JSON (но есть в Excel) ===\nНет отсутствующих моделей.\n\n")

    # 4.2. Модели, отсутствующие в Excel (но есть в JSON)
    missing_in_excel = []
    for normalized, json_info in models_json.items():
        found = False
        for model in models_excel:
            if normalize_model_name(model) == normalized:  # Исправлено
                found = True
                break
        if not found:
            missing_in_excel.append({"Модель": json_info["original"], "Источник": "JSON"})
    if missing_in_excel:
        df_missing_in_excel = pd.DataFrame(missing_in_excel)
        out.write("=== Модели, отсутствующие в Excel (но есть в JSON) ===\n")
        out.write(df_missing_in_excel.to_string(index=False) + "\n\n")
    else:
        out.write("=== Модели, отсутствующие в Excel (но есть в JSON) ===\nНет отсутствующих моделей.\n\n")

    # 4.3. Сравнение данных для совпадающих моделей
    discrepancies = []
    for normalized, json_info in models_json.items():
        excel_model = None
        for model in excel_data:
            if normalize_model_name(model) == normalized:  # Исправлено
                excel_model = model
                break
        if not excel_model:
            continue

        data = json_info['data']
        json_dims = data.get('dimensions_details', [{}])[0]
        excel_dims = excel_data[excel_model]['dimensions_details']

        # Сравнение dimensions_details
        for key in set(json_dims) | set(excel_dims):
            json_val = json_dims.get(key, {})
            excel_val = excel_dims.get(key, {})
            if isinstance(json_val, dict) and isinstance(excel_val, dict):
                json_min = json_val.get('min')
                json_max = json_val.get('max')
                excel_min = excel_val.get('min')
                excel_max = excel_val.get('max')
                is_min_max_equal = compare_min_max(json_min, json_max, excel_min, excel_max)
                if not is_min_max_equal:
                    discrepancies.append({
                        "Модель": excel_model,
                        "Параметр": key,
                        "JSON": f"min={format_value(json_min)}, max={format_value(json_max)}",
                        "Excel": f"min={format_value(excel_min)}, max={format_value(excel_max)}",
                        "Нужно исправить?": "Да"
                    })
            else:
                if normalize_value(json_val) != normalize_value(excel_val):
                    discrepancies.append({
                        "Модель": excel_model,
                        "Параметр": key,
                        "JSON": format_value(json_val),
                        "Excel": format_value(excel_val),
                        "Нужно исправить?": "Да"
                    })


        # Сравнение упаковки
        json_package = data.get('transportation', [{}])[0].get('packaging', {}).get('size', {})
        excel_package = excel_data[excel_model]['additional_info']['package_dimensions']
        for key in ['width', 'depth', 'height']:
            json_value = json_package.get(key, None)
            excel_value = excel_package.get(key, None)
            discrepancies.append({
                "Модель": excel_model,
                "Параметр": f"package_{key}",
                "JSON": format_value(json_value),
                "Excel": format_value(excel_value),
                "Нужно исправить?": "Да" if not safe_compare_values(json_value, excel_value) else "Нет"
            })

        # Сравнение веса и объёма
        json_brutto = data.get('dimensions', [{}])[0].get('brutto', None)
        excel_brutto = excel_data[excel_model]['dimensions_details'].get('brutto', None)
        discrepancies.append({
            "Модель": excel_model,
            "Параметр": "brutto",
            "JSON": format_value(json_brutto),
            "Excel": format_value(excel_brutto),
            "Нужно исправить?": "Да" if not safe_compare_values(json_brutto, excel_brutto) else "Нет"
        })

        json_netto = data.get('dimensions', [{}])[0].get('netto', None)
        excel_netto = excel_data[excel_model]['dimensions_details'].get('netto', None)
        discrepancies.append({
            "Модель": excel_model,
            "Параметр": "netto",
            "JSON": format_value(json_netto),
            "Excel": format_value(excel_netto),
            "Нужно исправить?": "Да" if not safe_compare_values(json_netto, excel_netto) else "Нет"
        })

        json_volume = data.get('dimensions', [{}])[0].get('volume', None)
        excel_volume = excel_data[excel_model]['additional_info'].get('volume', None)
        discrepancies.append({
            "Модель": excel_model,
            "Параметр": "volume",
            "JSON": format_value(json_volume),
            "Excel": format_value(excel_volume),
            "Нужно исправить?": "Да" if not safe_compare_values(json_volume, excel_volume) else "Нет"
        })

    # 4.4. Вывод несовпадений
    # if discrepancies:
    #     df_discrepancies = pd.DataFrame(discrepancies)
    #     out.write("=== Несовпадения параметров ===\n")
    #     out.write(df_discrepancies.to_string(index=False) + "\n\n")
    # else:
    #     out.write("=== Несовпадения параметров ===\nНет несовпадений.\n\n")
    # 4.4. Вывод несовпадений
    if discrepancies:
        df_discrepancies = pd.DataFrame(discrepancies)
        # Фильтруем только те строки, где "Нужно исправить?" == "Да"
        df_discrepancies_filtered = df_discrepancies[df_discrepancies["Нужно исправить?"] == "Да"]
        if not df_discrepancies_filtered.empty:
            out.write("=== Несовпадения параметров (требуют исправления) ===\n")
            out.write(df_discrepancies_filtered.to_string(index=False) + "\n\n")
        else:
            out.write("=== Несовпадения параметров (требуют исправления) ===\nНет несовпадений, требующих исправления.\n\n")
    else:
        out.write("=== Несовпадения параметров ===\nНет несовпадений.\n\n")


print("Сравнение завершено. Результаты в discrepancies.txt")
