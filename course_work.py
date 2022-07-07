import requests
import time
from pprint import pprint
import json

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version) -> None:
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_profile_photos(self, user_id=None):
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
        }
        
        profile_photos_list = []
        req = requests.get(photos_url, params={**self.params, **photos_params}).json()
        for item in req['response']['items']:
            d = {}
            size = item['sizes'][-1]['type']
            url = item['sizes'][-1]['url']
            likes = item['likes']['count']
            date = item['date']
            d['likes'] = str(likes)
            for i in profile_photos_list:
                if str(likes) in i.values():
                    d['likes'] = str(likes) + str(date)
            d['size'] = size
            d['url'] = url
            profile_photos_list.append(d)
        return profile_photos_list

    def get_json_file(self, profile_photos_list, path):
        with open(path, 'w', encoding='utf-8') as f:
            json_photos_list=[]
            for i in profile_photos_list:
                d={}
                for k, v in i.items():
                    if k != 'url':
                        d[k] = v
                    else:
                        continue
                json_photos_list.append(d)
            json.dump(json_photos_list, f, ensure_ascii=False, indent=2)


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_profile_photos(self, profile_photos_list, path):
        for i in profile_photos_list:
            photo_url = i['url']
            file_name = i['likes']
            upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?url=' + photo_url + '&path=' + path + file_name + '.jpg'
            headers = self.get_headers()
            params = {"overwrite": "true"}
            response = requests.post(url=upload_url, params=params, headers=headers)
            print(response)
    
vk_client = VkUser('ВАШ ТОКЕН VK', '5.131')
profile_photos_list = vk_client.get_profile_photos('ВАШ ID VK')
pprint(profile_photos_list)
vk_client.get_json_file(profile_photos_list, 'ПУТЬ/ИМЯ ФАЙЛА.json')

ya_client = YaUploader('ВАШ ТОКЕН YA')
pprint(ya_client.upload_profile_photos(profile_photos_list, 'ПУТЬ ПАПКИ на Я.ДИСКЕ/'))