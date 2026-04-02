# import requests
# from bs4 import BeautifulSoup
# import csv
# import urllib.parse
# import json
# import numpy as np
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# base_url = "https://utfc.ru"

# def get_page_with_selenium(url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     try:
#         driver.get(url)
#         time.sleep(3)
#         return driver.page_source
#     except Exception as e:
#         print(f"Ошибка при загрузке {url}: {e}")
#         return None
#     finally:
#         driver.quit()

# def get_subcategory_links(main_page_html):
#     if not main_page_html:
#         return []

#     soup = BeautifulSoup(main_page_html, 'html.parser')
#     links = set()

#     for a in soup.select('a[href*="/catalog/"]'):
#         href = a.get('href')
#         if href and not href.endswith('/catalog/') and not href.startswith('http'):
#             links.add(base_url + href)

#     return list(links)

# def get_product_links(subcategory_html):
#     if not subcategory_html:
#         return []

#     soup = BeautifulSoup(subcategory_html, 'html.parser')
#     product_links = set()

#     for a in soup.select('a[href*="/catalog/"][title]'):
#         href = a.get('href')
#         if href and not href.startswith('http'):
#             product_links.add(base_url + href)

#     return list(product_links)

# def get_product_data_with_selenium(product_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     try:
#         driver.get(product_url)
#         time.sleep(3)

#         # Получаем HTML страницы
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'html.parser')

#         # Получаем основные данные
#         title = driver.title

#         breadcrumbs = soup.find('div', class_='breadcrumbs')
#         base_name = np.nan
#         if breadcrumbs:
#             last_span = breadcrumbs.find_all('span')[-1]
#             if last_span.text.strip():
#                 base_name = last_span.text.strip()

#         full_describe_tag = soup.find('div', class_='simple-article size-3 col-xs-b30')
#         full_describe = np.nan
#         if full_describe_tag:
#             full_describe = full_describe_tag.get_text(strip=True)

#         category_tag = soup.find('div', class_='simple-article size-3 grey')
#         category = category_tag.text.strip() if category_tag else np.nan

#         article_number = np.nan
#         article_tag = soup.find('div', class_='simple-article size-3 col-xs-b5')
#         if article_tag and 'Артикул:' in article_tag.text:
#             article_span = article_tag.find('span', class_='grey')
#             article_number = article_span.text.strip() if article_span else np.nan

#         # Получаем все возможные варианты отделки
#         finish_types = {}
#         finish_select = soup.select_one('[data-name-prop="type_finish"] select[name="somename"]')
#         if finish_select:
#             for option in finish_select.find_all('option'):
#                 if option.get('value') and not option.get('disabled'):
#                     finish_types[option.get('title')] = option.get('data-onevalue')

#         # Получаем все возможные варианты цвета
#         finish_colors = {}
#         color_containers = soup.select('[data-name-prop="color_finish"] li.product-item-scu-item-color-container:not(.notallowed)')
#         for color in color_containers:
#             color_name = color.get('title')
#             color_value = color.get('data-onevalue')
#             if color_name and color_value:
#                 finish_colors[color_value] = color_name

#         product_data_list = []

#         # Собираем все изображения со страницы
#         all_images = set()
#         for img in soup.select('img'):
#             src = img.get('src') or img.get('data-src')
#             if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
#                 if not src.startswith('http'):
#                     src = urllib.parse.urljoin(base_url, src)
#                 all_images.add(src)

#         # Собираем описания из всех блоков на странице
#         descriptions = {
#             "Основание": np.nan,
#             "Подлокотники": np.nan,
#             "Газлифт": np.nan,
#             "Механизм": np.nan,
#             "Особенности": np.nan,
#             "Ролики": np.nan
#         }

#         for block in soup.select('div.col-sm-6'):
#             h5 = block.select_one('div.h5')
#             if h5:
#                 key = h5.text.strip()
#                 value = block.select_one('div.simple-article.size-2')
#                 if value and key in descriptions:
#                     descriptions[key] = value.text.strip()

