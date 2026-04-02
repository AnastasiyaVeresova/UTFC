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
    name = re.sub(r'сн\s*-?\s*710\s+айкью', 'айкью', name, flags=re.IGNORECASE)
    name = re.sub(r'сн\s*-?\s*800\s+энжел', 'энжел', name, flags=re.IGNORECASE)
    name = re.sub(r'н\/п|н_п', 'нп', name)
    name = re.sub(r'[/\\]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[^\w\s+-]', '', name)
    name = re.sub(r'пластик\/хром|пластик хром', 'пластикхром', name)
    name = re.sub(r'хром\/хдп\/мб|хром хдп мб', 'хромхдпмб', name)
    name = re.sub(r'дерево\/мб|дерево мб', 'деревомб', name)
    name = re.sub(r'с', 'c', name)
    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)
    name = re.sub(r'сн-(\d+)', 'сн\\1', name)
    name = re.sub(r'^\s*сн710\s+', '', name)
    name = re.sub(r'tg\s+столик', 'tgстолик', name)
    name = re.sub(r'пиастра\s+столик', 'пиастрастолик', name)
    name = re.sub(r'пластик\s+хром', 'пластикхром', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Преобразование пустых значений
def normalize_value(value):
    if isinstance(value, str) and value.strip() in ('', '-', '--'):
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    if value is None:
        return ""
    return str(value)

# Замена точки на запятую в числовых значениях
def format_number(value):
    if isinstance(value, (int, float)):
        return str(value).replace('.', ',')
    if isinstance(value, str):
        return value.replace('.', ',')
    return value

# Чтение Excel
excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 1].dropna().tolist()

columns_mapping = {
    'Unnamed: 2': ('chair_height', 'min', 'max'),
    'Unnamed: 4': ('headrest_height', 'min', 'max'),
    'Unnamed: 6': ('seat_to_floor_height', 'min', 'max'),
    'Unnamed: 10': ('armrest_height_from_seat', 'min', 'max'),
    'Unnamed: 15': ('chair_depth', 'min', None),
    'Unnamed: 17': ('seat_depth', 'min', 'max'),
    'Unnamed: 20': ('backrest_height', None, 'max'),
    'Unnamed: 21': ('backrest_to_seat_height', 'min', 'max'),
    'Unnamed: 25': ('seat_width_with_armrests', 'min', 'max'),
    'Unnamed: 27': ('seat_width', None, 'max'),
    'Unnamed: 30': ('diameter_cross', None, 'max'),
    'Unnamed: 31': ('runners_width', None, 'max'),
    'Unnamed: 32': ('runners_depth', None, 'max'),
    'Unnamed: 33': ('recommended_load', None, None),
    'Unnamed: 34': ('max_load', None, None),
    'Unnamed: 35': ('skeleton', None, None),
    'Unnamed: 36': ('minpromtorg', None, None),
    'Unnamed: 37': ('typeofproduct', None, None),
    'Unnamed: 38': ('netto', None, None),
    'Unnamed: 39': ('brutto', None, None),
    'Unnamed: 40': ('package_width', None, None),
    'Unnamed: 41': ('package_depth', None, None),
    'Unnamed: 42': ('package_height', None, None),
    'Unnamed: 43': ('volume', None, None)
}

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
                "min": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
                "max": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col) + 1]))
            }
        elif min_key is not None:
            model_data["dimensions_details"][key] = {
                "min": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
                "max": None
            }
        elif max_key is not None:
            model_data["dimensions_details"][key] = {
                "max": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))
            }
        else:
            model_data["dimensions_details"][key] = format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))

    model_data["additional_info"] = {
        "package_dimensions": {
            "width": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 40')])),
            "depth": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 41')])),
            "height": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 42')]))
        },
        "volume": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 43')]))
    }

    excel_data[model] = model_data

# Рекурсивный поиск всех JSON-файлов в папке и подпапках
products_dir = r'C:\Users\UTFC\Documents\БалтМебель\to\products'

json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# Список для моделей, отсутствующих в JSON
missing_in_json = set(excel_data.keys())

# Список всех возможных параметров размеров
all_dimension_params = [
    "chair_height", "headrest_height", "seat_to_floor_height", "armrest_height_from_seat",
    "chair_depth", "seat_depth", "backrest_height", "backrest_to_seat_height",
    "seat_width_with_armrests", "seat_width", "diameter_cross", "runners_width",
    "runners_depth", "seat_to_floor_height_upper", "armrest_height_from_floor",
    "armrest_width_support", "armrest_length_support", "seat_depth_km",
    "backrest_height_external", "backrest_width_narrow", "backrest_width_wide",
    "recommended_load", "max_load", "skeleton", "minpromtorg", "typeofproduct",
    "netto", "brutto", "package_width", "package_depth", "package_height", "volume"
]

