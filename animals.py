from abc import ABC, abstractmethod

class Animal(ABC):

	animals = []

	@staticmethod
	def byFood_key(animal):
		return animal.amount_food

	@staticmethod
	def byName_key(animal):
		return animal.name

	@staticmethod
	def animals_sort():
		Animal.animals.sort(key = Animal.byName_key)
		print('animals', Animal.animals)
		Animal.animals.sort(key = Animal.byFood_key, reverse = True)
		print('animals', Animal.animals)
		for an in Animal.animals:
			print(an.name)


	@abstractmethod
	def amount_and_type_of_food(self):
		pass

class Tiger(Animal):
	def __init__(self, name, amount_food, type_food): # predator
		self.name = name
		self.amount_food = amount_food
		self.type_food = type_food
		Animal.animals.append(self)

	def amount_and_type_of_food(self):
		super().amount_and_type_of_food()
		print('1')

	def __repr__(self):
		return str(self.amount_food)

class Man(Animal):
	def __init__(self, name, amount_food, type_food): # omnivorous
		self.name = name
		self.amount_food = amount_food
		self.type_food = type_food
		Animal.animals.append(self)

	def amount_and_type_of_food(self):
		pass

class Kangaroo(Animal):
	def __init__(self, name, amount_food, type_food): # herbivorous
		self.name = name
		self.amount_food = amount_food
		self.type_food = type_food
		Animal.animals.append(self)

	def amount_and_type_of_food(self):
		pass

	def __repr__(self):
		return str(self.amount_food)

t = Tiger('krolek', 5, 'predator')
k1 = Kangaroo('anek', 3, 'herbivorous')
k2 = Kangaroo('nek', 4, 'herbivorous')
k3 = Kangaroo('bnek', 3, 'herbivorous')

print(Animal.animals_sort())
#t.amount_and_type_of_food()

