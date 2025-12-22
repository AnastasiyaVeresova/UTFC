import os
import json

def process_file(file_path):
    """Обрабатывает один файл: заменяет ../ на пустую строку в полях images."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if "images" in data:
            for image_set in data["images"]:
                for key, value in image_set.items():
                    if isinstance(value, str) and value.startswith("../"):
                        image_set[key] = value[3:]

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Файл {file_path} успешно обработан.")

    except Exception as e:
        print(f"Ошибка при обработке файла {file_path}: {e}")

def find_and_process_files(root_dir):
    """Рекурсивно ищет и обрабатывает все файлы .json и .kjr в папке и её подпапках."""
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('.json', '.kjr')):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    root_directory = r"C:\Users\UTFC\Documents\Downloads\to\products"
    find_and_process_files(root_directory)
    print("Обработка завершена.")
