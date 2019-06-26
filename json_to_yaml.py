

import json, yaml

from pprint import pprint

with open('read.json') as file:
    row = file.read()
    file_text = json.loads(row)

with open('write.json', 'w') as file:
    json.dump(file_text, file)