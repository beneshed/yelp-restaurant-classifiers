import json
json_data = open('business.json')
data = json.load(json_data)
to_write = {}
fields = {}
f = open('categories', 'w')
my_list = []
for x in data:
    if x['open'] == True:
        f.write(str(x['categories'])+'\n')

json.dump(my_list, f)
f.close()
