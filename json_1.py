
data = {
	"action" : "msg",
	"to" : "account_name",
	"from" : "account_name",
	"encoding" : "ascii",
	"message" : "message"
}

import json

from pprint import pprint

with open('read.json') as file:
    row = file.read()
    pprint(json.loads(row))


with open('write.json', 'w') as file:
    json.dump(data, file)