# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()

try:
	print "Creando tabla transformada..."
	cursor.execute('''\


		CREATE TABLE transformada (
			  id 					integer NOT NULL PRIMARY KEY,		
			  Descripcion			varchar(100),
			  Vehi_Comercial  		varchar(50),
			  Tipo_de_Vehiculo  	varchar(50),
			  Anio  	    		integer,
			  Marca  	    		varchar(50),
			  Modelo  				varchar(50),
			  Tipo_Arresto			varchar(50)
		);''')
	con.commit()


except sqlite3.OperationalError:
	print "La tabla transformada ya existe. Limpiando tabla..."
	cursor.execute('''
	delete from transformada where 1; ''')
	pass

try:
	print "Creando vistas auxiliares..."
	cursor.execute('''

		create view riesgos as select
			id as riesgo_id,
			case when lesiones="Yes" then 1 else 0 end as riesgo1, 
			case when alcohol="Yes" then 1 else 0 end as riesgo2,
			case when contr_accidente="Yes" then 1 else 0 end as riesgo3,
			case when fallecimiento="Yes" then 1 else 0 end as riesgo4,
			case when merc_peligrosas="Yes" then 1 else 0 end as riesgo5
		from accidentes;''')
except sqlite3.OperationalError:
	print "La vista riesgos ya existe"
	pass

try:
	cursor.execute('''

		create view riesgo as select
			riesgo_id as riesgo_id,
			riesgo1+riesgo2+riesgo3+riesgo4+riesgo5 as total
		from riesgos;''')
except sqlite3.OperationalError:
	print "La vista riesgo ya existe"
	pass

print "Insertando datos en la tabla..."
cursor.execute('''

	insert into transformada 
	(id, descripcion, Vehi_Comercial, Tipo_de_Vehiculo, Anio,
		Marca, Modelo, Tipo_Arresto)
	select id, descripcion, Vehi_Comercial, 
		Tipo_de_Vehiculo,Anio, Marca, Modelo, Tipo_Arresto
	from accidentes;''')

cursor.execute('''
	select id, Descripcion, Vehi_Comercial, Tipo_de_Vehiculo, 
		Anio, Marca, Modelo, Tipo_Arresto, Total as Riesgo
	from transformada
	join riesgo
	on transformada.id = riesgo.riesgo_id;''')

con.commit()

print "Creando csv..."
archivo=open ("Transformada1.csv","a")
archivo.write("Descripcion, Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo")
archivo.write("\n")

for i in cursor:
	archivo.write(str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8]))
	archivo.write("\n")

archivo.close()
cursor.close()
con.close()

print "Transformacion 1 realizada"

print "Creando la base de datos..."
con = sqlite3.connect('Accidentes1.db')
cursor = con.cursor()

cursor.execute(''' CREATE TABLE ACCIDENTES (
	  id 					integer NOT NULL PRIMARY KEY,	
	  Descripcion			varchar(100),
	  Vehi_Comercial  		varchar(50),
	  Tipo_de_Vehiculo  	varchar(50),
	  Anio  	    		integer,
	  Marca  	    	    varchar(50),
	  Modelo                varchar(50),
	  Tipo_Arresto			varchar(50),
	  Riesgo 				integer
	);''')

cursor.execute('''\


		CREATE TABLE Marca (
			  id 					integer NOT NULL PRIMARY KEY,		
			  marca						varchar(100),
			  numero_marca		  		varchar(50)

		);''')

con.commit()

cursor.execute('''\


		CREATE TABLE Modelo (
			  id 					integer NOT NULL PRIMARY KEY,		
			  modelo  					varchar(50),
			  numero_modelo  	    	varchar(50)


		);''')

con.commit()
cursor.execute('''\


		CREATE TABLE tipoarresto (
			  id 					integer NOT NULL PRIMARY KEY,		
			  tipo_arresto  	    	varchar(50),
			  numero_tipo_arresto  		varchar(50)

		);''')

con.commit()

cursor.execute('''\


		CREATE TABLE tipovehiculo (
			  id 					integer NOT NULL PRIMARY KEY,		
			  tipo_vehiculo  	    	varchar(50),
			  numero_tipo_vehiculo  	varchar(50)

		);''')

con.commit()

cursor.execute('''\


		CREATE TABLE vehiculocomercial (
			  id 					integer NOT NULL PRIMARY KEY,		
			  vehiculo_comercial  	    	varchar(50),
			  numero_vehiculo_comercial  	varchar(50)

		);''')

con.commit()

cursor.execute('''\


		CREATE TABLE Descripciones (
			  id 					integer NOT NULL PRIMARY KEY,		
			  descripciones  	    	varchar(50),
			  numero_descripcion  		varchar(50)

		);''')
con.commit()

print "Insertando en la nueva base de datos transformada..."
reader = csv.reader(open('Transformada1.csv', 'rb'))
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
		Riesgo= str(row[7])
		y = y +1
		cursor.execute("INSERT INTO ACCIDENTES (id, Descripcion, Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo) VALUES (?,?,?,?,?,?,?,?,?)", 
			(id, Descripcion, Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo))
	x = x + 1

con.commit()
cursor.close()
con.close()

os.system("rm Transformada1.csv")
os.system("rm Accidentes.db")
os.system("mv Accidentes1.db Accidentes.db")

print "Fin transformacion 1"