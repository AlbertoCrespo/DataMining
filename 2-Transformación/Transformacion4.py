# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()

tipo_arresto = []

cursor.execute("select distinct Tipo_Arresto from ACCIDENTES")

for i in cursor:
	tipo_arresto.append(str(i[0]))


print "Sustituyendo Tipos Arresto validos por grupos de conocimiento..."
txt = open('tipoarresto.txt', 'w')
txt.write("----------------------------------------------------------")
txt.write("\n")
txt.write("TABLA DE TIPO DE ARRESTO")
txt.write("\n")
txt.write("----------------------------------------------------------")
txt.write("\n")

y = 0
z = 0
for i in tipo_arresto:
	x = "UPDATE ACCIDENTES SET Tipo_Arresto = '"+str(y)+"'  WHERE Tipo_Arresto == '"+str(i)+"'"
	txt.write(""+str(i)+"-Numero:"+str(y))
	txt.write("\n")
	cursor.execute(x)
	con.commit()
	cursor.execute("INSERT INTO tipoarresto (id, tipo_arresto, numero_tipo_arresto) VALUES (?,?,?)", (str(z),str(i),str(y)))
	con.commit()
	y = y + 1
	z = z + 1


txt.write("----------------------------------------------------------")
txt.write("\n")
txt.close()

con.commit()

tipo_vehiculo = []

cursor.execute("select distinct Tipo_de_Vehiculo from ACCIDENTES")

for i in cursor:
	tipo_vehiculo.append(str(i[0]))


print "Sustituyendo Tipos Vehiculo validos por grupos de conocimiento..."
txt = open('tipovehiculo.txt', 'w')
txt.write("----------------------------------------------------------")
txt.write("\n")
txt.write( "TABLA DE TIPO DE VEHICULO")
txt.write("\n")
txt.write("----------------------------------------------------------")
txt.write("\n")

y = 0
z = 0
for i in tipo_vehiculo:
	x = "UPDATE ACCIDENTES SET Tipo_de_Vehiculo = '"+str(y)+"'  WHERE Tipo_de_Vehiculo == '"+str(i)+"'"
	txt.write(""+str(i)+"-Numero:"+str(y))
	txt.write("\n")
	cursor.execute(x)
	con.commit()
	cursor.execute("INSERT INTO tipovehiculo (id, tipo_vehiculo, numero_tipo_vehiculo) VALUES (?,?,?)", (str(z),str(i),str(y)))
	con.commit()
	y = y + 1
	z = z + 1

txt.write("----------------------------------------------------------")
txt.write("\n")

txt.close()

con.commit()


vehiculo_comercial = []

cursor.execute("select distinct Vehi_Comercial from ACCIDENTES")

for i in cursor:
	vehiculo_comercial.append(str(i[0]))


print "Sustituyendo vehiculo_comercial validos por grupos de conocimiento..."
txt = open('vehiculocomercial.txt', 'w')
txt.write("----------------------------------------------------------")
txt.write("\n")
txt.write("TABLA DE VEHICULO COMERCIAL")
txt.write("\n")
txt.write( "----------------------------------------------------------")
txt.write("\n")

y = 0
z = 0
for i in vehiculo_comercial:
	x = "UPDATE ACCIDENTES SET Vehi_Comercial = '"+str(y)+"'  WHERE Vehi_Comercial == '"+str(i)+"'"
	txt.write(""+str(i)+"-Numero:"+str(y))
	txt.write("\n")
	cursor.execute(x)
	con.commit()
	cursor.execute("INSERT INTO vehiculocomercial (id, vehiculo_comercial, numero_vehiculo_comercial) VALUES (?,?,?)", (str(z),str(i),str(y)))
	con.commit()
	y = y + 1
	z = z + 1

txt.write("----------------------------------------------------------")
txt.write("\n")

txt.close()

con.commit()

cursor.close()
con.close()

print "Fin transformacion 4"