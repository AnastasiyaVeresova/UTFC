import os
import json

def update_namefile_in_json(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # Получаем имя файла без расширения
                    new_name = os.path.splitext(file)[0]

                    # Обновляем все вхождения "namefile" на новое имя
                    if "namefile" in data:
                        data["namefile"] = [new_name]

                    # Сохраняем изменения обратно в файл
                    with open(file_path, 'w', encoding='utf-8', ensure_ascii=False) as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)

                    print(f"Обновлён файл: {file_path} → namefile: {new_name}")

                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

# Укажите путь к папке
folder_path = r"C:\Users\UTFC\Documents\Downloads\to\products"
update_namefile_in_json(folder_path)
