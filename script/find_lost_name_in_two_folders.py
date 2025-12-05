# import os

# def get_all_filenames(root_dir):
#     """Собирает все имена файлов (без пути) из папки и её подпапок"""
#     filenames = set()
#     for root, dirs, files in os.walk(root_dir):
#         for file in files:
#             filenames.add(file)
#     return filenames

# # Пути к папкам
# output_files2 = r'C:\Users\UTFC\Documents\Downloads\catalog_to\output_files2'
# output_files = r'C:\Users\UTFC\Documents\Downloads\to\products'

# # Получаем списки файлов
# files2 = get_all_filenames(output_files2)
# files1 = get_all_filenames(output_files)

# # Ищем отсутствующие файлы
# missing_files = files2 - files1

# # Выводим результат
# if missing_files:
#     print("Файлы, которые есть в output_files2, но отсутствуют в output_files:")
#     for file in sorted(missing_files):
#         print(file)
# else:
#     print("Все файлы из output_files2 присутствуют в output_files.")




import os
import json
import re

def normalize_name(name):
    """Нормализует имя: убирает игнорируемые слова, приводит к нижнему регистру, сохраняет дефисы"""
    ignored_words = {'utfc', 'кресло', 'стул', 'табурет', 'диван', 'пуф'}
    name = name.lower().strip()
    # Разбиваем по пробелам, запятым, подчёркиваниям, но сохраняем дефисы
    words = re.split(r'[\s\'_,]+', name)
    filtered_words = []
    for word in words:
        if word not in ignored_words:
            filtered_words.append(word)
    # Соединяем через пробел, но дефисы внутри слов сохраняются
    return ' '.join(filtered_words).strip()

def get_all_namefiles(root_dir):
    """Собирает все значения namefile из JSON-файлов в папке и её подпапках"""
    namefiles = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if 'namefile' in data and data['namefile']:
                        name = data['namefile'][0]
                        namefiles.add(normalize_name(name))
                except Exception as e:
                    print(f"Ошибка при чтении {file}: {e}")
    return namefiles

# Пути к папкам
output_files2 = r'C:\Users\UTFC\Documents\Downloads\catalog_to\output_files2'
output_files = r'C:\Users\UTFC\Documents\Downloads\to\products'

# Получаем множества нормализованных namefile
namefiles2 = get_all_namefiles(output_files2)
namefiles1 = get_all_namefiles(output_files)

# Ищем отсутствующие значения
missing_namefiles = namefiles2 - namefiles1

# Выводим результат
if missing_namefiles:
    print("Значения namefile, которые есть в output_files2, но отсутствуют в products (с учётом игнорируемых слов и сохранением дефисов):")
    for name in sorted(missing_namefiles):
        print(name)
else:
    print("Все значения namefile из output_files2 присутствуют в products (с учётом игнорируемых слов и сохранением дефисов).")
