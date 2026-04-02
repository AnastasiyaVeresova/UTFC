import os
import json

def find_json_files_with_seat_height(root_dir, target_value=370):
    matching_files = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if 'dimensions_details' in data and len(data['dimensions_details']) > 0:
                            seat_to_floor = data['dimensions_details'][0].get('seat_to_floor_height', {})
                            if seat_to_floor:
                                min_val = seat_to_floor.get('min')
                                max_val = seat_to_floor.get('max')
                                if min_val == target_value or (isinstance(min_val, str) and min_val.strip() == str(target_value)):
                                    matching_files.append((file_path, 'min', min_val))
                                if max_val == target_value or (isinstance(max_val, str) and max_val.strip() == str(target_value)):
                                    matching_files.append((file_path, 'max', max_val))
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")
    return matching_files

# Путь к папке с файлами
root_directory = r'C:\Users\UTFC\Documents\Downloads\to\products'

# Поиск файлов
results = find_json_files_with_seat_height(root_directory, 370)

# Вывод результатов
if results:
    print("Найдены файлы с seat_to_floor_height = 370:")
    for file_path, field, value in results:
        print(f"Файл: {file_path}")
        print(f"  Поле: {field}, Значение: {value}")
else:
    print("Файлы с seat_to_floor_height = 370 не найдены.")
