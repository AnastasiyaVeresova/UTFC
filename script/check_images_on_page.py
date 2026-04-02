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

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Список страниц для проверки
pages = [
    "http://127.0.0.1:5500/html/chair_cafe_and_bar.html",
    "http://127.0.0.1:5500/html/chair_visitors.html",
    "http://127.0.0.1:5500/html/armchair_comfort.html",
    "http://127.0.0.1:5500/html/epik.html",
    "http://127.0.0.1:5500/html/armchair_personal.html",
    "http://127.0.0.1:5500/html/armchair_rukovoditel.html"
]

# Функция для проверки наличия изображений на странице
def check_images_on_page(url):
    driver.get(url)
    time.sleep(2)  # Ждём загрузки страницы
    images = driver.find_elements(By.TAG_NAME, "img")
    errors = []
    for img in images:
        try:
            if not img.get_attribute("src") or img.get_attribute("naturalWidth") == "0":
                errors.append(f"Отсутствует или не загружено изображение: {img.get_attribute('outerHTML')}")
        except Exception as e:
            errors.append(f"Ошибка при проверке изображения: {e}")
    return errors

# Основной цикл
for page in pages:
    print(f"\nПроверяю страницу: {page}")
    errors = check_images_on_page(page)
    if errors:
        print(f"Ошибки на странице {page}:")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"На странице {page} все изображения загружены корректно.")

# Закрываем браузер
driver.quit()
print("\nПроверка завершена!")
