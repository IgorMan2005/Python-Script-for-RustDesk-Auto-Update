# rustdesk_auto_update
## Python Script for RustDesk Auto-Update


<img src="https://igorman2005.github.io/images/rustdesk.png" alt="rustdesk_auto_update">


### Install rustdesk_auto_update

```
pip install requests

pip install rustdesk-auto-update
```

### Run rustdesk_auto_update
```
rustdesk_auto_update.main()
```


### How the script works:

- Check for the latest version: The script uses the GitHub API to get information about the latest RustDesk release.
- Download: Downloads a ZIP archive with the latest version of RustDesk.
- Install: Unpacks the archive and moves the files to the desired directory (for example, Program Files on Windows or /opt on Linux).
- Cleanup: Removes temporary files after installation.

### Notes:

- The script is written for Windows. If you are using Linux or macOS, you may need to modify the installation paths.
- Make sure you have administrator rights to install the program.
- If RustDesk requires additional actions for installation (for example, running the installer), they should be added to the install_rustdesk function.
- This script can be run periodically (for example, via cron on Linux or Task Scheduler on Windows) to automatically update RustDesk.

---

### Как работает скрипт:

- Проверка последней версии: Скрипт использует GitHub API для получения информации о последнем релизе RustDesk.
- Скачивание: Скачивает ZIP-архив с последней версией RustDesk.
- Установка: Распаковывает архив и перемещает файлы в нужную директорию (например, Program Files на Windows или /opt на Linux).
- Очистка: Удаляет временные файлы после установки.

### Примечания:

- Скрипт написан для Windows. Если вы используете Linux или macOS, может потребоваться доработка путей установки.
- Убедитесь, что у вас есть права администратора для установки программы.
- Если RustDesk требует дополнительных действий для установки (например, запуск инсталлятора), их нужно добавить в функцию install_rustdesk.
- Этот скрипт можно запускать периодически (например, через cron на Linux или Task Scheduler на Windows) для автоматического обновления RustDesk.


### Documentation

https://best-itpro.ru/news/rustdesk_auto_update/


That's All, Folks! 
;)

---

https://best-itpro.ru
