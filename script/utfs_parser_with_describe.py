import requests
from bs4 import BeautifulSoup
import os
import csv
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

def get_product_description(product_html):
    if not product_html:
        return {}

    soup = BeautifulSoup(product_html, 'html.parser')
    description = {}

    # Ищем название товара
    title_tag = soup.find('h1')
    if title_tag:
        description['Название'] = title_tag.text.strip()

    # Ищем блоки с характеристиками
    h5_tags = soup.select('div.h5')
    for h5 in h5_tags:
        key = h5.text.strip()
        next_div = h5.find_next_sibling('div', class_='simple-article size-2')
        if next_div:
            value = next_div.text.strip()
            description[key] = value

    return description

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
    for link in subcategory_links:
        print(f"Обрабатываю подкатегорию: {link}")
        subcategory_html = get_page_with_selenium(link)
        time.sleep(2)
        if subcategory_html:
            product_links = get_product_links(subcategory_html)
            for product_link in product_links:
                print(f"Обрабатываю товар: {product_link}")
                product_html = get_page_with_selenium(product_link)
                time.sleep(2)
                if product_html:
                    description = get_product_description(product_html)
                    if description:
                        all_products.append(description)

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
                        product_html = get_page_with_selenium(product_link)
                        time.sleep(2)
                        if product_html:
                            description = get_product_description(product_html)
                            if description:
                                all_products.append(description)

    print(f"Собрано описаний: {len(all_products)}")

    with open('utfc_products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=all_products[0].keys() if all_products else [])
        writer.writeheader()
        writer.writerows(all_products)

    print(f"Сохранено {len(all_products)} описаний в файл utfc_products.csv")

if __name__ == "__main__":
    main()
