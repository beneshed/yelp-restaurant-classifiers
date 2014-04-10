import csv
my_list = [] 
with open('categories.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        for col in row:
            my_list.append(col.strip()) 

my_list=set(my_list)
print(my_list)
