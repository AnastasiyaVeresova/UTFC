import requests
from bs4 import BeautifulSoup
import os
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

def get_chair_names(subcategory_html):
    if not subcategory_html:
        return []

    soup = BeautifulSoup(subcategory_html, 'html.parser')
    names = []

    # Ищем все теги <a> с атрибутом title внутри div.h6.animate-to-green
    for a in soup.select('div.h6.animate-to-green a[title], a[href*="/catalog/"][title]'):
        if a.text.strip():
            name = a.text.strip()
            names.append(name)
            print(f"Найдено название: {name}")  # Отладочный вывод

    return names

def get_pagination_links(subcategory_html, subcategory_url):
    if not subcategory_html:
        return []

    soup = BeautifulSoup(subcategory_html, 'html.parser')
    pagination_links = set()

    # Ищем все ссылки на страницы пагинации
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

    all_chairs = []
    for link in subcategory_links:
        print(f"Обрабатываю подкатегорию: {link}")
        subcategory_html = get_page_with_selenium(link)
        time.sleep(2)
        if subcategory_html:
            chairs = get_chair_names(subcategory_html)
            all_chairs.extend(chairs)

            # Обрабатываем пагинацию
            pagination_links = get_pagination_links(subcategory_html, link)
            for page_link in pagination_links:
                print(f"Обрабатываю страницу пагинации: {page_link}")
                page_html = get_page_with_selenium(page_link)
                time.sleep(2)
                if page_html:
                    chairs = get_chair_names(page_html)
                    all_chairs.extend(chairs)

    print(f"Первые 5 наименований: {all_chairs[:5]}")
    print(f"Всего наименований: {len(all_chairs)}")

    with open('utfc_chairs_list.txt', 'w', encoding='utf-8') as f:
        for chair in all_chairs:
            f.write(chair + '\n')

    print(f"Сохранено {len(all_chairs)} наименований в файл utfc_chairs_list.txt")

if __name__ == "__main__":
    main()
