import os
import re

def cyr_to_lat(text):
    """Заменяет кириллические буквы на латинские аналоги"""
    cyr_to_lat_map = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch',
        'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
        'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    for cyr, lat in cyr_to_lat_map.items():
        text = text.replace(cyr, lat)
    return text

def sanitize_filename(name):
    """Убирает суффиксы и заменяет недопустимые символы"""
    name = re.sub(r'[-_]\w+$', '', name)  # убирает суффиксы типа -G, -MB
    name = cyr_to_lat(name)  # кириллица → латиница
    name = re.sub(r'[\\/*?:"<>|]', '_', name)  # недопустимые символы → _
    return name.strip()

def rename_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.json'):
                old_path = os.path.join(root, filename)
                new_name = sanitize_filename(filename[:-5]) + '.json'  # без .json → sanitize → + .json
                new_path = os.path.join(root, new_name)
                if old_path != new_path:
                    if not os.path.exists(new_path):
                        os.rename(old_path, new_path)
                        print(f"Переименован: {filename} → {new_name}")
                    else:
                        print(f"Файл {new_name} уже существует, пропускаю.")
                else:
                    print(f"Имя {filename} уже корректное.")

# Укажите путь к папке
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
rename_files(products_dir)
