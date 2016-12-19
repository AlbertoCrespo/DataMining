import sqlite3
import os
import csv


try:
	print "Creando base de datos Accidentes.db"

	con = sqlite3.connect('Accidentes.db')
	con.text_factory = str
	cursor = con.cursor()

	print "La base de datos se creo correctamente"

	#CREAMOS LAS TABLAS

	cursor.execute(''' CREATE TABLE ACCIDENTES (
	  id 					integer NOT NULL PRIMARY KEY,	
	  Descripcion			varchar(100),
	  Localizacion         	varchar(50),
	  Accidente       		varchar(50),
	  Lesiones  			varchar(50),
	  Fallecimiento			varchar(50),
	  Merc_Peligrosas  		varchar(50),
	  Vehi_Comercial  		varchar(50),
	  Alcohol  				varchar(50),
	  Tipo_de_Vehiculo  	varchar(50),
	  Anio  	    		integer,
	  Marca  	    	    varchar(50),
	  Modelo                varchar(50),
	  Contr_Accidente		varchar(50),
	  Genero				varchar(50),
	  Tipo_Arresto			varchar(50)
	);''')


	print "Insertando valores del cvs..."
	reader = csv.reader(open('Preproceso2.csv', 'rb'))
	x = 0
	y = 1
	for index,row in enumerate(reader):
		if x > 0:
			id = str(y)
			Descripcion= str(row[0])
			Localizacion= str(row[1])
			Accidente= str(row[2])
			Lesiones= str(row[3])
			Fallecimiento= str(row[4])
			Merc_Peligrosas= str(row[5])
			Vehi_Comercial= str(row[6])
			Alcohol= str(row[7])
			Tipo_de_Vehiculo= str(row[8])
			Anio= str(row[9])
			Marca= str(row[10])
			Modelo = str(row[11])
			Contr_Accidente= str(row[12])
			Genero= str(row[13])
			Tipo_Arresto= str(row[14])
			y = y +1
			cursor.execute("INSERT INTO Accidentes (id, Descripcion, Localizacion, Accidente, Lesiones, Fallecimiento, Merc_Peligrosas, Vehi_Comercial, Alcohol, Tipo_de_Vehiculo, Anio, Marca, Modelo, Contr_Accidente, Genero, Tipo_Arresto) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
				(id, Descripcion, Localizacion, Accidente, Lesiones, Fallecimiento, Merc_Peligrosas, Vehi_Comercial, Alcohol, Tipo_de_Vehiculo, Anio, Marca,Modelo, Contr_Accidente, Genero, Tipo_Arresto))
		x = x + 1

	con.commit()
	cursor.close()
	con.close()
except sqlite3.OperationalError:
	print "La base de datos ya existe"


os.system("rm Preproceso2.csv")

