# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()

print "Clasificando modelosvalidos y modelos basura"
cursor.execute("select modelo from accidentes group by modelo having count(modelo)>200 order by count(modelo) desc")

lista_modelos = []

for i in cursor:
	lista_modelos.append(str(i[0]))


print("Sustituyendo modelos validos por grupos de conocimiento...")
txt = open('modelos.txt', 'w')
txt.write("----------------------------------------------------------")
txt.write("\n")
txt.write("TABLA DE MODELOS")
txt.write("\n")
txt.write("----------------------------------------------------------")
txt.write("\n")

y = 0
z = 0
for i in lista_modelos:
	x = "UPDATE ACCIDENTES SET modelo = '"+str(y)+"'  WHERE modelo == '"+str(i)+"'"
	txt.write(""+str(i)+"-Numero:"+str(y))
	txt.write("\n")
	cursor.execute(x)
	con.commit()
	cursor.execute("INSERT INTO Modelo (id, modelo, numero_modelo) VALUES (?,?,?)", (str(z),str(i),str(y)))
	con.commit()
	y = y + 1
	z = z + 1

txt.write("----------------------------------------------------------")
txt.write("\n")

txt.close()
con.commit()

print "Elimnando modelos basura..."
cursor.execute("delete from accidentes where modelo not in( select distinct modelo from accidentes where modelo GLOB  '[0-9]' or modelo GLOB '[0-9][0-9]' or modelo GLOB '[0-9][0-9][0-9]')")

con.commit()

cursor.close()
con.close()

print "Fin transformacion 3"