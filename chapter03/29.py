# coding: utf-8
import urllib.request
import re
import gzip
import json


wp_filename = 'jawiki-country.json.gz'

contents = {}
with gzip.open(wp_filename, 'r') as f:
    for line in f:
        content = json.loads(line)
        contents[content['title']] = content['text']

uk_text = contents['イギリス']
match = re.search(r'\{\{基礎情報 .*\n\|([\s\S]*?)\n\}\}', uk_text)
basic_infos = match.group(1).split('\n|')
basic_infos = [info.split(' = ') for info in basic_infos]
basic_info_dic = {info[0]: info[1] for info in basic_infos}

image_url = basic_info_dic['国旗画像'].replace(' ', '+')
url = ('https://commons.wikimedia.org/w/api.php?'
       f'action=query&titles=File:{image_url}&'
       'prop=imageinfo&iiprop=url&format=json')
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))
url = tuple(data["query"]["pages"].values())[0]['imageinfo'][0]['url']
print(url)
