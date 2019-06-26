
import csv, json
file_text = []
with open('read.csv') as file:
      text = csv.reader(file)
      for row in text:
            file_text.append(row)

with open('write.json', 'w') as file:
    json.dump(file_text, file)