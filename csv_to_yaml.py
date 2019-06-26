

import csv, yaml
file_text = []
with open('read.csv') as file:
      text = csv.reader(file)
      for row in text:
            file_text.append(row)

with open('write.yaml', 'w') as file:
    row = yaml.dump(file_text, file, Dumper=yaml.Dumper)