import sqlite3
import os
import csv



print "Creando base de datos Accidentes.db"

con = sqlite3.connect('Accidentes.db')
con.text_factory = str
cursor = con.cursor()



lista_descripciones = []
cursor.execute("SELECT Descripcion FROM CLUSTER")

for i in cursor:
	lista_descripciones.append(str(i[0]))

for i in lista_descripciones:
	x = "SELECT descripciones FROM Descripciones WHERE numero_descripcion == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Descripcion = '"+str(j[0])+"'  WHERE Descripcion == '"+str(i)+"'")
		con.commit()




lista_vehiculocomercial = []
cursor.execute("SELECT Vehi_Comercial FROM CLUSTER")

for i in cursor:
	lista_vehiculocomercial.append(str(i[0]))

for i in lista_vehiculocomercial:
	x = "SELECT vehiculo_comercial FROM vehiculocomercial WHERE numero_vehiculo_comercial == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Vehi_Comercial = '"+str(j[0])+"'  WHERE Vehi_Comercial == '"+str(i)+"'")
		con.commit()



lista_tipovehiculo = []
cursor.execute("SELECT Tipo_de_Vehiculo FROM CLUSTER")

for i in cursor:
	lista_tipovehiculo.append(str(i[0]))

for i in lista_tipovehiculo:
	x = "SELECT tipo_vehiculo FROM tipovehiculo WHERE numero_tipo_vehiculo == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Tipo_de_Vehiculo = '"+str(j[0])+"'  WHERE Tipo_de_Vehiculo == '"+str(i)+"'")
		con.commit()


lista_marca = []
cursor.execute("SELECT Marca FROM CLUSTER")

for i in cursor:
	lista_marca.append(str(i[0]))

for i in lista_marca:
	x = "SELECT marca FROM Marca WHERE numero_marca == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Marca = '"+str(j[0])+"'  WHERE Marca == '"+str(i)+"'")
		con.commit()


lista_modelo = []
cursor.execute("SELECT Modelo FROM CLUSTER")

for i in cursor:
	lista_modelo.append(str(i[0]))

for i in lista_modelo:
	x = "SELECT modelo FROM Modelo WHERE numero_modelo == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Modelo = '"+str(j[0])+"'  WHERE Modelo == '"+str(i)+"'")
		con.commit()




lista_tipoarresto = []
cursor.execute("SELECT Tipo_Arresto FROM CLUSTER")

for i in cursor:
	lista_tipoarresto.append(str(i[0]))

for i in lista_tipoarresto:
	x = "SELECT tipo_arresto FROM tipoarresto WHERE numero_tipo_arresto == '"+str(i)+"'"
	cursor.execute(str(x))
	for j in cursor:
		cursor.execute("UPDATE CLUSTER SET Tipo_Arresto = '"+str(j[0])+"'  WHERE Tipo_Arresto == '"+str(i)+"'")
		con.commit()




archivo=open ("Final.csv","a")
archivo.write("Descripcion,Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo, Ocurrencias, Grupo")
archivo.write("\n")

cursor.execute("SELECT Descripcion,Vehi_Comercial, Tipo_de_Vehiculo, Anio, Marca, Modelo, Tipo_Arresto, Riesgo, Ocurrencias, Grupo FROM CLUSTER")

for i in cursor:
	archivo.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8])+","+str(i[9]))
	archivo.write("\n")


archivo.close()
cursor.close()
con.close()



