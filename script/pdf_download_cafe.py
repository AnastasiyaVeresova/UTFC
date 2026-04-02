import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Настройка Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Работа в фоне
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\UTFC\Documents\Downloads\pdfs\chair_cafe_and_bar",  # Папка для сохранения PDF
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Открываем страницу с товарами
driver.get("http://127.0.0.1:5500/html/chair_cafe_and_bar.html")
time.sleep(3)  # Ждём загрузки страницы

# Находим все ссылки на карточки товаров
product_links = driver.find_elements(By.CSS_SELECTOR, ".product-card a")
urls = [link.get_attribute("href") for link in product_links]

# Переходим по каждой ссылке и скачиваем PDF
for url in urls:
    driver.get(url)
    time.sleep(2)  # Ждём загрузки страницы товара
    try:
        download_button = driver.find_element(By.ID, "downloadPdf")
        download_button.click()
        print(f"Скачиваю PDF для: {url}")
        time.sleep(3)  # Ждём скачивания
    except Exception as e:
        print(f"Не удалось скачать PDF для {url}: {e}")

# Закрываем браузер
driver.quit()
print("Все PDF скачаны!")
