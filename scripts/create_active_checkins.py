import csv
import json
json_data = open('/home/bwaters/School/CS484/yelp-restaurant-classifiers/json/checkins.json')
data = json.load(json_data)
f = open('active_checkins.json', 'w')
with open('unique_ids') as f2:
    ids = f2.read().splitlines()
my_list = []
for x in data:
    if x['business_id'] in ids:
        f.write(str(x)+',\n')
f.close()
f2.close()
