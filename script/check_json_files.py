import os
import json

def check_json_files(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if "transportation" in data:
                            for item in data["transportation"]:
                                if "packaging" in item and "size" in item["packaging"]:
                                    size = item["packaging"]["size"]
                                    width = size.get("width", "")
                                    depth = size.get("depth", "")
                                    height = size.get("height", "")
                                    if not width or not depth or not height:
                                        print(f"Файл: {file_path} — отсутствуют или пустые размеры в size")
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

# Укажите путь к папке
folder_path = r"C:\Users\UTFC\Documents\Downloads\to\products"
check_json_files(folder_path)
