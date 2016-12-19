# -*- coding: utf-8 -*-

import csv
import string



def cambiar(x):
	buscar =","
	reemplazar_por = " "
	x = string.replace(x,buscar,reemplazar_por)
	return x

print "Limpiando comas en csv..."
reader = csv.reader(open('violacionestrafico.csv', 'rb'))
archivo=open ("Preproceso1.csv","a")

for index,row in enumerate(reader):
	for i in range(34):
		archivo.write(str(cambiar(str(row[i])))+",")
	archivo.write(str(cambiar(str(row[34]))))
	archivo.write("\n")
archivo.close()