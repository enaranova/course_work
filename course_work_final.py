from importlib import import_module
from configparser import ConfigParser
from pprint import pprint
from vk_user_module import VkUser
from ya_uploader_module import YaUploader
from get_json_file_module import get_json_file

config = ConfigParser()  # создаём объекта парсера
config.read('config.ini')  # читаем конфиг

username = input('Введите id или screen_name: ')
photos_quantity = int(input('Сколько фотографий вы хотите скачать? '))

vk_client = VkUser(token=config['Vkontakte']['token'], version='5.131')
profile_photos_list = vk_client.get_profile_photos(username, photos_quantity=photos_quantity)

get_json_file(profile_photos_list=profile_photos_list, path='ПУТЬ/ИМЯ.json')

ya_client = YaUploader(config['YandexDisk']['token'])
ya_client.upload_profile_photos(profile_photos_list, 'ИМЯ_ПАПКИ')