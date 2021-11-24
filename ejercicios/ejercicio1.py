def preguntar_nombre():
	nombre = input('¿Como te llamas?')
	return nombre

def preguntar_edad():
	edad = input('¿Cuantos años tienes?')
	aniosRestantes = 100-int(edad)
	añoCentenario = aniosRestantes + 2021
	return añoCentenario

nombre = preguntar_nombre()
anio = preguntar_edad()
print('Hola', nombre, 'En el año ', anio, ' cumpliras 100')
