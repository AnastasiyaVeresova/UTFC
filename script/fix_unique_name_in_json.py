import os
import json

def fix_unique_name_in_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'unique_name' in data and not isinstance(data['unique_name'], list):
        data['unique_name'] = [data['unique_name']]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    fix_unique_name_in_json(file_path)
                    print(f"Обработан: {file_path}")
                except Exception as e:
                    print(f"Ошибка при обработке {file_path}: {e}")

if __name__ == "__main__":
    target_dir = r"C:\Users\UTFC\Documents\Downloads\to\products"
    process_directory(target_dir)
    print("Готово!")