# Обновление JSON-файлов
failed_updates = []

for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            original_data = json.load(f)

        model_name = original_data.get('namefile', [''])[0]
        if not model_name:
            model_name = original_data.get('name', [''])[0]

        normalized = normalize_model_name(model_name)
        excel_model = None

        for model in excel_data:
            if normalize_model_name(model) == normalized:
                excel_model = model
                missing_in_json.discard(model)
                break

        # Если в JSON нет `dimensions_details`, создаём его
        if 'dimensions_details' not in original_data or not original_data['dimensions_details']:
            original_data['dimensions_details'] = [{}]

        # Проходим по всем возможным параметрам размеров
        for param in all_dimension_params:
            if param not in original_data['dimensions_details'][0]:
                original_data['dimensions_details'][0][param] = {"min": "", "max": ""}

        # Обновляем значения из Excel, если они есть
        if excel_model:
            excel_model_data = excel_data[excel_model]
            for key, value in excel_model_data['dimensions_details'].items():
                if key in original_data['dimensions_details'][0]:
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            if sub_value is not None and sub_value != "":
                                original_data['dimensions_details'][0][key][sub_key] = sub_value
                    else:
                        if value is not None and value != "":
                            original_data['dimensions_details'][0][key] = value

            # Обновляем additional_info
            if 'additional_info' in original_data:
                if 'package_dimensions' in original_data['additional_info']:
                    for key, value in excel_model_data['additional_info']['package_dimensions'].items():
                        if value is not None and value != "":
                            original_data['additional_info']['package_dimensions'][key] = value
                if 'volume' in original_data['additional_info']:
                    if excel_model_data['additional_info']['volume'] is not None:
                        original_data['additional_info']['volume'] = excel_model_data['additional_info']['volume']

            # Обновляем прочие поля
            if 'skeleton' in original_data and excel_model_data['dimensions_details'].get('skeleton') is not None:
                original_data['skeleton'] = excel_model_data['dimensions_details'].get('skeleton')
            if 'minpromtorg' in original_data and excel_model_data['dimensions_details'].get('minpromtorg') is not None:
                original_data['minpromtorg'] = excel_model_data['dimensions_details'].get('minpromtorg')
            if 'typeofproduct' in original_data and excel_model_data['dimensions_details'].get('typeofproduct') is not None:
                original_data['typeofproduct'] = excel_model_data['dimensions_details'].get('typeofproduct')

            # Обновляем max_load и recommended_load в guarantee
            if 'guarantee' in original_data and len(original_data['guarantee']) > 0:
                if 'max_load' in original_data['guarantee'][0] and excel_model_data['dimensions_details'].get('max_load') is not None:
                    original_data['guarantee'][0]['max_load'] = format_number(excel_model_data['dimensions_details'].get('max_load'))
                if 'recommended_load' in original_data['guarantee'][0] and excel_model_data['dimensions_details'].get('recommended_load') is not None:
                    original_data['guarantee'][0]['recommended_load'] = format_number(excel_model_data['dimensions_details'].get('recommended_load'))

            # Обновляем brutto и netto в dimensions
            if 'dimensions' in original_data and len(original_data['dimensions']) > 0:
                if 'brutto' in original_data['dimensions'][0] and excel_model_data['dimensions_details'].get('brutto') is not None:
                    original_data['dimensions'][0]['brutto'] = format_number(excel_model_data['dimensions_details'].get('brutto'))
                if 'netto' in original_data['dimensions'][0] and excel_model_data['dimensions_details'].get('netto') is not None:
                    original_data['dimensions'][0]['netto'] = format_number(excel_model_data['dimensions_details'].get('netto'))

            # Обновляем volume в dimensions
            if 'dimensions' in original_data and len(original_data['dimensions']) > 0 and excel_model_data['additional_info'].get('volume') is not None:
                original_data['dimensions'][0]['volume'] = format_number(excel_model_data['additional_info'].get('volume'))

        # Сохраняем обновленный JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(original_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        failed_updates.append((json_file, str(e)))

# Вывод списка файлов, которые не удалось обновить
with open('failed_updates.txt', 'w', encoding='utf-8') as f:
    for file, reason in failed_updates:
        f.write(f"{file}: {reason}\n")

# Записываем модели, отсутствующие в JSON
with open('missing_in_json.txt', 'w', encoding='utf-8') as f:
    for model in missing_in_json:
        f.write(f"{model}\n")

print("Обновление завершено. Список неудачных обновлений в failed_updates.txt, отсутствующих моделей в missing_in_json.txt")
