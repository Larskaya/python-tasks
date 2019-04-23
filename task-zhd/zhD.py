from score import *
from train import *
from request import *
from cashier import *
from passenger import *

all_trains = []

t1 = Train('1A', [ 
	{ 'station': 'msk', 'date': '15.12.2016', 'time': '15:10', 'cost': '0' }, 
	{ 'station': 'blg', 'date': '15.12.2016', 'time': '15:40', 'cost': '300' },
	{ 'station': 'rst', 'date': '15.12.2016', 'time': '16:25', 'cost': '650' },
	{ 'station': 'spb', 'date': '15.12.2016', 'time': '17:10', 'cost': '450' }] )

t2 = Train('2B', [
	{ 'station': 'msk', 'date': '20.01.2017', 'time': '12:00', 'cost': '0' },
	{ 'station': 'reu', 'date': '20.01.2017', 'time': '13:15', 'cost': '750' }, 
	{ 'station': 'zhl', 'date': '20.01.2017', 'time': '14:05', 'cost': '500' }, 
 	{ 'station': 'vld', 'date': '20.01.2017', 'time' :'15:30', 'cost': '850' } ])

t3 = Train('3B', [
	{ 'station': 'msk', 'date': '01.02.2017', 'time': '18:10', 'cost': '0' },
	{ 'station': 'zhl', 'date': '01.02.2017', 'time': '19:30', 'cost': '800' }])

all_trains.append(t1)
all_trains.append(t2)
all_trains.append(t3)

cashierObj = Cashier(all_trains)
passengerObj = Passenger( {'name': 'alex', 'start_st': 'msk', 'end_st': 'rst', 'time': '15:10', 'date': '15.12.2016'}, cashierObj, 1500)
passengerObj.request_train()
passengerObj.choose_and_buy_the_train()



