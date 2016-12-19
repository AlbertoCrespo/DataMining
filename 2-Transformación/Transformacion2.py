# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()

print "Clasificando marcasvalidas y marcas basura"

cursor.execute("select marca from ACCIDENTES  group by marca  having  count (marca) > 2000")

lista_marcas = []

for i in cursor:
	lista_marcas.append(str(i[0]))


print "Sustituyendo marcas validas por grupos de conocimiento..."

txt = open('marcas.txt', 'w')
txt.write("----------------------------------------------------------")
txt.write("\n")
txt.write("TABLA DE MARCAS")
txt.write("\n")
txt.write("----------------------------------------------------------")
txt.write("\n")

y = 0
z = 1
for i in lista_marcas:
	x = "UPDATE ACCIDENTES SET marca = '"+str(y)+"'  WHERE marca == '"+str(i)+"'"
	txt.write(""+str(i)+"-Numero:"+str(y))
	txt.write("\n")
	cursor.execute(x)
	con.commit()
	cursor.execute("INSERT INTO Marca (id, marca, numero_marca) VALUES (?,?,?)",(str(z),str(i),str(y)))
	con.commit()
	y = y + 1
	z = z + 1

txt.write("----------------------------------------------------------")
txt.write("\n")
txt.close()

print "Elimnando modelos basura..."
cursor.execute("delete from accidentes where marca not in( select distinct marca from accidentes where marca GLOB  '[0-9]' or marca GLOB '[0-9][0-9]' or marca GLOB '[0-9][0-9][0-9]')")
con.commit()


con.commit()
cursor.close()
con.close()

print "Fin transformacion 2"