class Link:

	links = []
	whole_link = []

	def find_first_letter(self, sym):
		lst = []
		for link in self.links:
			if sym == link[0]:
				lst.append(link)
		return lst

	def find_second_letter(self, sym):
		lst = []
		for link in self.links:
			if sym == link[1]:
				lst.append(link)
		return lst

	def test(self, new_link):
		a = self.find_first_letter(new_link[0])
		b = self.find_second_letter(new_link[1])
		if a and b:
			for el in a:
				self.whole_link.append(el)
			for el in b:
				self.whole_link.append(el)
		for link in self.whole_link:
			if new_link[1] in link:
				return False
		return True

	def add_link(self, new_link):
		if self.test(new_link):
			self.links.append(new_link)

	def show(self):
		return self.links

l = Link()
l.add_link(('a', 'b'))
l.add_link(('b', 'c'))
l.add_link(('c', 'k'))
l.add_link(('k', 'l'))
l.add_link(('l', 'm'))
l.add_link(('a', 'm'))
print(l.show())









