
# Python Script for RustDesk Auto-Update
# Created by IgorMan. 2024
# https://best-itpro.ru

# pip install rustdesk_auto_update

import os
import requests
import shutil
import platform
import tempfile

# URL to check the latest version of RustDesk
RUSTDESK_LATEST_RELEASE_URL = "https://api.github.com/repos/rustdesk/rustdesk/releases/latest"

# Folder for temporary storage of files
TEMP_DIR = tempfile.gettempdir()

def get_latest_version():
    """Last release of RustDesk"""
    response = requests.get(RUSTDESK_LATEST_RELEASE_URL)
    if response.status_code != 200:
        raise Exception("Can't get info about last release version RustDesk. Check your Internet connection...")
    return response.json()


def download_file(url, output_path):
    """Download the latest version of RustDesk"""
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"Failed to download installer: {url}")
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


def main():
    try:
        # Last release of RustDesk
        latest_release = get_latest_version()
        latest_version = latest_release["tag_name"]
        print(f"Last release of RustDesk: {latest_version}")

        # Определяем ссылку для скачивания
        assets = latest_release["assets"]
        for asset in assets:
            # for Windows
            if "x86_64.exe" in asset["name"]:
                download_url = asset["browser_download_url"]
                break
        else:
            raise Exception("Failed to find file for download.")

        # Скачиваем файл
        rustdesk_path = os.path.join(TEMP_DIR, asset["name"])
        print(rustdesk_path)
        print("Get last release...\n")

        os.makedirs(TEMP_DIR, exist_ok=True)
        download_file(download_url, rustdesk_path)

        print(f"Last release of RustDesk: {latest_version}")
        print(f"was download in: {rustdesk_path}")
        print("Just install it and enjoy!\n;) ")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
