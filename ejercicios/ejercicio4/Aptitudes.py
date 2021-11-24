from clase_empleados import Empleado
class Aptitudes(Empleado):
	def __init__(self, nombre, num_empl, lenguaje, so, idioma):
		super().__init__(nombre, num_empl)
		self.lenguaje = lenguaje
		self.so = so
		self.idioma = idioma