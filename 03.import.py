import csv
with open('C:\\Mijn\\departement.csv', mode='r') as dept :
     rd = csv.reader(dept, delimiter=',')
     for r in rd :
        print(r)