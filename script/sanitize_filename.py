import os
import json
import re

def sanitize_filename(filename):
    # Заменяем запрещённые символы на _
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def process_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Берём значение из "namefile"
    namefile = data["namefile"][0]
    # Очищаем имя файла
    new_unique_name = sanitize_filename(namefile)
    # Обновляем "unique_name"
    data["unique_name"] = new_unique_name

    # Сохраняем изменения обратно в файл
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Переименовываем файл
    dirname = os.path.dirname(filepath)
    new_filename = f"{new_unique_name}.json"
    new_filepath = os.path.join(dirname, new_filename)

    # Проверяем, что нового имени файла не существует
    if not os.path.exists(new_filepath):
        os.rename(filepath, new_filepath)
        print(f"Файл переименован: {new_filename}")
    else:
        print(f"Файл {new_filename} уже существует!")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                filepath = os.path.join(root, filename)
                process_json_file(filepath)

# Укажите путь к вашей директории
directory_path = r'C:\Users\UTFC\Documents\Downloads\to\products'
process_directory(directory_path)
