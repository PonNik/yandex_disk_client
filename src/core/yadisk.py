import requests

class YandexDiskClient:
    def __init__(self, token):
        self.api_base_url = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {'Authorization': f'OAuth {token}'}

    def get_folder_contents(self, path='/'):
        params = {'path': path}
        response = requests.get(f'{self.api_base_url}/resources', headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def download_file(self, file_path, local_path):
        params = {'path': file_path}
        response = requests.get(f'{self.api_base_url}/resources/download', headers=self.headers, params=params)
        response.raise_for_status()

        download_url = response.json()['href']
        file_response = requests.get(download_url)
        file_response.raise_for_status()

        with open(local_path, 'wb') as file:
            file.write(file_response.content)