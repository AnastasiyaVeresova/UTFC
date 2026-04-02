import os
import json

def merge_json_files_in_folder(folder_path):
    merged_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    merged_data.append(data)
                except json.JSONDecodeError:
                    print(f"Ошибка чтения файла: {filename}")
    return merged_data

def process_products_folder(base_path):
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            merged_data = merge_json_files_in_folder(folder_path)
            output_filename = f"{folder_name}.json"
            output_path = os.path.join(base_path, output_filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(merged_data, f, ensure_ascii=False, indent=4)
            print(f"Создан файл: {output_filename}")

# Укажите путь к папке products
products_path = r'C:\Users\UTFC\Documents\Downloads\to\products'
process_products_folder(products_path)
