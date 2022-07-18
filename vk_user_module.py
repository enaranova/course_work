import requests
from pprint import pprint

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version) -> None:
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_profile_photos(self, user_id=None, photos_quantity=None):
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
        profile_photos_list_new = []
        
        if photos_quantity > len(profile_photos_list):
            print(f'В вашем профиле нет столько фотографий аватарок.')
            exit
        else:
            for i in range(photos_quantity):
                profile_photos_list_new.append(profile_photos_list[i])
            return profile_photos_list_new