#         # Собираем размеры
#         sizes = {}
#         for row in soup.select('div.product-description-entry.row.nopadding'):
#             name = row.select_one('div.col-xs-6 div.h6')
#             value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
#             if name and value:
#                 sizes[name.text.strip()] = value.text.strip()

#         # Собираем размеры упаковки
#         package_sizes = {}
#         for row in soup.select('div.product-description-entry.row.nopadding'):
#             name = row.select_one('div.col-xs-6 div.h6')
#             value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
#             if name and value and 'упаковки' in name.text.strip().lower():
#                 package_sizes[name.text.strip()] = value.text.strip()

#         # Собираем дополнительные материалы
#         additional = []
#         for link in soup.select('a[href*=".pdf"], a[href*=".doc"], a[href*=".docx"]'):
#             additional.append({
#                 'Type': link.text.strip(),
#                 'Link': urllib.parse.urljoin(base_url, link.get('href'))
#             })

#         # Если нет разновидностей, собираем данные как для одного товара
#         if not finish_types or not finish_colors:
#             product_data = {
#                 "title": title,
#                 "base_name": base_name,
#                 "finish_type": np.nan,
#                 "color": np.nan,
#                 "variant_name": base_name,
#                 "fullname": base_name,
#                 "category": category,
#                 "article_number": article_number,
#                 "full_describe": full_describe,
#                 "images": '; '.join(all_images) if all_images else np.nan,
#                 "Link_arm": product_url
#             }
#             product_data.update(descriptions)
#             product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else np.nan
#             product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else np.nan
#             product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else np.nan

#             product_data_list.append(product_data)

#         else:
#             # Если есть разновидности, собираем данные для каждой комбинации
#             for finish_type_name, finish_type_value in finish_types.items():
#                 for color_value, color_name in finish_colors.items():
#                     product_data = {
#                         "title": title,
#                         "base_name": base_name,
#                         "finish_type": finish_type_name,
#                         "color": color_name,
#                         "variant_name": f"{base_name} ({finish_type_name}, {color_name})",
#                         "fullname": f"{base_name} ({finish_type_name}, {color_name})",
#                         "category": category,
#                         "article_number": article_number,
#                         "full_describe": full_describe,
#                         "images": '; '.join(all_images) if all_images else np.nan,
#                         "Link_arm": product_url
#                     }
#                     product_data.update(descriptions)
#                     product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else np.nan
#                     product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else np.nan
#                     product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else np.nan

#                     product_data_list.append(product_data)

#         return product_data_list

#     except Exception as e:
#         print(f"Ошибка при обработке {product_url}: {e}")
#         return []
#     finally:
#         driver.quit()

# def get_pagination_links(subcategory_html, subcategory_url):
#     if not subcategory_html:
#         return []

#     soup = BeautifulSoup(subcategory_html, 'html.parser')
#     pagination_links = set()

#     for a in soup.select('div.pagination-wrapper a.pagination'):
#         href = a.get('href')
#         if href and not href.startswith('javascript:'):
#             pagination_links.add(base_url + href if href.startswith('/') else href)

#     return list(pagination_links)

# def main():
#     main_page_html = get_page_with_selenium(f"{base_url}/catalog/")
#     if not main_page_html:
#         print("Не удалось загрузить главную страницу каталога.")
#         return

#     subcategory_links = get_subcategory_links(main_page_html)
#     print(f"Найдено подкатегорий: {len(subcategory_links)}")

#     all_products = []
#     fieldnames = [
#         "title", "base_name", "finish_type", "color", "variant_name", "fullname", "category", "article_number",
#         "full_describe", "images", "Основание", "Подлокотники", "Газлифт", "Механизм", "Особенности", "Ролики",
#         "sizes", "package_sizes", "Specifications", "Link_arm"
#     ]

#     # Для отладки: ограничиваем количество подкатегорий
#     subcategory_links = subcategory_links[:2]

