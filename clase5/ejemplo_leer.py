# -*- coding windows-1252 -*-

import io

#fichero = open("quijote_pg2000.txt", 'r')
#for linea in fichero:
#	print(linea)
#fichero.close()

#with open("quijote_pg2000.txt", 'r') as fichero:
#	contenido = fichero.read(200)
#	print(contenido)

with open("quijote_pg2000.txt", 'r') as fichero:
	contenido = fichero.readlines(2000)
	for c in contenido:
		print(c.strip())