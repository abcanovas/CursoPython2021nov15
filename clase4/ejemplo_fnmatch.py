import fnmatch
import os

patron = 'ejemplo*.py'
print('Patrón de búsqueda: ', patron)
print('*****')

#ficheros = os.listdir('./')
#for nombre in ficheros:
	#print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre, patron)))

ficheros = os.listdir('./')
for nombre in ficheros:
	print('Nombre: ', ficheros)
	print('Coinciden: ',fnmatch.filter(ficheros,patron))