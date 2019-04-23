from score import *

class Cashier:
	def __init__(self, trains):
		self.trains = trains

	def get_price(self, stations):
		all_prices = []
		for intermediate_station in stations:
			price = len(intermediate_station) + 1
			all_prices.append(price)
		return all_prices

	def give_the_score(self, option):
		print(option)
		keys = option.keys()
		for key in keys:
			price = option[key][0]
		return Score(price)


	def get_intermediate_stations(self, trains, start, end): 
		intermediate_stations = []
		for train in trains:
			stations = []
			start_index = train.stations.index(travel_settings['start_st'])
			end_index = train.stations.index(travel_settings['end_st'])
			counter = start_index + 1

			while counter < end_index:
				stations.append(train.stations[counter])
				counter += 1
			intermediate_stations.append(stations)
		return intermediate_stations


	def processing(self, request):
		all_need_trains = []
		print('request', request.travel_settings)
		for train in self.trains:
			ls = []
			for station in train.stations:
				if station['station'] == request.travel_settings['start_st']:
					ls.append('start')
				elif station['station'] == request.travel_settings['end_st']:
					ls.append('end')
			if ls == ['start', 'end']:
				all_need_trains.append(train)

		ls = []
		for train in all_need_trains:
			for train2 in self.trains:
				if train == train2:
					for station in train2.stations:
						if station['date'] == request.travel_settings['date'] and station['time'] == request.travel_settings['time']:
							ls.append(train2)
		return ls

	def sell(self, train, passenger):
		counter = 0
		need_money = 0
		while counter < len(train.stations):
			if train.stations[counter]['station'] == passenger.travel_settings['start_st']:
				start_station_index = counter
			elif train.stations[counter]['station'] == passenger.travel_settings['end_st']:
				end_station_index = counter
			counter += 1

		if start_station_index < end_station_index:
			counter = start_station_index
			while counter <= end_station_index:
				need_money += int(train.stations[counter]['cost'])
				counter += 1
		return need_money
		




						
		







