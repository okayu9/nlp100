# coding: utf-8
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

for key, value in basic_info_dic.items():
    value_no_em = re.sub("''''(.*?)''''", '\\1', value)
    value_no_em = re.sub("'''(.*?)'''", '\\1', value_no_em)
    value_no_em = re.sub("''(.*?)''", '\\1', value_no_em)
    basic_info_dic[key] = value_no_em

for key, value in basic_info_dic.items():
    print(f'{key}: {value}')
