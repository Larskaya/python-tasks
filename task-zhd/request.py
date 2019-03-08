class Request:
	def __init__(self, end_station, time, date):
		self.station = end_station
		self.time = time
		self.date = date

	def __repr__(self):
		return 'Request' + ', end stations:' + str(self.station) + ', time:' + str(self.time) + ', date:' + str(self.date)