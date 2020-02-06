# l=[]
# for letter in 'python':
#     if(letter == 't'):
#         l.append(letter)
# print(l)
# l=[ letter  for letter in 'pythttton'  if (letter == 't')]
# print(l)





# import csv
#
# with open('Python.csv', 'w') as csvfile:
# fieldnames = ['first_name', 'last_name', 'Rank']
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#    fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})
#     writer.writerow({'Rank': 'A', 'first_name': 'Smith',
#                      'last_name': 'Rodriguez'})
#     writer.writerow({'Rank': 'B', 'last_name': 'Oscar', 'first_name': 'Jane'})
#     writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
#
# print("Writing complete")


#create a csv file
#Heading == "name"  "admission year"  "section"  "group"
#read with the help of pandas

# heading skip

import csv

with open('class.csv', 'w') as csvfile:
    fieldnames = ["name" , "admission year" , "section" , "group"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Sonali', 'admission year': "2018", 'section': 'A','group':'2'})
    writer.writerow({'admission year': "2018",'name': 'Riya', 'section': 'A','group':'2'})
    writer.writerow({'admission year': "2018",  'section': 'A','name': 'Priya', 'group': '2'})
    writer.writerow({'admission year': "2018", 'section': 'A', 'group': '2', 'name': 'Rajan'})
    writer.writerow({'section': 'A','admission year': "2018",  'group': '2', 'name': 'Ram'})
    writer.writerow({'section': 'A',  'group': '2', 'admission year': "2018",'name': 'Sham'})
    writer.writerow({'section': 'A', 'group': '2', 'name':'CSK','admission year': "2018"})
    writer.writerow({'admission year': "2018", 'group': '2', 'section': 'A','name': 'KKR'})
    writer.writerow({'section': 'A','admission year': "2018", 'name': 'Punjab','group': '2',})
    writer.writerow({'group': '2', 'name': 'Mohan','section': 'A', 'admission year': "2018"})
import pandas
df = pandas.read_csv('class.csv', skiprows=[0])
print(df)

print("Writing complete")

