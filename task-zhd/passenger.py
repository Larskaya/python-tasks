from request import *

all_requests = []

class Passenger:
	def __init__(self, money, start_station, end_station, time, date):
		self.end_station = end_station
		self.time = time
		self.date = date
		self.money = money

	def apply(self):
		all_requests.append(Request(self.end_station, self.time, self.date))
		print('all requests', all_requests)

	def choose_a_train(self, all_options):
		prices_of_option = []
		print('all options', all_options)
		for option in all_options:
			keys = option.keys()
			for name in keys:
				prices_of_option.append(option[name])
		best_option = min(prices_of_option)
		return all_options[best_option]

	def pay(self, score):
		if self.money > score.price:
			self.money -= score.price
			return self.money