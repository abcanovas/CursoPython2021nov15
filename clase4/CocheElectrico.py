from Coche import Coche

#Herencia: extendiendo la clase
class CocheElectrico(Coche):
	# El método __init__() para crear una clase hija
	def __init__(self, marca, modelo, tipo):
		super().__init__(marca, modelo, tipo)
		self.battery_size = 100
		self.charge_level = 0

	# Agregar un nuevo método a la clase
	def cargar(self):
		self.nivel_carga = 100
		print('El coche está cargado.')

	# Sobrescribir un método del padre
	def gasolina_completo(self):
		print('El coche no tiene depósito de gasolina!')

# Usar el método padre e hijo
coche_electrico = CocheElectrico('Tesla', 'Modelo 3', 'Berlina')
print(coche_electrico.modelo)
coche_electrico.cargar()
coche_electrico.conducir()

# Mostrar la o las clases de la cual se está heredando
print(CocheElectrico.__mro__)