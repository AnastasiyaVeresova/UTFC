# import pandas as pd
# import json
# import os
# import re
# import math

# # Функция нормализации имени модели
# def normalize_model_name(name):
#     if not isinstance(name, str):
#         return ""
#     name = name.lower().strip()
#     name = re.sub(r'\bстул\b|\bкресло\b|Кресло UTFC\b', '', name, flags=re.IGNORECASE)
#     name = re.sub(r'\s+', ' ', name)
#     name = re.sub(r'[^\w\s-]', '', name)
#     name = re.sub(r'с', 'c', name)
#     name = re.sub(r'в\/п', 'вп', name)
#     name = re.sub(r'н\/п', 'нп', name)
#     name = re.sub(r'х\/дп', 'хдп', name)
#     name = re.sub(r'м\/б', 'мб', name)
#     name = re.sub(r'тг', 'tg', name)
#     name = re.sub(r'пвм', 'пвм', name)
#     name = re.sub(r'\s+', ' ', name).strip()
#     return name

# # Преобразование пустых значений
# def normalize_value(value):
#     if isinstance(value, str) and value.strip() in ('', '-', '--'):
#         return None
#     if isinstance(value, float) and math.isnan(value):
#         return None
#     if value is None:
#         return None
#     return value

# # Замена точки на запятую в числовых значениях
# def format_number(value):
#     if isinstance(value, (int, float)):
#         return str(value).replace('.', ',')
#     if isinstance(value, str):
#         return value.replace('.', ',')
#     return value

# # Чтение Excel
# excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
# df = pd.read_excel(excel_path, sheet_name='Размеры')

# # Создание словаря с данными из Excel
# excel_data = {}
# models_excel = df.iloc[3:, 0].dropna().tolist()

# columns_mapping = {
#     'Unnamed: 1': ('chair_height', 'min', 'max'),
#     'Unnamed: 3': ('headrest_height', 'min', 'max'),
#     'Unnamed: 5': ('seat_to_floor_height', 'min', 'max'),
#     'Unnamed: 11': ('armrest_height_from_seat', 'min', 'max'),
#     'Unnamed: 16': ('chair_depth', 'min', None),
#     'Unnamed: 18': ('seat_depth', 'min', 'max'),
#     'Unnamed: 21': ('backrest_height', None, 'max'),
#     'Unnamed: 22': ('backrest_to_seat_height', 'min', 'max'),
#     'Unnamed: 26': ('seat_width_with_armrests', 'min', 'max'),
#     'Unnamed: 28': ('seat_width', None, 'max'),
#     'Unnamed: 31': ('diameter_cross', None, 'max'),
#     'Unnamed: 32': ('runners_width', None, 'max'),
#     'Unnamed: 33': ('runners_depth', None, 'max'),
#     'Unnamed: 34': ('recommended_load', None, None),
#     'Unnamed: 35': ('max_load', None, None),
#     'Unnamed: 36': ('skeleton', None, None),
#     'Unnamed: 37': ('minpromtorg', None, None),
#     'Unnamed: 38': ('typeofproduct', None, None),
#     'Unnamed: 39': ('netto', None, None),
#     'Unnamed: 40': ('brutto', None, None),
#     'Unnamed: 41': ('package_width', None, None),
#     'Unnamed: 42': ('package_depth', None, None),
#     'Unnamed: 43': ('package_height', None, None),
#     'Unnamed: 44': ('volume', None, None)
# }

# for i, model in enumerate(models_excel):
#     model_data = {
#         "model": model,
#         "normalized": normalize_model_name(model),
#         "dimensions_details": {},
#         "additional_info": {}
#     }

#     for col, (key, min_key, max_key) in columns_mapping.items():
#         if min_key is not None and max_key is not None:
#             model_data["dimensions_details"][key] = {
#                 "min": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
#                 "max": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col) + 1]))
#             }
#         elif min_key is not None:
#             model_data["dimensions_details"][key] = {
#                 "min": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
#                 "max": None
#             }
#         elif max_key is not None:
#             model_data["dimensions_details"][key] = {
#                 "max": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))
#             }
#         else:
#             model_data["dimensions_details"][key] = format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))

