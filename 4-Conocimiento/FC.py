# -*- coding: utf-8 -*-

import csv
import sys




def SacarFilasColumnas(i):
	lista = []
	reader = csv.reader(open('Final.csv', 'rb'))
	for index,row in enumerate(reader):
		x = str(row[i])
		a = x in lista
		if a == False:
			lista.append(x)
	return lista



def Contar(modelo,tipo,f,c):
	count = 0
	reader = csv.reader(open('Final.csv', 'rb'))
	for index,row in enumerate(reader):
		if modelo == str(row[f]) and tipo == str(row[c]):
			count = count + 1

	return count


nombre = sys.argv[1]
archivo=open (nombre+".csv","a")

f = int(sys.argv[2])
c = int(sys.argv[3])

filas = SacarFilasColumnas(f)
columnas = SacarFilasColumnas(c)

archivo.write("X,")
for i in range(len(columnas)-1):
	archivo.write(str(columnas[i])+",")
archivo.write(str(columnas[len(columnas)-1]))
archivo.write("\n")


for i in range(len(filas)):
	archivo.write(str(filas[i])+",")
	for j in range(len(columnas)-1):
		x = Contar(filas[i],columnas[j],f,c)
		archivo.write(str(x)+",")
	x = Contar(filas[i],columnas[len(columnas)-1],f,c)
	archivo.write(str(x))
	archivo.write("\n")

archivo.close()
