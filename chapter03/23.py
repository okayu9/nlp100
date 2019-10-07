import re
import gzip
import json


wp_filename = 'jawiki-country.json.gz'

contents = {}
with gzip.open(wp_filename, 'r') as f:
    for line in f:
        content = json.loads(line)
        contents[content['title']] = content['text']

uk_text = contents['イギリス'].split('\n')

for line in uk_text:
    match = re.search(r'^=(=+)(.*?)=*$', line)
    if not match:
        continue
    head_symbol = match.group(1)
    head_level = len(head_symbol)
    head = match.group(2).strip()
    print(head, head_level, sep='\t')