#     model_data["additional_info"] = {
#         "package_dimensions": {
#             "width": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 41')])),
#             "depth": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 42')])),
#             "height": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 43')]))
#         },
#         "volume": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 44')]))
#     }

#     excel_data[model] = model_data

# # Рекурсивный поиск всех JSON-файлов в папке и подпапках
# products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
# json_files = []
# for root, dirs, files in os.walk(products_dir):
#     for file in files:
#         if file.endswith('.json'):
#             json_files.append(os.path.join(root, file))

# # Обновление JSON-файлов
# failed_updates = []
# skipped_updates = []

# for json_file in json_files:
#     try:
#         with open(json_file, 'r', encoding='utf-8') as f:
#             data = json.load(f)

#         model_name = data.get('namefile', [''])[0]
#         if not model_name:
#             model_name = data.get('name', [''])[0]

#         normalized = normalize_model_name(model_name)
#         excel_model = None

#         for model in excel_data:
#             if normalize_model_name(model) == normalized:
#                 excel_model = model
#                 break

#         if excel_model:
#             excel_model_data = excel_data[excel_model]

#             # Обновляем dimensions_details
#             if 'dimensions_details' in data and len(data['dimensions_details']) > 0:
#                 for key, value in excel_model_data['dimensions_details'].items():
#                     if key in data['dimensions_details'][0]:
#                         if isinstance(value, dict):
#                             for sub_key, sub_value in value.items():
#                                 if sub_value is not None:
#                                     data['dimensions_details'][0][key][sub_key] = sub_value
#                         else:
#                             if value is not None:
#                                 data['dimensions_details'][0][key] = value

#             # Обновляем additional_info
#             if 'additional_info' in data:
#                 if 'package_dimensions' in data['additional_info']:
#                     for key, value in excel_model_data['additional_info']['package_dimensions'].items():
#                         if value is not None:
#                             data['additional_info']['package_dimensions'][key] = value
#                 if 'volume' in data['additional_info']:
#                     if excel_model_data['additional_info']['volume'] is not None:
#                         data['additional_info']['volume'] = excel_model_data['additional_info']['volume']

#             # Обновляем прочие поля
#             if 'skeleton' in data and excel_model_data['dimensions_details'].get('skeleton') is not None:
#                 data['skeleton'] = excel_model_data['dimensions_details'].get('skeleton')
#             if 'minpromtorg' in data and excel_model_data['dimensions_details'].get('minpromtorg') is not None:
#                 data['minpromtorg'] = excel_model_data['dimensions_details'].get('minpromtorg')
#             if 'typeofproduct' in data and excel_model_data['dimensions_details'].get('typeofproduct') is not None:
#                 data['typeofproduct'] = excel_model_data['dimensions_details'].get('typeofproduct')

#             # Обновляем max_load и recommended_load в guarantee
#             if 'guarantee' in data and len(data['guarantee']) > 0:
#                 if 'max_load' in data['guarantee'][0] and excel_model_data['dimensions_details'].get('max_load') is not None:
#                     data['guarantee'][0]['max_load'] = format_number(excel_model_data['dimensions_details'].get('max_load'))
#                 if 'recommended_load' in data['guarantee'][0] and excel_model_data['dimensions_details'].get('recommended_load') is not None:
#                     data['guarantee'][0]['recommended_load'] = format_number(excel_model_data['dimensions_details'].get('recommended_load'))

#             # Обновляем brutto и netto в dimensions
#             if 'dimensions' in data and len(data['dimensions']) > 0:
#                 if 'brutto' in data['dimensions'][0] and excel_model_data['dimensions_details'].get('brutto') is not None:
#                     data['dimensions'][0]['brutto'] = format_number(excel_model_data['dimensions_details'].get('brutto'))
#                 if 'netto' in data['dimensions'][0] and excel_model_data['dimensions_details'].get('netto') is not None:
#                     data['dimensions'][0]['netto'] = format_number(excel_model_data['dimensions_details'].get('netto'))

