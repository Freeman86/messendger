
data = [
      ['hostname','vendor','model','location'],
      ['kp1','Cisco','2960','Moscow'],
      ['kp2','Cisco','2960','Novosibirsk'],
      ['kp3','Cisco','2960','Kazan'],
      ['kp4','Cisco','2960','Tomsk']
        ]

import csv

with open('read.csv') as file:
      text = csv.reader(file)
      for row in text:
            print(row)

with open('write.csv', 'w') as file:
      wr = csv.writer(file)
      for row in data:
            wr.writerow(row)