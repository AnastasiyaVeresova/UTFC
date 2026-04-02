import os

def get_file_list(root_dir):
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file)
    return file_list

# Укажите ваш путь
root_directory = r'C:\Users\UTFC\Documents\Downloads\to\products'

files = get_file_list(root_directory)

for file in files:
    print(file)
