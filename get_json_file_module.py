import json

def get_json_file(profile_photos_list, path):
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
