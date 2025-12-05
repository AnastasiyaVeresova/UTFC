import os

def count_files_in_folders(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        if foldername != root_folder:  # Пропускаем корневую папку
            print(f"Папка: {foldername}")
            print(f"Количество файлов: {len(filenames)}\n")

def count_all_files(root_folder):
    total_files = 0
    for foldername, subfolders, filenames in os.walk(root_folder):
        total_files += len(filenames)
    print(f"Общее количество файлов: {total_files}")

# Укажите путь к вашей папке
path = r"C:\Users\UTFC\Documents\Downloads\to\products"
count_files_in_folders(path)
count_all_files(path)

