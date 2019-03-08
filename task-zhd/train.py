class Train:
	def __init__(self, number_of_train, stations): 
		self.number_of_train = number_of_train
		self.stations = stations

	def __repr__(self):
		return str(self.number_of_train)