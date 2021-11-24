import os
import shutil
import pandas as pd


"""
#Crear el/los scripts correspondientes para:
#1.- Crear una copia y luego convertir el fichero .csv a .tsv
#2.- Crear un directorio y mover la copia del fichero .csv dentro
#3.- Escribir en un nuevo fichero las primeras 100 líneas del fichero .tsv 
#4.- Exportar las primeras 5 columnas del fichero en formato .xlsx a un nuevo fichero.
"""

#Punto 1 Copiar
shutil.copy(src='01001c.csv', dst='copia01001c.csv')

#fichero_path = 'nuevoDir'
#if not fichero_path.exists():
#    os.makedirs(fichero_path)

shutil.move(src='copia01001c.csv', dst='./nuevoDir/copia01001c.csv')

with open("./nuevoDir/copia01001c.csv", 'r') as fichero:
	contenido = fichero.readlines(100)
	for c in contenido:
		print(c.strip())


fichero_csv = "'./nuevoDir/copia01001c'.csv"
escribir_csv = "'./nuevoDir/nuevoCsv'.csv"

leer_csv = pd.read_csv(fichero_csv, encoding="ISO-8859-1")

with open(escribir_csv, 'w') as write_csv:
	write_csv.write(leer_csv.head(10).to_csv(sep=',', index=False))


