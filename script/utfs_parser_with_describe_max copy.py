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

        # Получаем основные данные
        title = driver.title

        breadcrumbs = soup.find('div', class_='breadcrumbs')
        base_name = np.nan
        if breadcrumbs:
            last_span = breadcrumbs.find_all('span')[-1]
            if last_span.text.strip():
                base_name = last_span.text.strip()

        full_describe_tag = soup.find('div', class_='simple-article size-3 col-xs-b30')
        full_describe = np.nan
        if full_describe_tag:
            full_describe = full_describe_tag.get_text(strip=True)

        category_tag = soup.find('div', class_='simple-article size-3 grey')
        category = category_tag.text.strip() if category_tag else np.nan

        article_number = np.nan
        article_tag = soup.find('div', class_='simple-article size-3 col-xs-b5')
        if article_tag and 'Артикул:' in article_tag.text:
            article_span = article_tag.find('span', class_='grey')
            article_number = article_span.text.strip() if article_span else np.nan

        # Получаем все возможные варианты отделки
        finish_types = {}
        finish_select = soup.select_one('[data-name-prop="type_finish"] select[name="somename"]')
        if finish_select:
            for option in finish_select.find_all('option'):
                if option.get('value') and not option.get('disabled'):
                    finish_types[option.get('title')] = option.get('data-onevalue')

        # Получаем все возможные варианты цвета
        finish_colors = {}
        color_containers = soup.select('[data-name-prop="color_finish"] li.product-item-scu-item-color-container:not(.notallowed)')
        for color in color_containers:
            color_name = color.get('title')
            color_value = color.get('data-onevalue')
            if color_name and color_value:
                finish_colors[color_value] = color_name

        product_data_list = []

        # Если нет разновидностей, собираем данные как для одного товара
        if not finish_types or not finish_colors:
            product_data = {
                "title": title,
                "base_name": base_name,
                "finish_type": np.nan,
                "color": np.nan,
                "variant_name": base_name,
                "fullname": base_name,
                "category": category,
                "article_number": article_number,
                "full_describe": full_describe,
                "Link_arm": product_url
            }

            # Собираем изображения
            images = set()
            for img in soup.select('.swiper-slide[data-entity="image"] img'):
                src = img.get('data-src') or img.get('src')
                if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                    if not src.startswith('http'):
                        src = urllib.parse.urljoin(base_url, src)
                    images.add(src)
            for img in soup.select('.product-small-preview-entry img'):
                src = img.get('src')
                if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                    if not src.startswith('http'):
                        src = urllib.parse.urljoin(base_url, src)
                    images.add(src)
            product_data['images'] = '; '.join(images) if images else np.nan

            # Собираем описание
            description = {
                "Основание": np.nan,
                "Подлокотники": np.nan,
                "Газлифт": np.nan,
                "Механизм": np.nan,
                "Особенности": np.nan,
                "Ролики": np.nan
            }

            # Ищем все вкладки с описанием
            tab_entries = soup.find_all('div', class_='tab-entry')
            for tab in tab_entries:
                if 'display: block' in tab.get('style', ''):
                    for block in tab.select('div.col-sm-6'):
                        h5 = block.select_one('div.h5')
                        if h5:
                            key = h5.text.strip()
                            value = block.select_one('div.simple-article.size-2')
                            if value and key in description:
                                description[key] = value.text.strip()
            product_data.update(description)

            # Собираем размеры
            sizes = {}
            for tab in tab_entries:
                if 'Размер:' in tab.get_text():
                    for row in tab.select('div.product-description-entry.row.nopadding'):
                        name = row.select_one('div.col-xs-6 div.h6')
                        value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                        if name and value:
                            sizes[name.text.strip()] = value.text.strip()
            product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else np.nan

            # Собираем размеры упаковки
            package_sizes = {}
            for tab in tab_entries:
                if 'Размер упаковки:' in tab.get_text():
                    for row in tab.select('div.product-description-entry.row.nopadding'):
                        name = row.select_one('div.col-xs-6 div.h6')
                        value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                        if name and value:
                            package_sizes[name.text.strip()] = value.text.strip()
            product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else np.nan

            # Собираем дополнительные материалы
            additional = []
            for tab in tab_entries:
                if 'Дополнительно' in tab.get_text():
                    for link in tab.select('a[href]'):
                        additional.append({
                            'Type': link.text.strip(),
                            'Link': urllib.parse.urljoin(base_url, link.get('href'))
                        })
            product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else np.nan

            product_data_list.append(product_data)

        else:
            # Если есть разновидности, собираем данные для каждой комбинации
            for finish_type_name, finish_type_value in finish_types.items():
                for color_value, color_name in finish_colors.items():
                    product_data = {
                        "title": title,
                        "base_name": base_name,
                        "finish_type": finish_type_name,
                        "color": color_name,
                        "variant_name": f"{base_name} ({finish_type_name}, {color_name})",
                        "fullname": f"{base_name} ({finish_type_name}, {color_name})",
                        "category": category,
                        "article_number": article_number,
                        "full_describe": full_describe,
                        "Link_arm": product_url
                    }

                    # Собираем изображения для текущего варианта
                    images = set()
                    for img in soup.select(f'[data-onevalue="{color_value}"] .swiper-slide img'):
                        src = img.get('data-src') or img.get('src')
                        if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                            if not src.startswith('http'):
                                src = urllib.parse.urljoin(base_url, src)
                            images.add(src)
                    for img in soup.select(f'[data-onevalue="{color_value}"] .product-small-preview-entry img'):
                        src = img.get('src')
                        if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                            if not src.startswith('http'):
                                src = urllib.parse.urljoin(base_url, src)
                            images.add(src)
                    # Если нет изображений для конкретного цвета, добавляем все изображения со страницы
                    if not images:
                        for img in soup.select('.swiper-slide[data-entity="image"] img'):
                            src = img.get('data-src') or img.get('src')
                            if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                                if not src.startswith('http'):
                                    src = urllib.parse.urljoin(base_url, src)
                                images.add(src)
                        for img in soup.select('.product-small-preview-entry img'):
                            src = img.get('src')
                            if src and (src.endswith('.webp') or src.endswith('.jpg') or src.endswith('.png')):
                                if not src.startswith('http'):
                                    src = urllib.parse.urljoin(base_url, src)
                                images.add(src)
                    product_data['images'] = '; '.join(images) if images else np.nan

                    # Собираем описание для текущего варианта
                    description = {
                        "Основание": np.nan,
                        "Подлокотники": np.nan,
                        "Газлифт": np.nan,
                        "Механизм": np.nan,
                        "Особенности": np.nan,
                        "Ролики": np.nan
                    }

                    # Ищем все вкладки с описанием
                    tab_entries = soup.find_all('div', class_='tab-entry')
                    for tab in tab_entries:
                        if 'display: block' in tab.get('style', ''):
                            for block in tab.select('div.col-sm-6'):
                                h5 = block.select_one('div.h5')
                                if h5:
                                    key = h5.text.strip()
                                    value = block.select_one('div.simple-article.size-2')
                                    if value and key in description:
                                        description[key] = value.text.strip()
                    product_data.update(description)

                    # Собираем размеры для текущего варианта
                    sizes = {}
                    for tab in tab_entries:
                        if 'Размер:' in tab.get_text():
                            for row in tab.select('div.product-description-entry.row.nopadding'):
                                name = row.select_one('div.col-xs-6 div.h6')
                                value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                                if name and value:
                                    sizes[name.text.strip()] = value.text.strip()
                    product_data['sizes'] = json.dumps(sizes, ensure_ascii=False) if sizes else np.nan

                    # Собираем размеры упаковки для текущего варианта
                    package_sizes = {}
                    for tab in tab_entries:
                        if 'Размер упаковки:' in tab.get_text():
                            for row in tab.select('div.product-description-entry.row.nopadding'):
                                name = row.select_one('div.col-xs-6 div.h6')
                                value = row.select_one('div.col-xs-6.text-right div.simple-article.size-2')
                                if name and value:
                                    package_sizes[name.text.strip()] = value.text.strip()
                    product_data['package_sizes'] = json.dumps(package_sizes, ensure_ascii=False) if package_sizes else np.nan

                    # Собираем дополнительные материалы для текущего варианта
                    additional = []
                    for tab in tab_entries:
                        if 'Дополнительно' in tab.get_text():
                            for link in tab.select('a[href]'):
                                additional.append({
                                    'Type': link.text.strip(),
                                    'Link': urllib.parse.urljoin(base_url, link.get('href'))
                                })
                    product_data['Specifications'] = json.dumps(additional, ensure_ascii=False) if additional else np.nan

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
        "title", "base_name", "finish_type", "color", "variant_name", "fullname", "category", "article_number",
        "full_describe", "images", "Основание", "Подлокотники", "Газлифт", "Механизм", "Особенности", "Ролики",
        "sizes", "package_sizes", "Specifications", "Link_arm"
    ]

    # Для отладки: ограничиваем количество подкатегорий
    subcategory_links = subcategory_links[:2]

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
