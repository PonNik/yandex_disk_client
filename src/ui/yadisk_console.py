import os
from src.core.yadisk import YandexDiskClient

class YandexDiskConsole:
    def __init__(self, token):
        self.disk_client = YandexDiskClient(token)
        self.current_path = '/'

    def run_console(self):
        while True:
            command = input(f'{self.current_path}> ')
            self.execute_command(command)

    def execute_command(self, command):
        parts = command.split()
        if not parts:
            return

        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == 'cd':
            self.change_directory(args)
        elif cmd == 'ls':
            self.list_contents()
        elif cmd == 'download':
            self.download_file(args)
        elif cmd == 'exit':
            exit()
        else:
            print(f'Unknown command: {cmd}')

    def change_directory(self, args):
        if not args:
            print('Usage: cd <directory>')
            return

        target_dir = args[0]
        if target_dir == '..':
            # Move to the parent directory
            self.current_path = os.path.dirname(self.current_path.rstrip('/'))
        else:
            # Move to the specified directory
            self.current_path = os.path.join(self.current_path, target_dir)

    def list_contents(self):
        folder_contents = self.disk_client.get_folder_contents(self.current_path)
        print(f'Contents of {self.current_path}:')
        for item in folder_contents['_embedded']['items']:
            print(item['name'])

    def download_file(self, args):
        if not args:
            print('Usage: download <file_path>')
            return

        file_path = args[0]
        local_path = file_path.split('/')[-1]  # Use the last part of the file path as the local file name
        self.disk_client.download_file(file_path, local_path)
        print(f'File successfully downloaded to {local_path}')

