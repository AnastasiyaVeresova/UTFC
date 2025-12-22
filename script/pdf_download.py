import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Основная папка для скачивания
base_download_dir = r"C:\Users\UTFC\Documents\Downloads\pdfs"
os.makedirs(base_download_dir, exist_ok=True)

# Настройка Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": base_download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Открываем страницу
    driver.get("http://127.0.0.1:5500/index.html")

    # Ждём, пока появятся кнопки .open-card-modal
    WebDriverWait(driver, 120).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#products .open-card-modal")) > 0
    )

    # Собираем все кнопки
    product_buttons = driver.find_elements(By.CSS_SELECTOR, "#products .open-card-modal")
    print(f"Найдено кнопок: {len(product_buttons)}")

    for i, button in enumerate(product_buttons):
        try:
            category = button.get_attribute("data-category")
            product_name = button.text
            print(f"Обрабатываю кнопку {i+1}/{len(product_buttons)}: {product_name} (Категория: {category})")

            # Создаём папку для категории, если её нет
            category_dir = os.path.join(base_download_dir, category)
            os.makedirs(category_dir, exist_ok=True)

            # Кликаем по кнопке (открывается в новом окне)
            driver.execute_script("arguments[0].scrollIntoView();", button)
            button.click()
            time.sleep(2)  # Даём время на открытие нового окна

            # Ждём появления нового окна
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

            # Переключаемся на новое окно
            driver.switch_to.window(driver.window_handles[1])

            # Ждём полной загрузки страницы карточки
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Ждём, пока страница полностью загрузится
            time.sleep(3)

            # Проверяем, есть ли кнопка для генерации PDF
            try:
                download_button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.ID, "downloadPdf"))
                )

                # Нажимаем кнопку для скачивания PDF
                download_button.click()
                print(f"Скачиваю PDF для: {product_name}")

                # Ждём завершения скачивания
                time.sleep(5)

                # Ищем последний скачанный файл
                files = os.listdir(base_download_dir)
                if files:
                    latest_file = max([os.path.join(base_download_dir, f) for f in files], key=os.path.getctime)
                    # Перемещаем файл в папку категории
                    shutil.move(latest_file, os.path.join(category_dir, os.path.basename(latest_file)))
                    print(f"Файл перемещён в {category_dir}")

            except Exception as e:
                print(f"Не удалось найти кнопку скачивания для {product_name}: {e}")

            # Закрываем окно после скачивания
            driver.close()

            # Возвращаемся к основному окну
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"Ошибка при обработке {product_name}: {e}")
            try:
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])
                    driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except:
                pass

finally:
    driver.quit()
    print("Все PDF скачаны!")
