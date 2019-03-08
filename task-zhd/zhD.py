from score import *
from train import *
from request import *
from cashier import *
from passenger import *

all_trains = []

number_first_train = '1A'
number_second_train = '2B'
number_third_train = '3B'

numbers_of_trains = []
numbers_of_trains.append(number_first_train)
numbers_of_trains.append(number_second_train)
numbers_of_trains.append(number_third_train)

stations1 = ['a', 'b', 'c']
stations2 = ['a', 'c']
stations3 = ['b', 'c']

t1 = Train(number_first_train, stations1)
t2 = Train(number_second_train,stations2 )
t3 = Train(number_third_train, stations3)

all_trains.append(t1)
all_trains.append(t2)
all_trains.append(t3)

start = 'a'
end = 'c'
money = 5
p = Passenger(money, start, end, '15:10', '10.05.20')
p.apply()

def find_all_need_trains(all_trains, start_station, end_station):
	print('all trains', all_trains)
	for train in all_trains:
		if start_station in train.stations and end_station in train.stations:
			all_need_trains.append(train)
	return all_need_trains

all_need_trains = []
all_need_trains = find_all_need_trains(all_trains, start, end)

def get_intermediate_stations(trains, start, end): # промежуточные станции
	intermediate_stations = []
	for train in trains:
		stations = []
		start_index = train.stations.index(start)
		end_index = train.stations.index(end)
		counter = start_index + 1
		while counter < end_index:
			stations.append(train.stations[counter])
			counter += 1
		intermediate_stations.append(stations)
	return intermediate_stations

intermediate_stations = get_intermediate_stations(all_need_trains, start, end)
print('num of trains - >', numbers_of_trains)
print('need trains - >', all_need_trains)
print('intermediate_stations - >', intermediate_stations)

def get_options(all_need_trains, all_prices):
	trains_with_prices = []
	counter = 0
	while counter < len(all_need_trains):
		d = { all_need_trains[counter].number_of_train: [all_prices[counter], intermediate_stations[counter]] }
		trains_with_prices.append(d)
		counter += 1
	return trains_with_prices


c = Cashier(numbers_of_trains, intermediate_stations, end)

all_prices = c.get_price()
all_options = get_options(all_need_trains, all_prices)

option = p.choose_a_train(all_options)
print(option)
passenger_score = c.give_the_score(option)
print(p.pay(passenger_score))

#Пассажир делает заявку на станцию назначения, время и дату поездки. Система регистрирует Заявку и осуществляет поиск соответствующего Поезда.
#Пассажир делает выбор Поезда и получает Cчет на оплату. Кассир вводит номера Поездов, промежуточные и конечные станции, цены.





