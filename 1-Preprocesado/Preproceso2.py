# -*- coding: utf-8 -*-

import csv
import os

def blanco(x):
	a = True
	if x == "" or x == None:
		a = False
	return a

def YesNo(x):
	a = False
	if x == "Yes" or x == "No":
		a = True
	return a

def Genero(x):
	a = False
	if x == "F" or x == "M":
		a = True
	return a

def Anno(x):
	a = True
	try:
		x = int(x)
		if x > 2016 or x < 1960:
			a = False
		return a 
	except ValueError:
		a = False
		return a


#de 823.130 registros a 749277

print "Eliminando espacios en blanco y valores incorrectos..."
reader = csv.reader(open('Preproceso1.csv', 'rb'))
archivo=open ("Preproceso2.csv","a")

archivo.write("Descripcion,Localizacion,Accidente,Lesiones,Fallecimiento,Mercancias Peligrosas,Vehiculo Comercial, Alcohol, Tipo de Vehiculo, Año, Marca, Modelo, Contribuyo Accidente, Genero, Tipo de Arresto")
archivo.write("\n")


for index,row in enumerate(reader):


	x1 = blanco(str(row[4]))
	x2 = blanco(str(row[5]))
	x3 = blanco(str(row[8]))
	x4 = blanco(str(row[10]))
	x5 = blanco(str(row[12]))
	x6 = blanco(str(row[14]))
	x7 = blanco(str(row[15]))
	x8 = blanco(str(row[16]))
	x9 = blanco(str(row[19]))
	x10 = blanco(str(row[20]))
	x11 = blanco(str(row[21]))
	x12 = blanco(str(row[22]))
	x13 = blanco(str(row[27]))
	x14 = blanco(str(row[29]))
	x15 = blanco(str(row[33]))

	if x1 == True and x2 == True and x3 == True and x4 == True and x5 == True and x6 == True and x7 == True and x8 == True and x9 == True and x10 == True and x11 == True and x12 == True and x13 == True and x14 == True and x15 == True:
		x = True
	else:
		x = False


	y1 = YesNo(str(row[8]))
	y2 = YesNo(str(row[10]))
	y3 = YesNo(str(row[12]))
	y4 = YesNo(str(row[14]))
	y5 = YesNo(str(row[15]))
	y6 = YesNo(str(row[16]))
	y7 = YesNo(str(row[27]))

	if y1 == True and y2 == True and y3 == True and y4 == True and y5 == True and y6 == True and y7 == True:
		y = True
	else:
		y = False


	z = Genero(str(row[29]))

	w = Anno(str(row[20]))


	if x == True and y == True and z == True and w == True:
		archivo.write(str(row[4])+","+str(row[5])+","+str(row[8])+","+str(row[10])+","+str(row[12])+","+str(row[14])+","+str(row[15])+","+str(row[16])+","+str(row[19])+","+str(row[20])+","+str(row[21])+","+str(row[22])+","+str(row[27])+","+str(row[29])+","+str(row[33]))
		archivo.write("\n")
	

archivo.close()
os.system("rm Preproceso1.csv")