#     for link in subcategory_links:
#         print(f"Обрабатываю подкатегорию: {link}")
#         subcategory_html = get_page_with_selenium(link)
#         time.sleep(2)
#         if subcategory_html:
#             product_links = get_product_links(subcategory_html)
#             for product_link in product_links:
#                 print(f"Обрабатываю товар: {product_link}")
#                 product_data_list = get_product_data_with_selenium(product_link)
#                 if product_data_list:
#                     all_products.extend(product_data_list)

#             # Обрабатываем пагинацию
#             pagination_links = get_pagination_links(subcategory_html, link)
#             for page_link in pagination_links:
#                 print(f"Обрабатываю страницу пагинации: {page_link}")
#                 page_html = get_page_with_selenium(page_link)
#                 time.sleep(2)
#                 if page_html:
#                     product_links = get_product_links(page_html)
#                     for product_link in product_links:
#                         print(f"Обрабатываю товар: {product_link}")
#                         product_data_list = get_product_data_with_selenium(product_link)
#                         if product_data_list:
#                             all_products.extend(product_data_list)

#     print(f"Собрано товаров: {len(all_products)}")

#     with open('utfc_products_all_variants_full.csv', 'w', newline='', encoding='utf-8') as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(all_products)

#     print(f"Сохранено {len(all_products)} товаров в файл utfc_products_all_variants_full.csv")

# if __name__ == "__main__":
#     main()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


import requests
from bs4 import BeautifulSoup
import csv
import urllib.parse
import json
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

base_url = "https://utfc.ru"

def get_page_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get(url)
        time.sleep(3)
        return driver.page_source
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None
    finally:
        driver.quit()

def get_subcategory_links(main_page_html):
    if not main_page_html:
        return []

    soup = BeautifulSoup(main_page_html, 'html.parser')
    links = set()

    for a in soup.select('a[href*="/catalog/"]'):
        href = a.get('href')
        if href and not href.endswith('/catalog/') and not href.startswith('http'):
            links.add(base_url + href)

    return list(links)

def get_product_links(subcategory_html):
    if not subcategory_html:
        return []

    soup = BeautifulSoup(subcategory_html, 'html.parser')
    product_links = set()

    for a in soup.select('a[href*="/catalog/"][title]'):
        href = a.get('href')
        if href and not href.startswith('http'):
            product_links.add(base_url + href)

    return list(product_links)

# def get_product_data_with_selenium(product_url):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')
#     options.add_argument('--disable-blink-features=AutomationControlled')
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     try:
#         driver.get(product_url)
#         time.sleep(3)

#         # Получаем HTML страницы
#         page_source = driver.page_source
#         soup = BeautifulSoup(page_source, 'html.parser')

#         # Получаем основные данные
#         title = driver.title

#         breadcrumbs = soup.find('div', class_='breadcrumbs')
#         base_name = np.nan
#         if breadcrumbs:
#             last_span = breadcrumbs.find_all('span')[-1]
#             if last_span.text.strip():
#                 base_name = last_span.text.strip()

#         full_describe_tag = soup.find('div', class_='simple-article size-3 col-xs-b30')
#         full_describe = np.nan
#         if full_describe_tag:
#             full_describe = full_describe_tag.get_text(strip=True)

#         category_tag = soup.find('div', class_='simple-article size-3 grey')
#         category = category_tag.text.strip() if category_tag else np.nan

#         article_number = np.nan
#         article_tag = soup.find('div', class_='simple-article size-3 col-xs-b5')
#         if article_tag and 'Артикул:' in article_tag.text:
#             article_span = article_tag.find('span', class_='grey')
#             article_number = article_span.text.strip() if article_span else np.nan

#         # Получаем все возможные варианты отделки
#         finish_types = {}
#         finish_select = soup.select_one('[data-name-prop="type_finish"] select[name="somename"]')
#         if finish_select:
#             for option in finish_select.find_all('option'):
#                 if option.get('value') and not option.get('disabled'):
#                     finish_types[option.get('title')] = option.get('data-onevalue')


