from request import *

class Passenger:
	def __init__(self, travel_settings, cashier, money):
		self.money = money
		self.travel_settings = travel_settings
		self.cashier = cashier

	def request_train(self):
		request = Request(self.travel_settings)
		self.trains = self.cashier.processing(request)

	def choose_and_buy_the_train(self):
		if len(self.trains) > 0:
			train = self.trains[0]
			money = self.cashier.sell(train, self)
			print('for sell', money)
			if money < self.money:
				self.money -= money
				print('passenger balance after', self.money)
			



		

			