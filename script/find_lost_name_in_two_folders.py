import os

def get_all_filenames(root_dir):
    """Собирает все имена файлов (без пути) из папки и её подпапок"""
    filenames = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            filenames.add(file)
    return filenames

# Пути к папкам
output_files2 = r'C:\Users\UTFC\Documents\Downloads\catalog_to\output_files2'
output_files = r'C:\Users\UTFC\Documents\Downloads\to\products'

# Получаем списки файлов
files2 = get_all_filenames(output_files2)
files1 = get_all_filenames(output_files)

# Ищем отсутствующие файлы
missing_files = files2 - files1

# Выводим результат
if missing_files:
    print("Файлы, которые есть в output_files2, но отсутствуют в output_files:")
    for file in sorted(missing_files):
        print(file)
else:
    print("Все файлы из output_files2 присутствуют в output_files.")