#             # Обновляем volume в dimensions
#             if 'dimensions' in data and len(data['dimensions']) > 0 and excel_model_data['additional_info'].get('volume') is not None:
#                 data['dimensions'][0]['volume'] = format_number(excel_model_data['additional_info'].get('volume'))

#             # Сохраняем обновленный JSON
#             with open(json_file, 'w', encoding='utf-8') as f:
#                 json.dump(data, f, ensure_ascii=False, indent=4)
#         else:
#             failed_updates.append((json_file, "Модель не найдена в Excel"))

#     except Exception as e:
#         failed_updates.append((json_file, str(e)))

# # Вывод списка файлов, которые не удалось обновить
# with open('failed_updates.txt', 'w', encoding='utf-8') as f:
#     for file, reason in failed_updates:
#         f.write(f"{file}: {reason}\n")

# # Вывод списка файлов, где обновление не произошло
# with open('skipped_updates.txt', 'w', encoding='utf-8') as f:
#     for file, reason in skipped_updates:
#         f.write(f"{file}: {reason}\n")

# print("Обновление завершено. Список неудачных обновлений в failed_updates.txt и пропущенных обновлений в skipped_updates.txt")



import pandas as pd
import json
import os
import re
import math
import copy

def compare_and_log_changes(original_data, updated_data, json_file):
    changes_detected = False
    changes_log = []

    def compare_values(original, updated, path):
        nonlocal changes_detected
        if isinstance(updated, dict) and isinstance(original, dict):
            compare_dicts(original, updated, path)
        elif isinstance(updated, list) and isinstance(original, list):
            compare_lists(original, updated, path)
        else:
            if original != updated:
                changes_detected = True
                changes_log.append(f"Изменено: {path}: '{original}' → '{updated}'")

    def compare_dicts(original, updated, path):
        for key in updated:
            current_path = f"{path}.{key}" if path else key
            if key in original:
                compare_values(original[key], updated[key], current_path)
            else:
                changes_detected = True
                changes_log.append(f"Добавлено: {current_path}: '{updated[key]}'")

    def compare_lists(original, updated, path):
        if len(original) != len(updated):
            changes_detected = True
            changes_log.append(f"Изменён размер списка: {path}: {len(original)} → {len(updated)}")
        else:
            for i, (orig_item, upd_item) in enumerate(zip(original, updated)):
                current_path = f"{path}[{i}]"
                compare_values(orig_item, upd_item, current_path)

    compare_values(original_data, updated_data, "")

    if changes_detected:
        with open('changes_log.txt', 'w', encoding='utf-8') as log_file:
            log_file.write(f"\nФайл: {json_file}\n")
            for change in changes_log:
                log_file.write(f"{change}\n")

        print(f"В файле {os.path.basename(json_file)} обнаружены изменения. Подробности в changes_log.txt")

    return changes_detected, changes_log



# Функция нормализации имени модели
def normalize_model_name(name):
    if not isinstance(name, str):
        return ""
    name = name.lower().strip()
    name = re.sub(r'\bстул\b|\bкресло\b|Кресло UTFC\b', '', name, flags=re.IGNORECASE)
    name = re.sub(r'сн\s*-?\s*710\s+айкью', 'айкью', name, flags=re.IGNORECASE)
    name = re.sub(r'сн\s*-?\s*800\s+энжел', 'энжел', name, flags=re.IGNORECASE)
    name = re.sub(r'н\/п|н_п', 'нп', name)  # Обрабатываем оба варианта

    name = re.sub(r'[/\\]', ' ', name)  # Замена слешей 
    name = re.sub(r'\s+', ' ', name) # Удаление лишних пробелов
    name = re.sub(r'[^\w\s+-]', '', name)  # Сохраняем + и -
    name = re.sub(r'пластик\/хром|пластик хром', 'пластикхром', name)
    name = re.sub(r'хром\/хдп\/мб|хром хдп мб', 'хромхдпмб', name)
    name = re.sub(r'дерево\/мб|дерево мб', 'деревомб', name)
    name = re.sub(r'с', 'c', name)
    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)
    name = re.sub(r'сн-(\d+)', 'сн\\1', name)  # Убираем дефис перед цифрами в "сн-<цифры>"
    name = re.sub(r'^\s*сн710\s+', '', name)
    name = re.sub(r'tg\s+столик', 'tgстолик', name)
    name = re.sub(r'пиастра\s+столик', 'пиастрастолик', name)
    name = re.sub(r'пластик\s+хром', 'пластикхром', name)


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

