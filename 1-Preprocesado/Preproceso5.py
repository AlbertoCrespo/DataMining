# -*- coding: utf-8 -*-

import sqlite3
import os
import csv

print "Eliminando registros repetidos..."
try:
	con = sqlite3.connect('Accidentes1.db')
	con.text_factory = str
	cursor = con.cursor()

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



	con.commit()
	cursor.close()
	con.close()
except sqlite3.OperationalError:
	print "La base de datos ya existe"


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()


Descripcion = []
Localizacion = []
Accidente = []
Lesiones = []
Fallecimiento = []
Merc_Peligrosas = []
Vehi_Comercial = []
Alcohol = []
Tipo_de_Vehiculo = []
Anio = []
Marca = []
Modelo = []
Contr_Accidente = []
Genero = []
Tipo_Arresto = []



cursor.execute("SELECT distinct Descripcion, Localizacion, Accidente, Lesiones, Fallecimiento, Merc_Peligrosas, Vehi_Comercial, Alcohol, Tipo_de_Vehiculo, Anio, Marca, Modelo, Contr_Accidente, Genero, Tipo_Arresto FROM ACCIDENTES")
for i in cursor:
	Descripcion.append(str(i[0]).encode('utf-8'))
	Localizacion.append(str(i[1]).encode('utf-8'))
	Accidente.append(str(i[2]).encode('utf-8'))
	Lesiones.append(str(i[3]).encode('utf-8'))
	Fallecimiento.append(str(i[4]).encode('utf-8'))
	Merc_Peligrosas.append(str(i[5]).encode('utf-8'))
	Vehi_Comercial.append(str(i[6]).encode('utf-8'))
	Alcohol.append(str(i[7]).encode('utf-8'))
	Tipo_de_Vehiculo.append(str(i[8]).encode('utf-8'))
	Anio.append(str(i[9]).encode('utf-8'))
	Marca.append(str(i[10]).encode('utf-8'))
	Modelo.append(str(i[11]).encode('utf-8'))
	Contr_Accidente.append(str(i[12]).encode('utf-8'))
	Genero.append(str(i[13]).encode('utf-8'))
	Tipo_Arresto.append(str(i[14]).encode('utf-8'))

con.commit()
cursor.close()
con.close()

con = sqlite3.connect('Accidentes1.db')
cursor = con.cursor()

for i in range(len(Descripcion)):
	cursor.execute("INSERT INTO Accidentes (id, Descripcion, Localizacion, Accidente, Lesiones, Fallecimiento, Merc_Peligrosas, Vehi_Comercial, Alcohol, Tipo_de_Vehiculo, Anio, Marca, Modelo, Contr_Accidente, Genero, Tipo_Arresto) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
				(str(i), Descripcion[i], Localizacion[i], Accidente[i], Lesiones[i], Fallecimiento[i], Merc_Peligrosas[i], Vehi_Comercial[i], Alcohol[i], Tipo_de_Vehiculo[i], Anio[i], Marca[i],Modelo[i], Contr_Accidente[i], Genero[i], Tipo_Arresto[i]))

con.commit()
cursor.close()
con.close()

os.system("rm Accidentes.db")
os.system("mv Accidentes1.db Accidentes.db")