#         # Получаем все возможные варианты цвета
#         finish_colors = {}
#         color_containers = soup.select('[data-name-prop="color_finish"] li.product-item-scu-item-color-container:not(.notallowed)')
#         for color in color_containers:
#             color_name = color.get('title')
#             color_value = color.get('data-onevalue')
#             if color_name and color_value:
#                 finish_colors[color_value] = color_name


#                                           # Получаем все возможные варианты отделки сиденья
#         finish_types_seat = {}
#         finish_select_seat = soup.select_one('[data-name-prop="type_finish_seat"] select[name="somename"]')
#         if finish_select_seat:
#             for option in finish_select_seat.find_all('option'):
#                 if option.get('value') and not option.get('disabled'):
#                     finish_types_seat[option.get('title')] = option.get('data-onevalue')

                    
#         # Получаем все возможные варианты цвета сиденья
#         finish_colors_seat = {}
#         color_containers = soup.select('[data-name-prop="color_finish_seat"] li.product-item-scu-item-color-container:not(.notallowed)')
#         for color_seat in color_containers:
#             color_name = color_seat.get('title')
#             color_value = color_seat.get('data-onevalue')
#             if color_name and color_value:
#                 finish_colors_seat[color_value] = color_name


#         product_data_list = []

#         # Собираем все изображения со страницы
#         all_images = set()
#         for img in soup.select('img'):
#             src = img.get('src') or img.get('data-src')
#             if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
#                 if not src.startswith('http'):
#                     src = urllib.parse.urljoin(base_url, src)
#                 all_images.add(src)

#         # Собираем описания из всех вкладок
#         descriptions = {
#             "Основание": None,
#             "Подлокотники": None,
#             "Газлифт": None,
#             "Механизм": None,
#             "Особенности": None,
#             "Ролики": None
#         }

#         # Ищем все вкладки с описанием
#         tab_entries = soup.find_all('div', class_='tab-entry')
#         for tab in tab_entries:
#             for block in tab.select('div.col-sm-6'):
#                 h5 = block.select_one('div.h5')
#                 if h5:
#                     key = h5.text.strip()
#                     value = block.select_one('div.simple-article.size-2')
#                     if value and key in descriptions:
#                         descriptions[key] = value.text.strip()

#         # Собираем размеры
#         sizes = {}
#         for tab in tab_entries:
#             for row in tab.select('div.product-description-entry.row.nopadding'):
#                 name = row.select_one('div.col-xs-6 div.h6')
#                 value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
#                 if name and value:
#                     sizes[name.text.strip()] = value.text.strip()

#         # Собираем размеры упаковки
#         package_sizes = {}
#         for tab in tab_entries:
#             for row in tab.select('div.product-description-entry.row.nopadding'):
#                 name = row.select_one('div.col-xs-6 div.h6')
#                 value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
#                 if name and value and 'упаковки' in name.text.strip().lower():
#                     package_sizes[name.text.strip()] = value.text.strip()

#         # Собираем дополнительные материалы
#         additional = []
#         for tab in tab_entries:
#             for link in tab.select('a[href*=".pdf"], a[href*=".doc"], a[href*=".docx"]'):
#                 additional.append({
#                     'Type': link.text.strip(),
#                     'Link': urllib.parse.urljoin(base_url, link.get('href'))
#                 })

#         # Если нет разновидностей, собираем данные как для одного товара
#         if not finish_types or not finish_colors:
#             product_data = {
#                 "title": title,
#                 "base_name": base_name,
#                 "finish_type": None,
#                 "color": None,
#                 "finish_type_seat": None,
#                 "color_seat": None,
#                 "variant_name": base_name,
#                 "fullname": base_name,
#                 "category": category,
#                 "article_number": article_number,
#                 "full_describe": full_describe,
#                 "images": '; '.join(all_images) if all_images else None,
#                 "Link_arm": product_url
#             }
#             product_data.update(descriptions)
#             product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else None
#             product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else None
#             product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else None

#             product_data_list.append(product_data)

