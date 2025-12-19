import os
import re
from PyPDF2 import PdfReader

def extract_year_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            if len(reader.pages) == 0:
                return None
            first_page_text = reader.pages[0].extract_text()
            # Ищем строку вида "Ярославль, 2025" или "Ярославль,2025" и т.п.
            match = re.search(r'Ярославль,\s*(\d{4})', first_page_text)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Ошибка при обработке {pdf_path}: {e}")
    return None

def process_folder(folder_path):
    year_dict = {}
    no_year_list = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                year = extract_year_from_pdf(pdf_path)
                if year:
                    if year not in year_dict:
                        year_dict[year] = []
                    year_dict[year].append(pdf_path)
                else:
                    no_year_list.append(pdf_path)

    return year_dict, no_year_list

def save_results(year_dict, no_year_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for year, files in sorted(year_dict.items(), key=lambda x: int(x[0]), reverse=True):
            f.write(f"\n=== Файлы с годом {year} ===\n")
            for file in files:
                f.write(f"{os.path.basename(file)}\n")
        f.write("\n=== Файлы без указания года ===\n")
        for file in no_year_list:
            f.write(f"{os.path.basename(file)}\n")

# Основной код
folder_path = r"C:\Users\UTFC\Documents\Downloads\catalog_to\extracted_images"
output_file = "ТО.txt"

year_dict, no_year_list = process_folder(folder_path)
save_results(year_dict, no_year_list, output_file)

print(f"Готово! Результаты сохранены в {output_file}")
