import os
import json
import re

def process_transportation_block(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "transportation" and isinstance(value, str):
                data[key] = re.sub(r'^(Для|для)\s+', '', value, flags=re.IGNORECASE)
            elif isinstance(value, (dict, list)):
                data[key] = process_transportation_block(value)
    elif isinstance(data, list):
        return [process_transportation_block(item) for item in data]
    return data

def process_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = process_transportation_block(data)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    process_json_file(filepath)
                    print(f"Обработан: {filepath}")
                except Exception as e:
                    print(f"Ошибка при обработке {filepath}: {e}")

folder_path = r"C:\Users\UTFC\Documents\Downloads\to\products"
process_folder(folder_path)
