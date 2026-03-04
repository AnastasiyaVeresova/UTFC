import json
import os

def clear_json_values(data):
    # Очистка dimensions_details
    if 'dimensions_details' in data and len(data['dimensions_details']) > 0:
        for key in data['dimensions_details'][0]:
            if isinstance(data['dimensions_details'][0][key], dict):
                for sub_key in data['dimensions_details'][0][key]:
                    data['dimensions_details'][0][key][sub_key] = ""
            else:
                data['dimensions_details'][0][key] = ""

    # Очистка dimensions
    if 'dimensions' in data and len(data['dimensions']) > 0:
        for key in data['dimensions'][0]:
            data['dimensions'][0][key] = ""

    # Очистка guarantee
    if 'guarantee' in data and len(data['guarantee']) > 0:
        for key in data['guarantee'][0]:
            data['guarantee'][0][key] = ""

    # Очистка transportation
    if 'transportation' in data and len(data['transportation']) > 0:
        if 'packaging' in data['transportation'][0]:
            if 'size' in data['transportation'][0]['packaging']:
                for key in data['transportation'][0]['packaging']['size']:
                    data['transportation'][0]['packaging']['size'][key] = ""
            if 'box_size' in data['transportation'][0]['packaging']:
                data['transportation'][0]['packaging']['box_size'] = ""

    return data

def process_json_files(directory):
    # Рекурсивно обходим все файлы в директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    # Очистка значений
                    data = clear_json_values(data)

                    # Сохранение изменений
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                    print(f"Значения в файле {file_path} успешно очищены.")
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")

# Укажите путь к папке с JSON-файлами
json_directory = r'C:\Users\UTFC\Documents\Downloads\to\products'

# Запуск обработки
process_json_files(json_directory)

print("Обработка завершена.")
