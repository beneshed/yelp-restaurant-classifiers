import csv
import json
json_data = open('/home/bwaters/School/CS484/yelp-restaurant-classifiers/json/business.json')
data = json.load(json_data)
csv_list = []
with open('categories.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        for col in row:
            csv_list.append(col.strip())

csv_list=set(csv_list)

to_write = {}
fields = {}
f = open('unique_ids', 'w')
my_list = []
ids = []
for x in data:
    if x['open'] == True:
        for y in x['categories']:
            if y in csv_list:
                ids.append(x['business_id']) 

ids = set(ids)
for i in ids:
    f.write(i+'\n')
        

json.dump(my_list, f)
f.close()
