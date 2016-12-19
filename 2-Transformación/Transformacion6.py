# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()


cursor.execute("SELECT descripcion, vehi_comercial, tipo_de_vehiculo, anio, marca, modelo, tipo_arresto, riesgo, count(*) as Ocurrencias from accidentes group by descripcion, vehi_comercial, tipo_de_vehiculo, anio, marca, modelo, tipo_arresto, riesgo having Ocurrencias > 6 ")

archivo=open ("BD.csv","a")
archivo.write("Descripcion,Vehi_Comercial,Tipo_de_Vehiculo,Anio,Marca,Modelo,Tipo_Arresto,Riesgo,Ocurrencias")
archivo.write("\n")

for i in cursor:
	archivo.write(str(i[0])+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[7])+","+str(i[8]))
	archivo.write("\n")

archivo.close()

cursor.close()
con.close()