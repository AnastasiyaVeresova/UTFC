import os
import json

# Путь к папке с JSON-файлами
products_dir = r'C:\Users\UTFC\Documents\Downloads\to\products'

# Рекурсивный поиск всех JSON-файлов в папке и подпапках
json_files = []
for root, dirs, files in os.walk(products_dir):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# Обработка каждого JSON-файла
for json_file in json_files:
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем наличие ключа "typeofproduct" и переименовываем его в "addition", очищая значение
        if 'typeofproduct' in data:
            data['addition'] = ""
            del data['typeofproduct']

        # Сохраняем обновленный JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Ошибка при обработке файла {json_file}: {e}")

print("Переименование и очистка значений завершена.")
