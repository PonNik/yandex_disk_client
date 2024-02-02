from src.ui.yadisk_console import YandexDiskConsole

if __name__ == '__main__':
    # Замените 'YOUR_TOKEN' на ваш токен Яндекс.Диска
    token = 'y0_AgAAAAA9XrX7AAst4wAAAAD5AN01yz_bCIHSQRW4wkChDGeuripnQAY'
    yandex_disk_console = YandexDiskConsole(token)
    yandex_disk_console.run_console()