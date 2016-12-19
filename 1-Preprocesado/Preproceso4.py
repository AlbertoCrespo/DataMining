# -*- coding: utf-8 -*-

import sqlite3
import os
import csv


def MarcaValida(marca,marcas):
	x = marca in marcas
	return x


print "Preparando estandarizacion de los datos"
con = sqlite3.connect('Accidentes.db')
cursor = con.cursor()

print "Estandarizando marca TOYOTA"
cursor.execute("UPDATE ACCIDENTES SET Marca='TOYOTA' WHERE  Marca LIKE '%TOY%'")
print "Estandarizando marca HONDA"
cursor.execute("UPDATE ACCIDENTES SET Marca='HONDA' WHERE  Marca LIKE '%HON%'")
print "Estandarizando marca NISSAN"
cursor.execute("UPDATE ACCIDENTES SET Marca='NISSAN' WHERE  Marca LIKE '%NIS%'")
print "Estandarizando marca FORD"
cursor.execute("UPDATE ACCIDENTES SET Marca='FORD' WHERE  Marca LIKE '%FORD%'")
print "Estandarizando marca CHEVROLET"
cursor.execute("UPDATE ACCIDENTES SET Marca='CHEVROLET' WHERE  Marca LIKE '%CHE%'")
print "Estandarizando marca HYUNDAI"
cursor.execute("UPDATE ACCIDENTES SET Marca='HYUNDAI' WHERE  Marca LIKE '%HYU%'")
print "Estandarizando marca MERCEDES"
cursor.execute("UPDATE ACCIDENTES SET Marca='MERCEDES' WHERE  Marca LIKE '%MER%'")
print "Estandarizando marca DODGE"
cursor.execute("UPDATE ACCIDENTES SET Marca='DODGE' WHERE  Marca LIKE '%DOD%'")
print "Estandarizando marca VOLKSWAGEN"
cursor.execute("UPDATE ACCIDENTES SET Marca='VOLKSWAGEN' WHERE  Marca LIKE 'VOLK%'")
print "Estandarizando marca VOLKSWAGEN"
cursor.execute("UPDATE ACCIDENTES SET Marca='VOLKSWAGEN' WHERE  Marca LIKE 'VW%'")
print "Estandarizando marca VOLVO"
cursor.execute("UPDATE ACCIDENTES SET Marca='VOLVO' WHERE  Marca LIKE 'VOLV%'")
print "Estandarizando marca MAZDA"
cursor.execute("UPDATE ACCIDENTES SET Marca='MAZDA' WHERE  Marca LIKE '%MAZ%'")
print "Estandarizando marca CADILLAC"
cursor.execute("UPDATE ACCIDENTES SET Marca='CADILLAC' WHERE  Marca LIKE '%CAD%'")
print "Estandarizando marca SUBARU"
cursor.execute("UPDATE ACCIDENTES SET Marca='SUBARU' WHERE  Marca LIKE '%SUB%'")
print "Estandarizando marca INFINITI"
cursor.execute("UPDATE ACCIDENTES SET Marca='INFINITI' WHERE  Marca LIKE '%INF%'")
print "Estandarizando marca LEXUS"
cursor.execute("UPDATE ACCIDENTES SET Marca='LEXUS' WHERE  Marca LIKE '%LEX%'")
print "Estandarizando marca ACURA"
cursor.execute("UPDATE ACCIDENTES SET Marca='ACURA' WHERE  Marca LIKE '%ACU%'")
print "Estandarizando marca PONTIAC"
cursor.execute("UPDATE ACCIDENTES SET Marca='PONTIAC' WHERE  Marca LIKE '%PON%'")
print "Estandarizando modelo 2 DOOR"
cursor.execute("UPDATE ACCIDENTES SET modelo='2 DOOR' WHERE  modelo LIKE '2 do%' or modelo like '2-D%'")
print "Estandarizando modelo TOWN & COUNTRY"
cursor.execute("UPDATE ACCIDENTES SET modelo='TOWN & COUNTRY' WHERE  modelo LIKE 'town%y'or modelo like 't%countr'")
print "Estandarizando modelo TOWN CAR"
cursor.execute("UPDATE ACCIDENTES SET modelo='TOWN CAR' WHERE  modelo LIKE 'town%car%'")
print "Estandarizando modelo 4 DOOR"
cursor.execute("UPDATE ACCIDENTES SET modelo='4 DOOR'WHERE  modelo LIKE '4D%' or modelo like '4dr' or modelo like '4 dr%'or modelo like '4DOOR' or modelo like '4-DOOR%' or modelo like '4 DOOR%'")
print "Estandarizando modelo PU"
cursor.execute("UPDATE ACCIDENTES SET modelo='PU' WHERE modelo like 'P%U'")
print "Estandarizando modelo COROLLA"
cursor.execute("UPDATE ACCIDENTES SET modelo='COROLLA' WHERE  modelo LIKE 'cor%a%'")
print "Estandarizando modelo TRCUK"
cursor.execute("UPDATE ACCIDENTES SET modelo='DUMP TRUCK' WHERE  modelo LIKE 'DUM%'")
print "Estandarizando modelo CAMRY 4S"
cursor.execute("UPDATE ACCIDENTES SET modelo='CAMRY 4S' WHERE  modelo LIKE 'CAMRY%'or modelo LIKE 'CAMARY'")
print "Estandarizando modelo PRIZM"
cursor.execute("UPDATE ACCIDENTES SET modelo='PRIZM' WHERE  modelo LIKE 'PRISM%'or modelo LIKE 'PRIZM%'")
print "Estandarizando modelo ALTIMA"
cursor.execute("UPDATE ACCIDENTES SET modelo='ALTIMA' WHERE  modelo LIKE 'ALTIMA%'")
print "Estandarizando modelo 2S"
cursor.execute("UPDATE ACCIDENTES SET modelo='2S' WHERE  modelo LIKE '2S%'")
print "Estandarizando modelo VN"
cursor.execute("UPDATE ACCIDENTES SET modelo='VN' WHERE  modelo LIKE 'VN%'")
print "Estandarizando modelo 3"
cursor.execute("UPDATE ACCIDENTES SET modelo='3' WHERE  modelo LIKE 'MAZDA%3%'")
print "Estandarizando modelo 5"
cursor.execute("UPDATE ACCIDENTES SET modelo='5' WHERE  modelo LIKE 'MAZDA%5%'")
print "Estandarizando modelo 6"
cursor.execute("UPDATE ACCIDENTES SET modelo='6' WHERE  modelo LIKE 'MAZDA%6%'")
cursor.execute("UPDATE ACCIDENTES SET Localizacion='MIDDLEBROOK RD AT GERMANTOWN RD' WHERE id=771337")
			

con.commit()
cursor.close()
con.close()


