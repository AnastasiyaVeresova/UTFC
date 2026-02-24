import pandas as pd
import re

# Отображение колонок (как в вашем первом скрипте)
columns_mapping = {
    'Unnamed: 1': ('chair_height', 'min'),
    'Unnamed: 2': ('chair_height', 'max'),

    'Unnamed: 3': ('headrest_height', 'min'),
    'Unnamed: 4': ('headrest_height', 'max'),

    'Unnamed: 5': ('seat_to_floor_height', 'min'),
    'Unnamed: 6': ('seat_to_floor_height', 'max'),

    'Unnamed: 11': ('armrest_height_from_seat', 'min'),
    'Unnamed: 12': ('armrest_height_from_seat', 'max'),

    'Unnamed: 16': ('chair_depth', 'min'),
    'Unnamed: 17': ('chair_depth', 'angle'),

    'Unnamed: 18': ('seat_depth', 'min'),
    'Unnamed: 19': ('seat_depth', 'max'),

    'Unnamed: 21': ('backrest_height', 'max'),

    'Unnamed: 22': ('backrest_to_seat_height', 'min'),
     'Unnamed: 23': ('backrest_to_seat_height', 'max'),

    'Unnamed: 26': ('seat_width_with_armrests', 'min'),
    'Unnamed: 27': ('seat_width_with_armrests', 'max'),

    'Unnamed: 28': ('seat_width', 'max'),

    'Unnamed: 31': ('diameter_cross', 'max'),

    'Unnamed: 32': ('runners_width', 'max'),
    'Unnamed: 33': ('runners_depth', 'max'),

    'Unnamed: 34': ('recommended_load', 'max'),
    'Unnamed: 35': ('max_load', 'max'),    

    'Unnamed: 36': ('skeleton', None),
    'Unnamed: 37': ('minprodtorg', None),
    'Unnamed: 37': ('typeofproduct', None),

    'Unnamed: 38': ('netto', None),
    'Unnamed: 39': ('brutto', None),
    'Unnamed: 40': ('package_width', None),
    'Unnamed: 41': ('package_depth', None),
    'Unnamed: 42': ('package_height', None),
    'Unnamed: 43': ('volume', None)
}

def normalize_model_name(name):
    if not isinstance(name, str):
        return ""
    name = name.lower().strip()
    name = re.sub(r'\bстул\b|\bкресло\b|Кресло UTFC\b', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'с', 'c', name)
    name = re.sub(r'в\/п', 'вп', name)
    name = re.sub(r'н\/п', 'нп', name)
    name = re.sub(r'х\/дп', 'хдп', name)
    name = re.sub(r'м\/б', 'мб', name)
    name = re.sub(r'тг', 'tg', name)
    name = re.sub(r'пвм', 'пвм', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name

def compare_excel_files(old_file, new_file, sheet_name, output_file):
    import re

    old_df = pd.read_excel(old_file, sheet_name=sheet_name)
    new_df = pd.read_excel(new_file, sheet_name=sheet_name)

    # Извлекаем модели и нормализуем их названия
    old_models = old_df.iloc[3:, 0].dropna().tolist()
    new_models = new_df.iloc[3:, 0].dropna().tolist()

    old_models_normalized = {normalize_model_name(m): m for m in old_models}
    new_models_normalized = {normalize_model_name(m): m for m in new_models}

    # Находим общие модели
    common_models = set(old_models_normalized.keys()) & set(new_models_normalized.keys())

    # Собираем изменения
    changes_by_model = {}

    for model_norm in common_models:
        old_model = old_models_normalized[model_norm]
        new_model = new_models_normalized[model_norm]

        old_row = old_df[old_df.iloc[:, 0] == old_model].iloc[0]
        new_row = new_df[new_df.iloc[:, 0] == new_model].iloc[0]

        model_changes = []

        for col, (param, min_max) in columns_mapping.items():
            old_val = old_row[col]
            new_val = new_row[col]
            if pd.isna(old_val) and pd.isna(new_val):
                continue
            if str(old_val).strip() == '-' and str(new_val).strip() == '-':
                continue
            if str(old_val).strip() != str(new_val).strip():
                model_changes.append({
                    'Параметр': param,
                    'Старое значение': old_val,
                    'Новое значение': new_val
                })

        if model_changes:
            changes_by_model[old_model] = model_changes

    # Запись результатов
    with open(output_file, 'w', encoding='utf-8') as f:
        if changes_by_model:
            f.write("=== Изменения по моделям ===\n\n")
            for model, changes in changes_by_model.items():
                f.write(f"Модель: {model}\n")
                for change in changes:
                    f.write(f"  {change['Параметр']}: {change['Старое значение']} → {change['Новое значение']}\n")
                f.write("\n")
        else:
            f.write("Изменений не найдено.\n")

    print(f"Сравнение завершено. Результаты в {output_file}")

# Пример использования
old_file = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования) (2).xlsx'
new_file = r'C:\Users\UTFC\Documents\Downloads\Таблица с размерами (для внутреннего пользования).xlsx'
sheet_name = 'Размеры'
output_file = 'excel_differences.txt'

compare_excel_files(old_file, new_file, sheet_name, output_file)


