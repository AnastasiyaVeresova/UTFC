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

# Чтение Excel
excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

# Создание словаря с данными из Excel
excel_data = {}
models_excel = df.iloc[3:, 0].dropna().tolist()

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
    'Unnamed: 34': ('recommended_load', None, None),
    'Unnamed: 35': ('max_load', None, None),
    'Unnamed: 36': ('skeleton', None, None),
    'Unnamed: 37': ('minpromtorg', None, None),
    'Unnamed: 38': ('typeofproduct', None, None),
    'Unnamed: 39': ('netto', None, None),
    'Unnamed: 40': ('brutto', None, None),
    'Unnamed: 41': ('package_width', None, None),
    'Unnamed: 42': ('package_depth', None, None),
    'Unnamed: 43': ('package_height', None, None),
    'Unnamed: 44': ('volume', None, None)
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
            # Удаляем модель из missing_in_json, если она найдена в JSON
            missing_in_json.discard(excel_model)

            excel_model_data = excel_data[excel_model]

            # Обновляем dimensions_details
            if 'dimensions_details' in data and len(data['dimensions_details']) > 0:
                for key, value in excel_model_data['dimensions_details'].items():
                    if key in data['dimensions_details'][0]:
                        if isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_value is not None:
                                    data['dimensions_details'][0][key][sub_key] = sub_value
                        else:
                            if value is not None:
                                data['dimensions_details'][0][key] = value

            # Обновляем additional_info
            if 'additional_info' in data:
                if 'package_dimensions' in data['additional_info']:
                    for key, value in excel_model_data['additional_info']['package_dimensions'].items():
                        if value is not None:
                            data['additional_info']['package_dimensions'][key] = value
                if 'volume' in data['additional_info']:
                    if excel_model_data['additional_info']['volume'] is not None:
                        data['additional_info']['volume'] = excel_model_data['additional_info']['volume']

            # Обновляем прочие поля
            if 'skeleton' in data and excel_model_data['dimensions_details'].get('skeleton') is not None:
                data['skeleton'] = excel_model_data['dimensions_details'].get('skeleton')
            if 'minpromtorg' in data and excel_model_data['dimensions_details'].get('minpromtorg') is not None:
                data['minpromtorg'] = excel_model_data['dimensions_details'].get('minpromtorg')
            if 'typeofproduct' in data and excel_model_data['dimensions_details'].get('typeofproduct') is not None:
                data['typeofproduct'] = excel_model_data['dimensions_details'].get('typeofproduct')

            # Обновляем max_load и recommended_load в guarantee
            if 'guarantee' in data and len(data['guarantee']) > 0:
                if 'max_load' in data['guarantee'][0] and excel_model_data['dimensions_details'].get('max_load') is not None:
                    data['guarantee'][0]['max_load'] = format_number(excel_model_data['dimensions_details'].get('max_load'))
                if 'recommended_load' in data['guarantee'][0] and excel_model_data['dimensions_details'].get('recommended_load') is not None:
                    data['guarantee'][0]['recommended_load'] = format_number(excel_model_data['dimensions_details'].get('recommended_load'))

            # Обновляем brutto и netto в dimensions
            if 'dimensions' in data and len(data['dimensions']) > 0:
                if 'brutto' in data['dimensions'][0] and excel_model_data['dimensions_details'].get('brutto') is not None:
                    data['dimensions'][0]['brutto'] = format_number(excel_model_data['dimensions_details'].get('brutto'))
                if 'netto' in data['dimensions'][0] and excel_model_data['dimensions_details'].get('netto') is not None:
                    data['dimensions'][0]['netto'] = format_number(excel_model_data['dimensions_details'].get('netto'))

            # Обновляем volume в dimensions
            if 'dimensions' in data and len(data['dimensions']) > 0 and excel_model_data['additional_info'].get('volume') is not None:
                data['dimensions'][0]['volume'] = format_number(excel_model_data['additional_info'].get('volume'))

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