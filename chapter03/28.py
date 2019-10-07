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
    value_no_link = re.sub(r'\[\[([^|]*?)\]\]', '\\1', value_no_em)
    value_no_link = re.sub(r'\[\[.*?\|(.*?)\]\]', '\\1', value_no_link)
    value_no_link = re.sub(r'\[https?://.*?\]', '', value_no_link)
    value_no_ref = re.sub(r'<ref[ >][\s\S]*?</ref>', '', value_no_link)
    value_no_ref = re.sub(r'<ref .*? />', '', value_no_ref)
    value_no_ref = value_no_ref.replace('<references />', '')
    value_no_br = re.sub(r'<br ?/>', '', value_no_ref)
    basic_info_dic[key] = value_no_br

for key, value in basic_info_dic.items():
    print(f'{key}: {value}')
