def preguntar_numero():
	numero = input('Di un numero')
	return int(numero)

def calcular_par_impar(numero):
	if numero % 4 == 0:
		print('El numero ', numero, ' es multiplo de 4')
	elif numero % 2 == 0:
		print('El numero ', numero, ' es par')
	else:
		print('El numero ', numero, ' es impar')

numero = preguntar_numero()
calcular_par_impar(numero)

