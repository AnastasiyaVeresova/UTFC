import pandas as pd
import json
import os
import re
import math

# exceptions_del_false = [
#     "самба люкс gtp tg столик",
#     "самба люкс gtp tg/столик",
#     "сн-710 айкью н пластик",
#     "сн-710 айкью н_п",
#     "соло макс ch-602 пластик",
#     "соло макс ch-602 хром",
#     "сильвия арм хром",
#     "сильвия хром"
# ]

parents_mapping = {
    # 'модель_дочерняя': 'модель_родитель',
    'кора ch': 'кора чёрный',
    'стандарт gr': 'стандарт',
    'стандарт': 'стандарт',
    'неон bl': 'неон',
    'табурет кр bl': 'табурет кр',
    'табурет кр ch': 'табурет кр',
    'табурет пр bl': 'табурет пр',
    'табурет пр ch': 'табурет пр',
    'табурет кр gr': 'табурет кр',
    'табурет пр gr': 'табурет пр',
    'изо gr': 'изо',
    'изо bl': 'изо',
    'изо ch': 'изо',
    'изо со столиком bl': 'стул изо со столиком',
    'изо со столиком ch': 'стул изо со столиком',
    'венус ch': 'венус',
    'венус gr': 'венус',
    'венус bl': 'венус',
    'венус м bl': 'венус м',
    'венус м gr': 'венус м',
    'венус м ch': 'венус м',
    'изо пластик bl': 'изо пластик',
    'изо пластик +': 'изо пластик +',
    'utfc киото м-250 cерый плаcтик': 'utfc киото м-250',
    'utfc мориока м-242 зеленый плаcтик': 'utfc мориока м-242',
    'utfc мориока м-242 краcный плаcтик': 'utfc мориока м-242',
    'utfc мориока м-242 черный плаcтик': 'utfc мориока м-242',
    'utfc оcака м-201 краcный плаcтик':'utfc оcака м-201',
    'utfc оcака м-201 черный плаcтик':'utfc оcака м-201',
    'utfc cанда м-207 черный плаcтик':'utfc cанда м-207',
    'utfc онтарио м-105 пластик хром': 'utfc онтарио м-105 пластик/хром', 
    'utfc канзас сн-111 в пластик хром': 'канзас utfc сн-111 в пластик/хром',
    'utfc канзас сн-111 в 3d хром':'канзас utfc сн-111 в 3d пластик/хром',
    'utfc канзас м-111 пластик хром': 'utfc канзас м-111 пластик/хром',
    'utfc онтарио сн-105 в пластик хром': 'онтарио utfc сн-105 в пластик/хром',
    'utfc онтарио сн-105 н пластик хром': 'онтарио utfc сн-105 н пластик/хром',
    'utfc онтарио сн-105 в 3d хром cр':'онтарио utfc сн-105 в 3d хром',
    'epik a-130-g brown':'epik a-130-g',
    'epik a-130-g gr':'epik a-130-g',
    'epik a-155-g темно-cиний':'epik a-155-g',
    'epik a-155-g пеcочный':'epik a-155-g',
    'биcтро bl':'биcтро',
    'биcтро gr':'биcтро',
    'биcтро ch':'биcтро',
    'биcтро м bl':'биcтро м',
    'биcтро м gr':'биcтро м',
    'биcтро м ch':'биcтро м',
    'ванесса ch':'ванесса',
    'ванесса bl':'ванесса',
    'верcаль ch':'верcаль ch',
    'компакт люкc cкладной gr':'компакт люкc cкладной',
    'компакт складной gr':'компакт складной',
    'компакт люкc 4н cкладной gr':'компакт люкc 4н cкладной',
    'компакт 4н складной gr':'компакт 4н складной',
    'неон ch':'неон',
    'неон gr':'неон',
    'неон bl':'неон',
    'cамба bl':'cамба',
    'cамба ch':'cамба',
    'cамба gr':'cамба',
    'cамба soft bl':'cамба',
    'cамба soft ch':'cамба',
    'cамба soft gr':'cамба',
    'cамба cо cтоликом bl':'cамба cо cтоликом',
    'cамба cо cтоликом soft ch':'cамба cо cтоликом',
    'cамба cо cтоликом soft bl':'cамба cо cтоликом',
    'самба люкс gtp tg столик':'самба люкс gtp tg/столик',
    'cофия bl':'cофия',
    'cофия cо cтоликом bl':'cофия cо cтоликом',
    'cтандарт gr':'cтандарт',
    'форум bl':'форум',
    'форум ch':'форум',
    'шелл с-07 софт':'шелл с-07 софт',
    'шелл с-07 софт bl':'шелл с-07 софт',
    'шелл с-07 софт gr':'шелл с-07 софт',
    'шелл с-07':'шелл с-07',
    'шелл с-07 bl':'шелл с-07',
    'шелл с-07 gr':'шелл с-07',
    'шелл gts с-21 софт белый':'шелл gts с-21 софт белый',
    'шелл gts с-21 софт черный':'шелл gts с-21 софт черный',
    'cтул кассира':'Стул кассира б_п',
    'дэли ch-503 white ch':'дэли сн-503 н/п хром',
    'дэли ch-503 белый пластик':'дэли сн-503 белый пластик',
    'дэли сн-503 н/п хром':'дэли ch-503 н_п хром',
    'ультра т-01 н пластик pl660':'ультра т-01 н пластик pl660',
    'ультра т-02 н пластик pl660':'ультра т-02 н пластик pl660',
    'ультра н 2д пластик': 'ультра т-02 н пластик',
    'epik e-201-g m021':'epik e-201-g',
    'epik а-011-g 201':'кресло epik а-011-g',
    'epik а-011-g 200':'кресло epik а-011-g',
    'epik e-222-g':'epik e-222-g s001-115',
    'epik a-155-g темно-синий':'epik a-155-g',
    'epik а-007-g l170':'кресло epik а-007-g',
    'epik а-007-g l200':'кресло epik а-007-g',
    'epik а-001-mb l235-187':'кресло epik а-001-mb',
    'epik а-001-mb l171-172':'кресло epik а-001-mb',
    'epik а-001-mb 235-187':'кресло epik а-001-mb',
    'epik а-001-mb 201-235':'кресло epik а-001-mb',
    'epik а-001-gb l201-271':'кресло epik а-001-mb',
    'epik p-700 plw tw69-128':'кресло epik р-700 ',
    'epik p-700 pl tw69-128':'кресло epik р-700 ',
    # 'epik p-521-sb m021':'кресло epik р-521-sb',   не получилось
    'epik e-222-g s001-115':'кресло epik e-222-mb',
    'epik a-181-g l200':'кресло epik a-181-g',
    'epik a-112-g l113 кэмел':'кресло epik a-112-g',
    'чико 4l bl':'чико 4l хром',
    'марко ch':'марко',
    'стул кассира б_п':'стул кассира б/п',
    'айкью сн-710 н_п':'айкью н/п сн-710',
    'айкью сн-710 н_п bl':'айкью н/п сн-710',
    'айкью н сн-710 пластик':'айкью н сн-710 пластик',
    'айкью сн-710 пластик':'айкью сн-710 пластик',    
    'соло макс ch-602 пластик':'соло max сн-602 пластик',
    'соло макс ch-602 хром':'соло max сн-602 хром',
    'соло макс комби хром':'соло max сн-602 хром',
    'соло макс комби пластик':'соло max сн-602 пластик',
    'честер 4l bl':'честер 4l хром',
    'верона к-10 н_п дерево':'верона к-10 н/п дерево',
    'честер хром':'честер хром',
    'софия со столиком ch':'софия со столиком',
    'софия со столиком bl':'софия со столиком',
    'софия ch':'софия',
    'Версаль bl':'Версаль',
    'софия bl':'софия',
    'сильвия арм хром':'сильвия арм хром',
    'сильвия хром':'сильвия хром',
    'кайман комфорт ch-301 в bl':'кайман комфорт сн-301 в хром',
    'кайман в топ-ган lux':'',
    'кайман трио сн-303 в bl':'кайман трио сн-303 в хром',
    'кайман трио сн-303 н bl':'кайман трио сн-303 н хром',
    'кайман трио ch-303 н_п bl':'',
    'кайман комфорт сн-301 н/п bl':'',
    'бистро м bl':'стул бистро м',
    'бистро м ch':'стул бистро м',
    'бистро м gr':'стул бистро м',
    'бистро ch':'стул бистро',
    'бистро bl':'стул бистро',
    'бистро gr':'стул бистро',
    'Нерон ch':'нерон',
    '':'',
    '':''
    
    # 'кайман ch-300 н_п bl':'кайман сн-300 н/п хром',    не получилось

}
# Пример: добавляем новые модели в parents_mapping
new_parents_mapping = {
    'новая_модель1': 'родитель1',
    'новая_модель2': 'родитель2',
}
parents_mapping.update(new_parents_mapping)


    # "lost": [
    #     {
    #         "clean": false,
    #         "limit": false,
    #         "del": false
    #     }