# Замена точки на запятую в числовых значениях
def format_number(value):
    if isinstance(value, (int, float)):
        return str(value).replace('.', ',')
    if isinstance(value, str):
        return value.replace('.', ',')
    return value

def remove_trailing_zero(value):
    if isinstance(value, str):
        try:
            num = float(value.replace(',', '.'))
            if num.is_integer():
                return str(int(num))
            else:
                return value.replace('.', ',')
        except ValueError:
            return value
    return value


# Чтение Excel
excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами_270226.xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 1].dropna().tolist()
print(df.head(10))

columns_mapping = {
    'Unnamed: 2': ('chair_height', 'min', 'max'),  # Высота кресла
    'Unnamed: 4': ('headrest_height', 'min', 'max'),  # Высота подголовника
    'Unnamed: 6': ('seat_to_floor_height_upper', 'min', 'max'),  # Высота сиденья (до верхней части)
    'Unnamed: 8': ('seat_to_floor_height', 'min', 'max'),  # Высота до сиденья (до нижней части)
    'Unnamed: 10': ('armrest_height_from_floor', 'min', 'max'),  # Высота подлокотника (до нижней части)
    'Unnamed: 12': ('armrest_height_from_seat', 'min', 'max'),  # Высота подлокотника (от сиденья)
    'Unnamed: 14': ('armrest_width_support', None, 'max'),  # Ширина подлокотников опорной части
    'Unnamed: 15': ('armrest_length_support', None, 'max'),  # Длина подлокотников опорной части
    'Unnamed: 17': ('chair_depth', 'min', None),  # Глубина кресла
    'Unnamed: 19': ('seat_depth', 'min', 'max'),  # Глубина сиденья
    'Unnamed: 21': ('seat_depth_km', None, 'max'),  # Глубина сиденья (КМ)
    'Unnamed: 22': ('backrest_height', None, 'max'),  # Высота спинки
    'Unnamed: 23': ('backrest_to_seat_height', 'min', 'max'),  # Высота спинки до сиденья
    'Unnamed: 25': ('backrest_height_external', None, 'max'),  # Высота спинки с внешней стороны
    'Unnamed: 27': ('seat_width_with_armrests', 'min', 'max'),  # Ширина сиденья с подлокотниками
    'Unnamed: 29': ('seat_width', None, 'max'),  # Ширина сиденья
    'Unnamed: 30': ('backrest_width_narrow', None, 'max'),  # Ширина спинки (узкая часть)
    'Unnamed: 31': ('backrest_width_wide', None, 'max'),  # Ширина спинки (широкая часть)
    'Unnamed: 32': ('diameter_cross', None, 'max'),  # Диаметр крестовины
    'Unnamed: 33': ('runners_width', None, 'max'),  # Ширина полозьев
    'Unnamed: 34': ('runners_depth', None, 'max'),  # Глубина полозьев
    'Unnamed: 35': ('recommended_load', None, None),  # Рекомендуемая нагрузка
    'Unnamed: 36': ('max_load', None, None),  # Предельно допустимая нагрузка
    'Unnamed: 37': ('skeleton', None, None),  # Каркас
    'Unnamed: 38': ('minpromtorg', None, None),  # Минпромторг
    # 'Unnamed: 39': ('typeofproduct', None, None),  # Тип продукта
    'Unnamed: 39': ('netto', None, None),  # Масса нетто
    'Unnamed: 40': ('brutto', None, None),  # Масса брутто
    'Unnamed: 41': ('package_width', None, None),  # Ширина упаковки
    'Unnamed: 42': ('package_depth', None, None),  # Глубина упаковки
    'Unnamed: 43': ('package_height', None, None),  # Высота упаковки
    'Unnamed: 44': ('volume', None, None),  # Объем
    'Unnamed: 45': ('box_on_pallet', None, None),  # Количество коробок на паллете, шт.
    'Unnamed: 46': ('pallet_width', None, None)  # габариты нагруженного паллета, мм (д.ш.в.)		
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

    model_data["transportation"] = {
        "size": {
            "width": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 41')])),
            "depth": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 42')])),
            "height": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 43')]))
        },
        "volume": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 44')]))
    }

    excel_data[model] = model_data


# Рекурсивный поиск всех JSON-файлов в папке и подпапках
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# Список для моделей, отсутствующих в JSON
missing_in_json = set(excel_data.keys())

# Обновление JSON-файлов
failed_updates = []
skipped_updates = []

for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            original_data = json.load(f)

        # Сохраняем копию оригинальных данных
        original_data_copy = copy.deepcopy(original_data)

        model_name = original_data.get('namefile', [''])[0]
        if not model_name:
            model_name = original_data.get('name', [''])[0]

        normalized = normalize_model_name(model_name)
        excel_model = None

        for model in excel_data:
            if normalize_model_name(model) == normalized:
                excel_model = model
                break

        if excel_model:
            excel_model_data = excel_data[excel_model]

            # Обновляем dimensions_details
            if 'dimensions_details' not in original_data:
                original_data['dimensions_details'] = [{}]

            for key, value in excel_model_data['dimensions_details'].items():
                if key not in original_data['dimensions_details'][0]:
                    original_data['dimensions_details'][0][key] = {}

                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        if sub_value is not None:
                            if sub_key not in original_data['dimensions_details'][0][key]:
                                original_data['dimensions_details'][0][key][sub_key] = sub_value
                            else:
                                original_data['dimensions_details'][0][key][sub_key] = sub_value
                else:
                    if value is not None:
                        original_data['dimensions_details'][0][key] = value

            # Обновляем additional_info
            if 'additional_info' in original_data:
                if 'package_dimensions' in original_data['additional_info']:
                    for key, value in excel_model_data['additional_info']['package_dimensions'].items():
                        if value is not None:
                            original_data['additional_info']['package_dimensions'][key] = value
                if 'volume' in original_data['additional_info']:
                    if excel_model_data['additional_info']['volume'] is not None:
                        original_data['additional_info']['volume'] = excel_model_data['additional_info']['volume']

            # Обновляем прочие поля
            if 'skeleton' in original_data and excel_model_data['dimensions_details'].get('skeleton') is not None:
                original_data['skeleton'] = excel_model_data['dimensions_details'].get('skeleton')
            if 'minpromtorg' in original_data:
                minpromtorg_value = excel_model_data['dimensions_details'].get('minpromtorg')
                if minpromtorg_value is not None:
                    original_data['minpromtorg'] = minpromtorg_value
                else:
                    original_data['minpromtorg'] = "-"  # или "", если нужно пустое значение

            if 'typeofproduct' in original_data and excel_model_data['dimensions_details'].get('typeofproduct') is not None:
                original_data['typeofproduct'] = excel_model_data['dimensions_details'].get('typeofproduct')

            # Обновляем max_load и recommended_load в guarantee
            if 'guarantee' in original_data and len(original_data['guarantee']) > 0:
                if 'max_load' in original_data['guarantee'][0] and excel_model_data['dimensions_details'].get('max_load') is not None:
                    original_data['guarantee'][0]['max_load'] = format_number(excel_model_data['dimensions_details'].get('max_load'))
                if 'recommended_load' in original_data['guarantee'][0] and excel_model_data['dimensions_details'].get('recommended_load') is not None:
                    original_data['guarantee'][0]['recommended_load'] = format_number(excel_model_data['dimensions_details'].get('recommended_load'))

            # Обновляем transportation.packaging.size и box_size
            if 'transportation' in original_data and len(original_data['transportation']) > 0:
                if 'packaging' in original_data['transportation'][0]:
                    for key, value in excel_model_data['transportation']['size'].items():
                        if value is not None and value != '':
                            clean_value = remove_trailing_zero(value)
                            original_data['transportation'][0]['packaging']['size'][key] = clean_value

                    width = original_data['transportation'][0]['packaging']['size'].get('width', '')
                    depth = original_data['transportation'][0]['packaging']['size'].get('depth', '')
                    height = original_data['transportation'][0]['packaging']['size'].get('height', '')
                    if width and depth and height:
                        original_data['transportation'][0]['packaging']['box_size'] = f"{width}х{depth}х{height}"

            # Обновляем brutto и netto в dimensions
            if 'dimensions' in original_data and len(original_data['dimensions']) > 0:
                if 'brutto' in original_data['dimensions'][0] and excel_model_data['dimensions_details'].get('brutto') is not None:
                    original_data['dimensions'][0]['brutto'] = format_number(excel_model_data['dimensions_details'].get('brutto'))
                if 'netto' in original_data['dimensions'][0] and excel_model_data['dimensions_details'].get('netto') is not None:
                    data['dimensions'][0]['netto'] = format_number(excel_model_data['dimensions_details'].get('netto'))

            # Обновляем volume в dimensions
            if 'dimensions' in original_data and len(original_data['dimensions']) > 0 and excel_model_data['additional_info'].get('volume') is not None:
                original_data['dimensions'][0]['volume'] = format_number(excel_model_data['additional_info'].get('volume'))

            # Сравниваем и логируем изменения
            compare_and_log_changes(original_data_copy, original_data, json_file)

            # Сохраняем обновленный JSON
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(original_data, f, ensure_ascii=False, indent=4)
        else:
            failed_updates.append((json_file, "Модель не найдена в Excel"))
            if 'lost' not in original_data:
                original_data['lost'] = [{'clean': False, 'limit': False, 'del': True}]
            else:
                if isinstance(original_data['lost'], list) and len(original_data['lost']) > 0:
                    original_data['lost'][0]['del'] = True
                else:
                    original_data['lost'] = [{'clean': False, 'limit': False, 'del': True}]
            # Сохраняем обновленный JSON
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(original_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        failed_updates.append((json_file, str(e)))

# Вывод списка файлов, которые не удалось обновить
with open('failed_updates.txt', 'w', encoding='utf-8') as f:
    for file, reason in failed_updates:
        f.write(f"{file}: {reason}\n")

# Вывод списка файлов, где обновление не произошло
with open('skipped_updates.txt', 'w', encoding='utf-8') as f:
    for file, reason in skipped_updates:
        f.write(f"{file}: {reason}\n")

# Записываем модели, отсутствующие в JSON
with open('missing_in_json.txt', 'w', encoding='utf-8') as f:
    for model in missing_in_json:
        f.write(f"{model}\n")

print("Обновление завершено. Список неудачных обновлений в failed_updates.txt, пропущенных обновлений в skipped_updates.txt, отсутствующих моделей в missing_in_json.txt")
# print(normalize_model_name("Стул Изо +"))

# name = "Стул Изо +"
# print("Исходное:", name)
# name = name.lower().strip()
# print("После lower и strip:", name)
# name = re.sub(r'\bстул\b|\bкресло\b|Кресло UTFC\b', '', name, flags=re.IGNORECASE)
# print("После удаления 'стул':", name)
# name = re.sub(r'\s+', ' ', name)
# print("После замены пробелов:", name)
# name = re.sub(r'[^\w\s+]', '', name)
# print("После удаления неразрешённых символов:", name)
excel_name = "Кресло UTFC Онтарио М-405 Н/п пластик/хром"
json_name = "UTFC Онтарио М-405 Н_п пластик хром"
print("Excel:", normalize_model_name(excel_name))
print("JSON:", normalize_model_name(json_name))