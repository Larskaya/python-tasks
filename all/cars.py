class Car:
	def __init__(self, wheels, color, engine_type):
		self.wheels = wheels
		self.color = color
		self.engine_type = engine_type

	@staticmethod
	def print(self):
		return f'ололо транспорт - сила'

	def buzz(self):
		print('to buzz')

	def go(self):
		print('to go')

	@classmethod
	def special_method1(cls):
		cls.color = 'red'
		cls.engine_type = 'petrol'
		print( f'Car({cls.color}, {cls.engine_type})' )


	@classmethod
	def special_method2(cls):
		cls.color = 'green'
		cls.engine_type = 'electric'
		print(f'Car({cls.color}, {cls.engine_type})')


#c1 = Car(4, 'yellow', 'electric')
Car.special_method1()

#c2 = Car(2, 'black', 'electric')
Car.special_method2()
#c1.go('c1')

