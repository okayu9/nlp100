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
    line = line.rstrip()
    if re.search(r'^\[\[Category:.*\]\]$', line):
        print(line)
