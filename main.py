from src.ui.yadisk_console import YandexDiskConsole
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    token = os.getenv("TOKEN")
    yandex_disk_console = YandexDiskConsole(token)
    yandex_disk_console.run_console()