# НЕ СРАБАТЫВАЕТ ДЛЯ
# "самба люкс gtp tg столик",

    # ]

# Функция нормализации имени модели
def normalize_karkas_name(name):
    if not isinstance(name, str):
        return ""
    name = name.strip()

    # Обработка SN-602 и подобных
    # name = re.sub(r'ch[-_]?(\d+)', r'ch-\1', name, flags=re.IGNORECASE)
    # name = re.sub(r'max\s+сн[-_]?(\d+)', r'сн-\1', name, flags=re.IGNORECASE)
    name = re.sub(r'сн\s*[-_]\s*(\d+)', r'сн-\1', name, flags=re.IGNORECASE)

    # Теперь все вариации с сн-602 и ch-602 приводим к одинаковому виду

    # Остальные замены
    name = name.replace('_', '/')
    name = re.sub(r'стул|кресло|кресло utfc', '', name, flags=re.IGNORECASE)
    name = re.sub(r'с\s*[-_]?\s*(\d+)', r'с-\1', name, flags=re.IGNORECASE)
    name = re.sub(r'с\s*-?\s*800\s+энжел', 'энжел', name, flags=re.IGNORECASE)
    name = re.sub(r'н\/п|н_п', 'н_п', name, flags=re.IGNORECASE)
    name = re.sub(r'б\/п|б_п', 'б_п', name, flags=re.IGNORECASE)
    name = re.sub(r'[/\\]', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[^\w\s+-]', '', name)
    name = re.sub(r'пластик\/хром|пластик хром', 'пластик хром', name, flags=re.IGNORECASE)
    name = re.sub(r'хром\/хдп\/мб|хром хдп мб', 'хром хдп мб', name, flags=re.IGNORECASE)
    name = re.sub(r'дерево\/мб|дерево мб', 'дерево мб', name, flags=re.IGNORECASE)
    # Удаляем замену 'с' на 'c', чтобы сохранить оригинальные слова
    # name = re.sub(r'с', 'c', name, flags=re.IGNORECASE)
    name = re.sub(r'в\/п', 'вп', name, flags=re.IGNORECASE)
    name = re.sub(r'х\/дп', 'хдп', name, flags=re.IGNORECASE)
    name = re.sub(r'м\/б', 'мб', name, flags=re.IGNORECASE)
    name = re.sub(r'тг', 'tg', name, flags=re.IGNORECASE)
    name = re.sub(r'пвм', 'пвм', name, flags=re.IGNORECASE)    
    name = re.sub(r'tg\s+столик', 'tg столик', name, flags=re.IGNORECASE)
    name = re.sub(r'пиастра\s+столик', 'пиастра столик', name, flags=re.IGNORECASE)
    name = re.sub(r'пластик\s+хром', 'пластик хром', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+', ' ', name).strip()

    return name.lower()
    

parents_mapping_normalized = {}
for key, value in parents_mapping.items():
    normalized_key = normalize_karkas_name(key)
    parents_mapping_normalized[normalized_key] = value

# Преобразование пустых значений
def normalize_value(value):
    if isinstance(value, str) and value.strip() in ('', '-', '--'):
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    if value is None:
        return ""
    return str(value)

def format_number(value):
    if isinstance(value, str):
        try:
            num = float(value.replace(',', '.'))
            rounded_num = round(num, 2)
            # Возвращаем в виде строки с двумя знаками
            return f"{rounded_num:.2f}".replace('.', ',')
        except:
            return value
    elif isinstance(value, (int, float)):
        rounded_num = round(value, 2)
        return f"{rounded_num:.2f}".replace('.', ',')
    return value

def format_number_whole(value):
    if isinstance(value, (int, float)):
        return f"{round(value, 2):.2f}".replace('.', ',')
    if isinstance(value, str):
        try:
            num = float(value.replace(',', '.'))
            return f"{round(num, 2):.0f}".replace('.', ',')
        except:
            return value
    return value

excel_path = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
df = pd.read_excel(excel_path, sheet_name='Размеры')

excel_data = {}
karkass_excel = df.iloc[3:, 1].dropna().tolist()

columns_mapping = {
    'Unnamed: 2': ('chair_height', 'min', 'max'),
    'Unnamed: 4': ('headrest_height', 'min', 'max'),
    'Unnamed: 6': ('seat_to_floor_height', 'min', 'max'),
    'Unnamed: 8': ('seat_to_floor_height_upper', 'min', 'max'),
    'Unnamed: 10': ('armrest_height_from_floor', 'min', 'max'),
    'Unnamed: 12': ('armrest_height_from_seat', 'min', 'max'),
    'Unnamed: 14': ('armrest_width_support', None, 'max'),
    'Unnamed: 15': ('armrest_length_support', None, 'max'),
    'Unnamed: 17': ('chair_depth', 'min', None),
    'Unnamed: 19': ('seat_depth', 'min', 'max'),
    'Unnamed: 21': ('seat_depth_km', None, 'max'),
    'Unnamed: 22': ('backrest_height', None, 'max'),
    'Unnamed: 23': ('backrest_to_seat_height', 'min', 'max'),
    'Unnamed: 25': ('backrest_height_external', None, 'max'),
    'Unnamed: 27': ('seat_width_with_armrests', 'min', 'max'),
    'Unnamed: 29': ('seat_width', None, 'max'),
    'Unnamed: 30': ('backrest_width_narrow', None, 'max'),
    'Unnamed: 31': ('backrest_width_wide', None, 'max'),
    'Unnamed: 32': ('diameter_cross', None, 'max'),
    'Unnamed: 33': ('runners_width', None, 'max'),
    'Unnamed: 34': ('runners_depth', None, 'max'),
    'Unnamed: 35': ('recommended_load', None, None),
    'Unnamed: 36': ('max_load', None, None),
    'Unnamed: 37': ('skeleton', None, None),
    'Unnamed: 38': ('minpromtorg', None, None),
    'Unnamed: 39': ('netto', None, None),
    'Unnamed: 40': ('brutto', None, None),
    'Unnamed: 41': ('package_width', None, None),
    'Unnamed: 42': ('package_depth', None, None),
    'Unnamed: 43': ('package_height', None, None),
    'Unnamed: 44': ('volume', None, None),
    'Unnamed: 45': ('box_on_pallet', None, None),
    'Unnamed: 46': ('pallet_width', None, None),
}

for i, karkas in enumerate(karkass_excel):
    normalized_karkas = normalize_karkas_name(karkas)
    karkas_data = {
        "karkas": karkas,
        "normalized": normalized_karkas,
        "dimensions_details": {},
        "additional_info": {}
    }

    for col, (key, min_key, max_key) in columns_mapping.items():
        if min_key is not None and max_key is not None:
            karkas_data["dimensions_details"][key] = {
                "min": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
                "max": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc(col) + 1]))
            }
        elif min_key is not None:
            karkas_data["dimensions_details"][key] = {
                "min": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)])),
                "max": None
            }
        elif max_key is not None:
            karkas_data["dimensions_details"][key] = {
                "max": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))
            }
        else:
            karkas_data["dimensions_details"][key] = format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc(col)]))

    karkas_data["additional_info"] = {
        "package_dimensions": {
            "width": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 40')])),
            "depth": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 41')])),
            "height": format_number_whole(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 42')]))
        },
        "netto": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 39')])),
        "brutto": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 40')])),
        "volume": format_number(normalize_value(df.iloc[i + 3, df.columns.get_loc('Unnamed: 44')]))
    }
    

    excel_data[normalized_karkas] = karkas_data

products_dir = r'C:\Users\UTFC\Documents\БалтМебель\to\products'

json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

missing_in_json = set(excel_data.keys())

all_dimension_params = [
    "chair_height", "headrest_height", "seat_to_floor_height", "armrest_height_from_seat",
    "chair_depth", "seat_depth", "backrest_height", "backrest_to_seat_height",
    "seat_width_with_armrests", "seat_width", "diameter_cross", "runners_width",
    "runners_depth", "seat_to_floor_height_upper", "armrest_height_from_floor",
    "armrest_width_support", "armrest_length_support", "seat_depth_km",
    "backrest_height_external", "backrest_width_narrow", "backrest_width_wide",
    "recommended_load", "max_load", "skeleton", "minpromtorg",
    "netto", "brutto", "package_width", "package_depth", "package_height", "volume"
]

failed_updates = []


# Собираем все нормализованные имена моделей из JSON-файлов
all_json_karkass = set()
for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        karkas_name = data.get('namefile', [''])[0] if isinstance(data.get('namefile'), list) else data.get('namefile', '')
        if not karkas_name:
            karkas_name = data.get('name', [''])[0] if isinstance(data.get('name'), list) else data.get('name', '')
        normalized_name = normalize_karkas_name(karkas_name)
        all_json_karkass.add(normalized_name)
    except Exception as e:
        print(f"Ошибка при чтении {json_file}: {e}")

# Находим модели, которые есть в JSON, но нет в Excel
karkass_only_in_json = all_json_karkass - set(excel_data.keys())
print("Модели, которые есть в JSON, но отсутствуют в Excel:")
for karkas in sorted(karkass_only_in_json):
    print(f"  - {karkas}")

    # Находим модели, которые есть в Excel, но нет в JSON
karkass_only_in_excel = set(excel_data.keys()) - all_json_karkass
print("Модели, которые есть в Excel, но отсутствуют в JSON:")
for karkas in sorted(karkass_only_in_excel):
    print(f"  - {karkas}")
    

# Функция для наследования параметров
def inherit_parameters(child_data, parent_data):
    # Наследуем dimensions_details
    if 'dimensions_details' not in child_data:
        child_data['dimensions_details'] = [{}]
    if not isinstance(child_data['dimensions_details'], list):
        child_data['dimensions_details'] = [child_data['dimensions_details']]
    if len(child_data['dimensions_details']) == 0:
        child_data['dimensions_details'] = [{}]

    dimensions = child_data['dimensions_details'][0]
    for key, value in parent_data['dimensions_details'].items():
        if isinstance(value, dict):
            if key not in dimensions:
                dimensions[key] = {}
            for sub_key, sub_value in value.items():
                if sub_value is not None and sub_value != "":
                    # Форматируем числовые поля
                    dimensions[key][sub_key] = format_number_whole(sub_value)
        else:
            if value is not None and value != "":
                dimensions[key] = format_number_whole(value)

    # Наследуем additional_info
    if 'additional_info' not in child_data:
        child_data['additional_info'] = {}
    for key, value in parent_data['additional_info'].items():
        if isinstance(value, dict):
            if key not in child_data['additional_info']:
                child_data['additional_info'][key] = {}
            for sub_key, sub_value in value.items():
                if sub_value is not None and sub_value != "":
                    child_data['additional_info'][key][sub_key] = format_number_whole(sub_value)
        else:
            if value is not None and value != "":
                child_data['additional_info'][key] = format_number_whole(value)

    # Наследуем netto, brutto, volume в корне или в dimensions[0]
    # if 'dimensions' in child_data and len(child_data['dimensions']) > 0:
    #     if 'netto' in parent_data['additional_info'] and parent_data['additional_info']['netto']:
    #         child_data['dimensions'][0]['netto'] = format_number(parent_data['additional_info']['netto'])
    #     if 'brutto' in parent_data['additional_info'] and parent_data['additional_info']['brutto']:
    #         child_data['dimensions'][0]['brutto'] = format_number(parent_data['additional_info']['brutto'])
    #     if 'volume' in parent_data['additional_info'] and parent_data['additional_info']['volume']:
    #         child_data['dimensions'][0]['volume'] = format_number(parent_data['additional_info']['volume'])
    # else:
    #     if 'netto' in parent_data['additional_info'] and parent_data['additional_info']['netto']:
    #         child_data['netto'] = format_number(parent_data['additional_info']['netto'])
    #     if 'brutto' in parent_data['additional_info'] and parent_data['additional_info']['brutto']:
    #         child_data['brutto'] = format_number(parent_data['additional_info']['brutto'])
    #     if 'volume' in parent_data['additional_info'] and parent_data['additional_info']['volume']:
    #         child_data['volume'] = format_number(parent_data['additional_info']['volume'])

    # Наследуем guarantee[0].max_load и guarantee[0].recommended_load
    if 'guarantee' in child_data and len(child_data['guarantee']) > 0:
        if 'max_load' in parent_data['dimensions_details'] and parent_data['dimensions_details']['max_load']:
            child_data['guarantee'][0]['max_load'] = format_number_whole(parent_data['dimensions_details']['max_load'])
        if 'recommended_load' in parent_data['dimensions_details'] and parent_data['dimensions_details']['recommended_load']:
            child_data['guarantee'][0]['recommended_load'] = format_number_whole(parent_data['dimensions_details']['recommended_load'])



# Обновляем все модели, включая дочерние
for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            original_data = json.load(f)

        karkas_name = original_data.get('namefile', [''])[0] if isinstance(original_data.get('namefile'), list) else original_data.get('namefile', '')
        if not karkas_name:
            karkas_name = original_data.get('name', [''])[0] if isinstance(original_data.get('name'), list) else original_data.get('name', '')

        normalized_name = normalize_karkas_name(karkas_name)
        print(f"Обрабатываем файл: {json_file}, модель: {karkas_name}, нормализованное: {normalized_name}")

        # Ищем родительскую модель
        parent_karkas_name = parents_mapping.get(normalized_name)
        if parent_karkas_name:
            parent_karkas_name = normalize_karkas_name(parent_karkas_name)
            print(f"Родительская модель для {normalized_name}: {parent_karkas_name}")
            if parent_karkas_name in excel_data:
                parent_data = excel_data[parent_karkas_name]
                print(f"Наследование: {normalized_name} -> {parent_karkas_name}")
                inherit_parameters(original_data, parent_data)
            else:
                print(f"ОШИБКА: Родительская модель {parent_karkas_name} отсутствует в Excel!")
        else:
            print(f"Нет родительской модели для {normalized_name} в parents_mapping")

        # Прямое обновление из Excel, если модель есть в Excel
        if normalized_name in excel_data:
            excel_karkas_data = excel_data[normalized_name]
            if 'dimensions_details' not in original_data or not original_data.get('dimensions_details'):
                original_data['dimensions_details'] = [{}]

            if isinstance(original_data.get('dimensions_details'), list) and len(original_data['dimensions_details']) > 0:
                dimensions = original_data['dimensions_details'][0]
            else:
                dimensions = {}
                original_data['dimensions_details'] = [dimensions]

            for param in all_dimension_params:
                if param not in dimensions:
                    dimensions[param] = {"min": "", "max": ""}

            for key, value in excel_karkas_data['dimensions_details'].items():
                if key in dimensions:
                    if isinstance(value, dict):
                        for sub_key, sub_value in value.items():
                            if sub_value is not None and sub_value != "":
                                if key not in dimensions:
                                    dimensions[key] = {}
                                dimensions[key][sub_key] = sub_value
                    else:
                        if value is not None and value != "":
                            dimensions[key] = value

            if 'additional_info' in original_data:
                if 'package_dimensions' in original_data['additional_info']:
                    for key, value in excel_karkas_data['additional_info']['package_dimensions'].items():
                        if value is not None and value != "":
                            original_data['additional_info']['package_dimensions'][key] = value
                if 'volume' in original_data['additional_info']:
                    if excel_karkas_data['additional_info']['volume'] is not None:
                        original_data['additional_info']['volume'] = excel_karkas_data['additional_info']['volume']

            if 'skeleton' in original_data and excel_karkas_data['dimensions_details'].get('skeleton') is not None:
                original_data['skeleton'] = excel_karkas_data['dimensions_details'].get('skeleton')
            if 'minpromtorg' in original_data and excel_karkas_data['dimensions_details'].get('minpromtorg') is not None:
                original_data['minpromtorg'] = excel_karkas_data['dimensions_details'].get('minpromtorg')

            if 'guarantee' in original_data and len(original_data['guarantee']) > 0:
                if 'max_load' in original_data['guarantee'][0] and excel_karkas_data['dimensions_details'].get('max_load') is not None:
                    original_data['guarantee'][0]['max_load'] = format_number_whole(excel_karkas_data['dimensions_details'].get('max_load'))
                if 'recommended_load' in original_data['guarantee'][0] and excel_karkas_data['dimensions_details'].get('recommended_load') is not None:
                    original_data['guarantee'][0]['recommended_load'] = format_number_whole(excel_karkas_data['dimensions_details'].get('recommended_load'))

        # Проверяем наличие 'dimensions' и его структуру
            if 'dimensions' in original_data:
                dims = original_data['dimensions']
                # Если dims — список, берем первый элемент
                if isinstance(dims, list):
                    if len(dims) == 0:
                        original_data['dimensions'] = [{}]
                        dims = original_data['dimensions'][0]
                    else:
                        dims = dims[0]
                # Если dims — не словарь, создаем список с одним словарем
                elif not isinstance(dims, dict):
                    original_data['dimensions'] = [{}]
                    dims = original_data['dimensions'][0]
            else:
                # Если 'dimensions' нет, создаем список с одним словарем
                original_data['dimensions'] = [{}]
                dims = original_data['dimensions'][0]

            # Теперь можно безопасно обновлять
            if excel_karkas_data['additional_info'].get('netto') is not None:
                dims['netto'] = format_number(excel_karkas_data['additional_info'].get('netto'))
            if excel_karkas_data['additional_info'].get('brutto') is not None:
                dims['brutto'] = format_number(excel_karkas_data['additional_info'].get('brutto'))
            volume_value = excel_karkas_data['additional_info'].get('volume')
            if volume_value is not None:
                if volume_value == "0,00":
                    dims['volume'] = ""
                else:
                    dims['volume'] = format_number(volume_value)

                
        # if normalized_name not in excel_data:
        #     # Проверяем наличие блока 'lost'
        #     if 'lost' in original_data and isinstance(original_data['lost'], list) and len(original_data['lost']) > 0:
        #         # Обновляем только 'del' в первом элементе
        #         original_data['lost'][0]['del'] = True
            # else:
                # Если блока нет или структура не та, создаем новый
                # original_data['lost'] = [{
                #     "clean": False,
                #     "limit": False,
                #     "del": False
                # }]

        # model_name_for_del = normalized_name.lower()
        # if model_name_for_del in [name.lower() for name in exceptions_del_false]:
        #     original_data['lost'][0]['del'] = False
        # else:
        #     original_data['lost'][0]['del'] = True

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(original_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        failed_updates.append((json_file, str(e)))

with open('failed_updates.txt', 'w', encoding='utf-8') as f:
    for file, reason in failed_updates:
        f.write(f"{file}: {reason}\n")

with open('missing_in_json.txt', 'w', encoding='utf-8') as f:
    for karkas in missing_in_json:
        f.write(f"{karkas}\n")

print("Обновление завершено. Список неудачных обновлений в failed_updates.txt, отсутствующих моделей в missing_in_json.txt")

# Собираем список дочерних моделей, для которых нет родителя в Excel
missing_parents = {}
missing_json = {}

for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Проверяем, что data — это словарь, а не список
        if not isinstance(data, dict):
            print(f"Пропускаем {json_file}: неожиданный формат данных (ожидался словарь)")
            continue
        karkas_name = data.get('namefile', [''])[0] if isinstance(data.get('namefile'), list) else data.get('namefile', '')
        if not karkas_name:
            karkas_name = data.get('name', [''])[0] if isinstance(data.get('name'), list) else data.get('name', '')
        if not karkas_name:
            print(f"Пропускаем {json_file}: не удалось определить имя модели")
            continue
        normalized_name = normalize_karkas_name(karkas_name)

        # Проверяем, есть ли модель в parents_mapping
        if normalized_name in parents_mapping:
            parent_karkas_name = normalize_karkas_name(parents_mapping[normalized_name])
            # Проверяем, есть ли родитель в Excel
            if parent_karkas_name not in excel_data:
                missing_parents[normalized_name] = parent_karkas_name

    except Exception as e:
        print(f"Ошибка при обработке {json_file}: {e}")
        continue

# Выводим список в формате для parents_mapping

all_json_karkass = set()


for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print(f"Пропускаем {json_file}: неожиданный формат данных (ожидался словарь)")
            continue
        karkas_name = data.get('namefile', [''])[0] if isinstance(data.get('namefile'), list) else data.get('namefile', '')
        if not karkas_name:
            karkas_name = data.get('name', [''])[0] if isinstance(data.get('name'), list) else data.get('name', '')
        if not karkas_name:
            print(f"Пропускаем {json_file}: не удалось определить имя модели")
            continue
        normalized_name = normalize_karkas_name(karkas_name)
        all_json_karkass.add(normalized_name)

        # Проверка родителя
        if normalized_name in parents_mapping:
            parent_karkas_name = normalize_karkas_name(parents_mapping[normalized_name])
            if parent_karkas_name not in excel_data:
                missing_parents[normalized_name] = parent_karkas_name

    except Exception as e:
        print(f"Ошибка при обработке {json_file}: {e}")
        continue

# Теперь собираем все модели из Excel
excel_models = set(excel_data.keys())

# Модели, есть в Excel, но нет в JSON
models_in_excel_not_in_json = excel_models - all_json_karkass

print("\nМодели, есть в Excel, но отсутствуют в JSON (их нужно добавить):")
for model in sorted(models_in_excel_not_in_json):
    print(f"  - {model}")
    #   моделей, для которых нет родителя в Excel (добавьте в parents_mapping):")
print("parents_mapping = {")
for child, parent in missing_parents.items():
    print(f"    '{child}': '{parent}',  # <--- Уточните родительскую модель!")
print("}")

# Сохраняем в файл
with open('missing_parents.txt', 'w', encoding='utf-8') as f:
    f.write("parents_mapping = {\n")
    for child, parent in missing_parents.items():
        f.write(f"    '{child}': '{parent}',  # <--- Уточните родительскую модель!\n")
    f.write("}\n")
print("\nСписок сохранён в missing_parents.txt")

test_strings = [
    "Онтарио СН-105 В пластик/хром",
    # 'сн-710 айкью н_п',
    # 'соло max сн-602 пластик',
    # 'соло макс ch-602 пластик',
    # 'epik p-521-sb m021:кресло epik р-521-sb',
    # "самба люкс gtp tg столик",
    # "сн-710 айкью н пластик",
    # "сн-710 айкью н_п",
    # "соло макс ch-602 пластик",
    # "соло макс ch-602 хром"
]

for s in test_strings:
    print(f"Original: {s}")
    print(f"Before normalization: {s}")
    normalized = normalize_karkas_name(s)
    print(f"After normalization: {normalized}")