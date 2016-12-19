import sqlite3
import os
import csv



print "Creando base de datos Accidentes.db"

con = sqlite3.connect('Accidentes.db')
con.text_factory = str
cursor = con.cursor()

print "La base de datos se creo correctamente"

#CREAMOS LAS TABLAS

cursor.execute(''' CREATE TABLE CLUSTER (
	  id 					integer NOT NULL PRIMARY KEY,	
	  Descripcion			varchar(100),
	  Vehi_Comercial  		varchar(50),
	  Tipo_de_Vehiculo  	varchar(50),
	  Anio  	    		integer,
	  Marca  	    	    varchar(50),
	  Modelo                varchar(50),
	  Tipo_Arresto			varchar(50),
	  Riesgo				varchar(50),
	  Ocurrencias			varchar(50),
	  Grupo					varchar(50)
	);''')


print "Insertando valores del cvs..."
reader = csv.reader(open('BDC.csv', 'rb'))
x = 0
y = 1
for index,row in enumerate(reader):
	if x > 0:
		id = str(y)
		Descripcion= str(row[0])
		Vehi_Comercial= str(row[1])
		Tipo_de_Vehiculo= str(row[2])
		Anio= str(row[3])
		Marca= str(row[4])
		Modelo = str(row[5])
		Tipo_Arresto= str(row[6])
		Riesgo = str(row[7])
		Ocurrencias = str(row[8])
		Grupo = str(row[9])
		y = y +1
		cursor.execute("INSERT INTO CLUSTER (id, Descripcion,Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo, Ocurrencias, Grupo) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (id, Descripcion,Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca,Modelo,Tipo_Arresto,Riesgo,Ocurrencias,Grupo))
	x = x + 1

con.commit()
cursor.close()
con.close()





