# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()


cursor.execute("SELECT Descripcion,Vehi_Comercial,Tipo_de_Vehiculo,Anio,Marca,Modelo,Tipo_Arresto,Riesgo FROM ACCIDENTES")

archivo=open ("BD.csv","a")
archivo.write("Descripcion,Vehi_Comercial,Tipo_de_Vehiculo,Anio,Marca,Modelo,Tipo_Arresto,Riesgo")
archivo.write("\n")

for i in cursor:
	archivo.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7]))
	archivo.write("\n")

archivo.close()


reader = csv.reader(open('BD.csv', 'rb'))
lista =[]

for index, rox in enumerate(reader):
	x=str.split(rox[0])
	i=0
	string=''
	while i<len(x) and i<2:
		string=string+x[i]+" "
		i=i+1
	if string.upper() not in lista:
		lista.append(string.upper())


os.system("rm BD.csv")


txt = open('descripciones.txt', 'w')
con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()


y = 0
z = 0

for elemento in lista:
	x = "UPDATE ACCIDENTES SET Descripcion = '"+str(y)+"'  WHERE Descripcion LIKE '"+elemento+"%'"
	cursor.execute(x)
	txt.write(elemento + " CON NUM " + str(y) + "\n")
	con.commit()
	cursor.execute("INSERT INTO Descripciones (id, descripciones, numero_descripcion) VALUES (?,?,?)", (str(z),str(elemento),str(y)))
	con.commit()
	y = y + 1
	z = z + 1

cursor.execute("delete from accidentes where Descripcion not in( select distinct Descripcion from accidentes where Descripcion GLOB  '[0-9]' or Descripcion GLOB '[0-9][0-9]' or Descripcion GLOB '[0-9][0-9][0-9]')")
con.commit()

cursor.execute("SELECT Descripcion,Vehi_Comercial,Tipo_de_Vehiculo,Anio,Marca,Modelo,Tipo_Arresto,Riesgo FROM ACCIDENTES")
cursor.close()
con.close()




