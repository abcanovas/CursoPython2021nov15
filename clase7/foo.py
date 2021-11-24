import math

print('Antes del import')

print('Antes de la funcion a')

def funcionA():
	print('Funcion A')

print('Antes de la funcion b')

def funcionB():
	"""
	docstring
	"""
	print('Función B: {}'.format(math.sqrt(100)))

print('Antes del control __name__')
if __name__ ==  '__main__':
	funcionA()
	funcionB()
print('Despues del control __name__')