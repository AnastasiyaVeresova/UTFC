import os
import json
import re

def sanitize_filename(name):
    """Заменяет недопустимые символы в имени файла на _"""
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', name)
    return sanitized.strip()

def rename_files_by_namefile(root_dir):
    for root, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.json'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if 'namefile' in data and data['namefile']:
                        new_name = data['namefile'][0]
                        new_name = sanitize_filename(new_name)
                        new_filepath = os.path.join(root, f"{new_name}.json")
                        if not os.path.exists(new_filepath):
                            os.rename(filepath, new_filepath)
                            print(f"Переименован: {filename} → {new_name}.json")
                        else:
                            print(f"Файл {new_name}.json уже существует, пропускаю.")
                    else:
                        print(f"В файле {filename} нет поля namefile или оно пустое.")
                except Exception as e:
                    print(f"Ошибка при обработке {filename}: {e}")

# Укажите путь к папке
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
rename_files_by_namefile(products_dir)
