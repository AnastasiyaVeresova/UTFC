import os
import json
import re
from collections import defaultdict

# Функция нормализации имени модели
def normalize_model_name(name):
    if not isinstance(name, str):
        return ""

    name = name.lower().strip()
    name = re.sub(r'\bстул\b|\bкресло\b|\butfc\b|\bчехол\b|\bдля\b|\bи\b|\bв\b|\bна\b|\bс\b|\bпод\b', '', name, flags=re.IGNORECASE)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()

    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'н\/п', 'нп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)

    words = name.split()
    words_sorted = sorted(words)
    normalized_name = ' '.join(words_sorted)

    return normalized_name

# 1. Чтение списка кресел из файла
def read_chairs_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        chairs = [line.strip() for line in f if line.strip()]
    return chairs

# 2. Рекурсивный поиск всех JSON-файлов в папке и подпапках
def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

# 3. Извлечение названий моделей из JSON-файлов
def extract_models_from_json(json_files):
    models_json = {}
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            model_name = data.get('namefile', [''])[0]
            if not model_name:
                model_name = data.get('name', [''])[0]
            if model_name:
                normalized = normalize_model_name(model_name)
                models_json[normalized] = {"file": json_file, "original": model_name}
        except Exception as e:
            print(f"Ошибка при чтении {json_file}: {e}")
    return models_json

# 4. Сравнение списков и вывод отсутствующих позиций
def compare_lists(chairs_list, models_json):
    missing_in_json = []
    missing_in_list = []

    # Нормализуем названия из списка
    normalized_chairs = [normalize_model_name(chair) for chair in chairs_list]

    # Ищем отсутствующие в JSON
    for chair in chairs_list:
        normalized = normalize_model_name(chair)
        if normalized not in models_json:
            missing_in_json.append({"Модель": chair, "Источник": "Список"})

    # Ищем отсутствующие в списке
    for normalized, info in models_json.items():
        if normalized not in normalized_chairs:
            missing_in_list.append({"Модель": info["original"], "Источник": "JSON"})

    return missing_in_json, missing_in_list

# 5. Сохранение результатов
def save_results(missing_in_json, missing_in_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        if missing_in_json:
            f.write("=== Модели, отсутствующие в JSON (но есть в списке) ===\n")
            for item in missing_in_json:
                f.write(f"{item['Модель']}\n")
            f.write("\n")
        else:
            f.write("=== Модели, отсутствующие в JSON (но есть в списке) ===\nНет отсутствующих моделей.\n\n")

        if missing_in_list:
            f.write("=== Модели, отсутствующие в списке (но есть в JSON) ===\n")
            for item in missing_in_list:
                f.write(f"{item['Модель']}\n")
            f.write("\n")
        else:
            f.write("=== Модели, отсутствующие в списке (но есть в JSON) ===\nНет отсутствующих моделей.\n\n")

# Основная функция
def main():
    # Пути к файлам
    chairs_list_path = r'C:\Users\UTFC\Documents\Downloads\to\script\utfc_chairs_list.txt'
    products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'
    output_file = 'missing_models.txt'

    # 1. Чтение списка кресел
    chairs_list = read_chairs_list(chairs_list_path)
    print(f"Прочитано {len(chairs_list)} моделей из списка.")

    # 2. Поиск JSON-файлов
    json_files = find_json_files(products_dir)
    print(f"Найдено {len(json_files)} JSON-файлов.")

    # 3. Извлечение моделей из JSON
    models_json = extract_models_from_json(json_files)
    print(f"Извлечено {len(models_json)} уникальных моделей из JSON.")

    # 4. Сравнение списков
    missing_in_json, missing_in_list = compare_lists(chairs_list, models_json)

    # 5. Сохранение результатов
    save_results(missing_in_json, missing_in_list, output_file)
    print(f"Результаты сохранены в {output_file}")

if __name__ == "__main__":
    main()
