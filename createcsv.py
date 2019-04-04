import csv
import random

ar1=['hola','mundo',1,2,3,4,5]
ar2=[]

for i in enumerate (ar1):
	ar2.append(random.randint(1,5))

file=[ar1,ar2]
newfile=open('archivo.csv','w',newline='')
arch=csv.writer(newfile, delimiter=',')
arch.writerow(['arreglo 1','arreglo 2'])
arch.writerows(zip(*file))

print('Archivo csv creado')
