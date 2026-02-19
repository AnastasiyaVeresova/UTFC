import os
import json

def find_seat_width_305(root_dir):
    found_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Проверяем seat_width в dimensions_details
                        if 'dimensions_details' in data:
                            for dim in data['dimensions_details']:
                                if 'seat_width' in dim:
                                    seat_width = dim['seat_width']
                                    if isinstance(seat_width, dict):
                                        if 'min' in seat_width and seat_width['min'] == 305:
                                            found_files.append({
                                                'file': file_path,
                                                'field': 'seat_width.min',
                                                'value': 305
                                            })
                                        if 'max' in seat_width and seat_width['max'] == 305:
                                            found_files.append({
                                                'file': file_path,
                                                'field': 'seat_width.max',
                                                'value': 305
                                            })
                                    elif seat_width == 305:
                                        found_files.append({
                                            'file': file_path,
                                            'field': 'seat_width',
                                            'value': 305
                                        })
                        # Проверяем seat_width в dimensions
                        if 'dimensions' in data:
                            for dim in data['dimensions']:
                                if 'seat_width' in dim and dim['seat_width'] == 305:
                                    found_files.append({
                                        'file': file_path,
                                        'field': 'seat_width',
                                        'value': 305
                                    })
                except Exception as e:
                    print(f"Ошибка при чтении файла {file_path}: {e}")

    # Выводим результаты
    if found_files:
        print("Найдены файлы с seat_width = 305:")
        print("=" * 80)
        for item in found_files:
            print(f"Файл: {item['file']}")
            print(f"  Поле: {item['field']} = {item['value']}")
            print("-" * 80)
        print(f"Всего найдено: {len(found_files)} файлов")
    else:
        print("Файлы с seat_width = 305 не найдены.")

# Запуск поиска
find_seat_width_305(r'C:\Users\UTFC\Documents\Downloads\to\products')
