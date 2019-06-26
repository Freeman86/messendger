
data = {

    'action1': 'msg_1',
    'to1': 'account_1',
    'action2': 'msg_2',
    'to2': 'account_2'
}


import yaml

with open('read.yaml') as file:
    row = yaml.load(file, Loader=yaml.Loader)
    print(row)


with open('write.yaml', 'w') as file:
    row = yaml.dump(data, file, Dumper=yaml.Dumper)
