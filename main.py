class Calculadora:
	def somar(self, v0, v1):
		return v0 + v1
	
	def subtrair(self, x, y):
		return x - y
	
	def multiplicar(self, x, y):
		return x * y
	
	def dividir(self, x, y):
		return x / y
	
	def exponenciar(self, x, y):
		return x ** y
	
	def modulo(self, x, y):
		return x % y


class Somar:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.somar(v0, v1)


class Subtrair:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.subtrair(v0, v1)


class Dividir:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.dividir(v0, v1)


class Exponenciar:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.exponenciar(v0, v1)


class Multiplicar:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.somar(v0, v1)


class Modulo:
	def __init__(self, calc, v0, v1):
		self.calc = calc
		
	def execute(self):
		self.calc.somar(v0, v1)
	