#         else:
#             # Если есть разновидности, собираем данные для каждой комбинации
#             for finish_type_name, finish_type_value in finish_types.items():
#                 for color_value, color_name in finish_colors.items():
#                     product_data = {
#                         "title": title,
#                         "base_name": base_name,
#                         "finish_type": finish_type_name,
#                         "color": color_name,
#                         "variant_name": f"{base_name} ({finish_type_name}, {color_name})",
#                         "fullname": f"{base_name} ({finish_type_name}, {color_name})",
#                         "category": category,
#                         "article_number": article_number,
#                         "full_describe": full_describe,
#                         "images": '; '.join(all_images) if all_images else None,
#                         "Link_arm": product_url
#                     }
#                     product_data.update(descriptions)
#                     product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else None
#                     product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else None
#                     product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else None

#                     product_data_list.append(product_data)

#         return product_data_list

#     except Exception as e:
#         print(f"Ошибка при обработке {product_url}: {e}")
#         return []
#     finally:
#         driver.quit()


def get_product_data_with_selenium(product_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get(product_url)
        time.sleep(3)

        # Получаем HTML страницы
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # --- Основные данные ---
        title = driver.title

        breadcrumbs = soup.find('div', class_='breadcrumbs')
        base_name = None
        if breadcrumbs:
            last_span = breadcrumbs.find_all('span')[-1]
            if last_span.text.strip():
                base_name = last_span.text.strip()

        full_describe_tag = soup.find('div', class_='simple-article size-3 col-xs-b30')
        full_describe = None
        if full_describe_tag:
            full_describe = full_describe_tag.get_text(strip=True)

        category_tag = soup.find('div', class_='simple-article size-3 grey')
        category = category_tag.text.strip() if category_tag else None

        article_number = None
        article_tag = soup.find('div', class_='simple-article size-3 col-xs-b5')
        if article_tag and 'Артикул:' in article_tag.text:
            article_span = article_tag.find('span', class_='grey')
            article_number = article_span.text.strip() if article_span else None

        # --- Сбор вариантов отделки ---
        # 1. Основная отделка (тип + цвет)
        finish_types = {}
        finish_select = soup.select_one('[data-name-prop="type_finish"] select[name="somename"]')
        if finish_select:
            for option in finish_select.find_all('option'):
                if option.get('value') and not option.get('disabled'):
                    finish_types[option.get('title')] = option.get('data-onevalue')

        finish_colors = {}
        color_containers = soup.select('[data-name-prop="color_finish"] li.product-item-scu-item-color-container:not(.notallowed)')
        for color in color_containers:
            color_name = color.get('title')
            color_value = color.get('data-onevalue')
            if color_name and color_value:
                finish_colors[color_value] = color_name

        # 2. Отделка сиденья (тип + цвет)
        finish_types_seat = {}
        finish_select_seat = soup.select_one('[data-name-prop="type_finish_seat"] select[name="somename"]')
        if finish_select_seat:
            for option in finish_select_seat.find_all('option'):
                if option.get('value') and not option.get('disabled'):
                    finish_types_seat[option.get('title')] = option.get('data-onevalue')

        finish_colors_seat = {}
        color_containers_seat = soup.select('[data-name-prop="color_finish_seat"] li.product-item-scu-item-color-container:not(.notallowed)')
        for color_seat in color_containers_seat:
            color_name = color_seat.get('title')
            color_value = color_seat.get('data-onevalue')
            if color_name and color_value:
                finish_colors_seat[color_value] = color_name

        # --- Сбор изображений ---
        all_images = set()
        for img in soup.select('img'):
            src = img.get('src') or img.get('data-src')
            if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                if not src.startswith('http'):
                    src = urllib.parse.urljoin(base_url, src)
                all_images.add(src)

        # --- Сбор описаний ---
        descriptions = {
            "Основание": None,
            "Подлокотники": None,
            "Газлифт": None,
            "Механизм": None,
            "Особенности": None,
            "Ролики": None
        }

        tab_entries = soup.find_all('div', class_='tab-entry')
        for tab in tab_entries:
            for block in tab.select('div.col-sm-6'):
                h5 = block.select_one('div.h5')
                if h5:
                    key = h5.text.strip()
                    value = block.select_one('div.simple-article.size-2')
                    if value and key in descriptions:
                        descriptions[key] = value.text.strip()

        # --- Сбор размеров ---
        sizes = {}
        for tab in tab_entries:
            for row in tab.select('div.product-description-entry.row.nopadding'):
                name = row.select_one('div.col-xs-6 div.h6')
                value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                if name and value:
                    sizes[name.text.strip()] = value.text.strip()

        # --- Сбор размеров упаковки ---
        package_sizes = {}
        for tab in tab_entries:
            for row in tab.select('div.product-description-entry.row.nopadding'):
                name = row.select_one('div.col-xs-6 div.h6')
                value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                if name and value and 'упаковки' in name.text.strip().lower():
                    package_sizes[name.text.strip()] = value.text.strip()

        # --- Сбор дополнительных материалов ---
        additional = []
        for tab in tab_entries:
            for link in tab.select('a[href*=".pdf"], a[href*=".doc"], a[href*=".docx"]'):
                additional.append({
                    'Type': link.text.strip(),
                    'Link': urllib.parse.urljoin(base_url, link.get('href'))
                })

        # --- Генерация всех комбинаций ---
        product_data_list = []

        # Если нет вариантов отделки, добавляем один товар
        if not finish_types and not finish_colors and not finish_types_seat and not finish_colors_seat:
            product_data = {
       "title": title,
    "base_name": base_name,
    "finish_type": None,
        "color": None,
        "finish_type_seat": None,
        "color_seat": None,
    "variant_name": None,
    "fullname": variant_name,
    "category": category,
    "article_number": article_number,
    "full_describe": full_describe,
    "images": '; '.join(all_images) if all_images else None,
    "Link_arm": product_url,
    "Основание": descriptions.get("Основание"),
    "Подлокотники": descriptions.get("Подлокотники"),
    "Газлифт": descriptions.get("Газлифт"),
    "Механизм": descriptions.get("Механизм"),
    "Особенности": descriptions.get("Особенности"),
    "Ролики": descriptions.get("Ролики"),
    "sizes": json.dumps(sizes, ensure_ascii=False) if sizes else None,
    "package_sizes": json.dumps(package_sizes, ensure_ascii=False) if package_sizes else None,
    "Specifications": json.dumps(additional, ensure_ascii=False) if additional else None
}
            product_data.update(descriptions)
            product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else None
            product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else None
            product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else None
            product_data_list.append(product_data)

        else:
            # Если есть варианты отделки, генерируем все комбинации
            # 1. Основная отделка (тип + цвет)
            finish_combinations = []
            if finish_types and finish_colors:
                for finish_type_name, finish_type_value in finish_types.items():
                    for color_value, color_name in finish_colors.items():
                        finish_combinations.append({
                            "finish_type": finish_type_name,
                            "color": color_name
                        })

            # 2. Отделка сиденья (тип + цвет)
            finish_combinations_seat = []
            if finish_types_seat and finish_colors_seat:
                for finish_type_seat_name, finish_type_seat_value in finish_types_seat.items():
                    for color_seat_value, color_seat_name in finish_colors_seat.items():
                        finish_combinations_seat.append({
                            "finish_type_seat": finish_type_seat_name,
                            "color_seat": color_seat_name
                        })

            # 3. Генерация всех возможных комбинаций
            finish_combinations = []
            if finish_types and finish_colors:
                for finish_type_name, finish_type_value in finish_types.items():
                    for color_value, color_name in finish_colors.items():
                        finish_combinations.append({
                            "finish_type": finish_type_name,
                            "color": color_name
                        })
            else:
                finish_combinations = [{"finish_type": None, "color": None}]

            finish_combinations_seat = []
            if finish_types_seat and finish_colors_seat:
                for finish_type_seat_name, finish_type_seat_value in finish_types_seat.items():
                    for color_seat_value, color_seat_name in finish_colors_seat.items():
                        finish_combinations_seat.append({
                            "finish_type_seat": finish_type_seat_name,
                            "color_seat": color_seat_name
                        })
            else:
                finish_combinations_seat = [{"finish_type_seat": None, "color_seat": None}]

            for finish in finish_combinations:
                for finish_seat in finish_combinations_seat:
                    variant_name = base_name
                    if finish["finish_type"] or finish_seat["finish_type_seat"]:
                        variant_name = f"{base_name} ({finish['finish_type'] or ''}, {finish['color'] or ''}, {finish_seat['finish_type_seat'] or ''}, {finish_seat['color_seat'] or ''})".strip().replace("  ", " ").replace(" ,", ",")

                    product_data = {
                        "title": title,
                        "base_name": base_name,
                        "finish_type": finish["finish_type"],
                        "color": finish["color"],
                        "finish_type_seat": finish_seat["finish_type_seat"],
                        "color_seat": finish_seat["color_seat"],
                        "variant_name": variant_name,
                        "fullname": variant_name,
                        "category": category,
                        "article_number": article_number,
                        "full_describe": full_describe,
                        "images": '; '.join(all_images) if all_images else None,
                        "Link_arm": product_url
                    }
                    product_data.update(descriptions)
                    product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else None
                    product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else None
                    product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else None
                    product_data_list.append(product_data)

        return product_data_list

    except Exception as e:
        print(f"Ошибка при обработке {product_url}: {e}")
        return []
    finally:
        driver.quit()


def get_pagination_links(subcategory_html, subcategory_url):
    if not subcategory_html:
        return []

    soup = BeautifulSoup(subcategory_html, 'html.parser')
    pagination_links = set()

    for a in soup.select('div.pagination-wrapper a.pagination'):
        href = a.get('href')
        if href and not href.startswith('javascript:'):
            pagination_links.add(base_url + href if href.startswith('/') else href)

    return list(pagination_links)

def main():
    main_page_html = get_page_with_selenium(f"{base_url}/catalog/")
    if not main_page_html:
        print("Не удалось загрузить главную страницу каталога.")
        return

    subcategory_links = get_subcategory_links(main_page_html)
    print(f"Найдено подкатегорий: {len(subcategory_links)}")

    all_products = []
    fieldnames = [
  "title", "base_name", "finish_type", "color", "finish_type_seat", "color_seat",
    "variant_name", "fullname", "category", "article_number", "full_describe", "images",
    "Основание", "Подлокотники", "Газлифт", "Механизм", "Особенности", "Ролики",
    "sizes", "package_sizes", "Specifications", "Link_arm"
    ]

    # Для отладки: ограничиваем количество подкатегорий
    # subcategory_links = subcategory_links[:2]

    for link in subcategory_links:
        print(f"Обрабатываю подкатегорию: {link}")
        subcategory_html = get_page_with_selenium(link)
        time.sleep(2)
        if subcategory_html:
            product_links = get_product_links(subcategory_html)
            for product_link in product_links:
                print(f"Обрабатываю товар: {product_link}")
                product_data_list = get_product_data_with_selenium(product_link)
                if product_data_list:
                    all_products.extend(product_data_list)

            # Обрабатываем пагинацию
            pagination_links = get_pagination_links(subcategory_html, link)
            for page_link in pagination_links:
                print(f"Обрабатываю страницу пагинации: {page_link}")
                page_html = get_page_with_selenium(page_link)
                time.sleep(2)
                if page_html:
                    product_links = get_product_links(page_html)
                    for product_link in product_links:
                        print(f"Обрабатываю товар: {product_link}")
                        product_data_list = get_product_data_with_selenium(product_link)
                        if product_data_list:
                            all_products.extend(product_data_list)

    print(f"Собрано товаров: {len(all_products)}")

    with open('utfc_products_all_variants_full.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_products)

    print(f"Сохранено {len(all_products)} товаров в файл utfc_products_all_variants_full.csv")

if __name__ == "__main__":
    main()
