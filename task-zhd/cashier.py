from score import *

class Cashier:
	def __init__(self, numbers_of_trains, stations, end_station):
		self.numbers_of_trains = numbers_of_trains
		self.stations = stations
		self.end_station = end_station

	def get_price(self):
		all_prices = []
		for intermediate_station in self.stations:
			price = len(intermediate_station) + 1
			all_prices.append(price)
		print('all prices', all_prices)
		return all_prices

	def give_the_score(self, option):
		keys = option.keys()
		for key in keys:
			price = option[key]
		return Score(price)
