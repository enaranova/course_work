import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_profile_photos(self, profile_photos_list, path):
        headers = self.get_headers()
        result = requests.put(url='https://cloud-api.yandex.net/v1/disk/resources?path=' + path, headers=headers)
        if result.status_code == 409:
            print("Такая папка уже существует. Задайте другое имя для создания новой папки")
        elif result.status_code == 201:
            for i in profile_photos_list:
                photo_url = i['url']
                file_name = i['likes']
                upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?url=' + photo_url + '&path=' + path + '/' + file_name + '.jpg'
                headers = self.get_headers()
                params = {"overwrite": "true"}
                response = requests.post(url=upload_url, params=params, headers=headers)
            print(f'Ваши фото загружены в папку {path} на яндекс диске')
        else:
            print('Ошибка')