import os
import json

def capitalize_only_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

def process_json_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'namefile' in data:
        old_name = data['namefile'][0]
        new_name = capitalize_only_first_letter(old_name)
        data['namefile'] = [new_name]

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON обработан: {filepath} → {old_name} → {new_name}")

def rename_file(filepath):
    dirname, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    new_name = capitalize_only_first_letter(name) + ext
    new_filepath = os.path.join(dirname, new_name)
    if new_name != filename:
        os.rename(filepath, new_filepath)
        print(f"Файл переименован: {filename} → {new_name}")
        return new_filepath
    return filepath

def walk_and_process(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.json'):
                filepath = os.path.join(root, file)
                new_filepath = rename_file(filepath)
                process_json_file(new_filepath)

if __name__ == "__main__":
    root_dir = r"C:\Users\UTFC\Documents\Downloads\to\products"
    walk_and_process(root_dir)
    print("Готово!")
