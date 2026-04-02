# import os

# def rename_files_in_folder(root_folder):
#     for root, dirs, files in os.walk(root_folder):
#         for filename in files:
#             if '_k01' in filename:
#                 new_filename = filename.replace('_k01', '')
#                 old_path = os.path.join(root, filename)
#                 new_path = os.path.join(root, new_filename)
#                 os.rename(old_path, new_path)
#                 print(f'Переименован: {filename} → {new_filename}')

# folder_path = r'C:\Users\UTFC\Documents\БалтМебель\photos\chairs\Идра В дерево D5 К01\1080'

# rename_files_in_folder(folder_path)


import os

def rename_files_in_folder(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for filename in files:
            if 'astek_bp_cpt' in filename:
                # Добавляем '_pl' после 'astek_bp'
                new_filename = filename.replace('astek_bp_cpt', 'astek_bp_pl_cpt')
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(old_path, new_path)
                print(f'Переименован: {filename} → {new_filename}')

folder_path = r'C:\Users\UTFC\Documents\БалтМебель\photos\chairs\астек бп с39\1080'
rename_files_in_folder(folder_path)

