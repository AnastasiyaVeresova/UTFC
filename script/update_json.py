import os
import json

def update_dimensions_in_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'dimensions_details' in data:
        for item in data['dimensions_details']:
            for key in item:
                if isinstance(item[key], dict) and 'max' in item[key] and 'min' not in item[key]:
                    item[key]['min'] = ""

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                update_dimensions_in_json(file_path)
                print(f"Обработан файл: {file_path}")

if __name__ == "__main__":
    folder_path = r"C:\Users\UTFC\Documents\Downloads\to\products"
    process_folder(folder_path)
    print("Готово!")
