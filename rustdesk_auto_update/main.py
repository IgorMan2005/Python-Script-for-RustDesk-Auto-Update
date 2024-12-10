
# pip install rustdesk_auto_update

import os
import requests
import subprocess
import zipfile
import shutil
import platform

# URL для проверки последней версии RustDesk
RUSTDESK_LATEST_RELEASE_URL = "https://api.github.com/repos/rustdesk/rustdesk/releases/latest"

# Папка для временного хранения файлов
TEMP_DIR = "rustdesk_temp"


def get_latest_version():
    """Получает информацию о последней версии RustDesk."""
    response = requests.get(RUSTDESK_LATEST_RELEASE_URL)
    if response.status_code != 200:
        raise Exception("Не удалось получить информацию о последней версии RustDesk.")
    return response.json()


def download_file(url, output_path):
    """Скачивает файл по указанному URL."""
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Не удалось скачать файл: {url}")
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def install_rustdesk(zip_path):
    """Устанавливает RustDesk из ZIP-архива."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR)

    # Перемещаем файлы в нужную директорию (например, в Program Files)
    if platform.system() == "Windows":
        install_dir = os.path.join("C:\\", "Program Files", "RustDesk")
    elif platform.system() == "Linux":
        install_dir = "/opt/rustdesk"
    elif platform.system() == "Darwin":  # macOS
        install_dir = "/Applications/RustDesk"
    else:
        raise Exception("Неподдерживаемая операционная система.")

    # Удаляем старую версию, если она существует
    if os.path.exists(install_dir):
        shutil.rmtree(install_dir)

    # Перемещаем новую версию
    shutil.move(os.path.join(TEMP_DIR, os.listdir(TEMP_DIR)[0]), install_dir)


def main():
    try:
        # Получаем информацию о последней версии
        latest_release = get_latest_version()
        latest_version = latest_release["tag_name"]
        print(f"Последняя версия RustDesk: {latest_version}")

        # Определяем ссылку для скачивания
        assets = latest_release["assets"]
        for asset in assets:
            if "Windows" in asset["name"] and asset["name"].endswith(".zip"):
                download_url = asset["browser_download_url"]
                break
        else:
            raise Exception("Не удалось найти файл для скачивания.")

        # Скачиваем файл
        print("Скачивание новой версии...")
        zip_path = os.path.join(TEMP_DIR, "rustdesk_latest.zip")
        os.makedirs(TEMP_DIR, exist_ok=True)
        download_file(download_url, zip_path)

        # Устанавливаем RustDesk
        print("Установка новой версии...")
        install_rustdesk(zip_path)

        # Очищаем временные файлы
        shutil.rmtree(TEMP_DIR)

        print("Обновление завершено!")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()