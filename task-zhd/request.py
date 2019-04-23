class Request:
	def __init__(self, travel_settings):
		self.travel_settings = travel_settings

	def __repr__(self):
		return 'Request' + str(self.travel_settings['start_st']) + str(self.travel_settings['end_st'])