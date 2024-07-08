import csv
import codecs
with codecs.open('C:\\Mijn\\departement.csv', encoding= 'utf-8', errors= 'replace') as dept :
     rd = csv.reader(dept, delimiter=',')
     departements = []
     for r in rd :
        departements.append(r[2])


departements.extend(['Geneve', 'Vaud', 'Valais'])
# departements.insert(0,'Neuchatel')
# print(departements)
# print(departements.pop())
# departements[2:2] = ['Neuchatel', 'Jura']
departements.sort()
print(departements)

# LIFO et FIFO
