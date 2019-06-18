

import requests

r = requests.get('https://yandex.ru')

text = r.content

print(text.decode())