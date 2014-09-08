
class tQueue(object):
	
	def __init__(self):
		self.size = 0
		self.q = [-1]*48
		self.head = 0
		self.tail = 0
	
	def put(self, item):
		self.q[self.tail] = item
		self.size += 1
		self.tail += 1

	def get(self):
		item = self.q[self.head]
		self.q[self.head] = -1
		self.head = self.head + 1
		if self.head == 48:
			self.head = 0
		self.size -= 1
		return item

	def copy(self, other):
		self.size = other.size
		self.head = other.head
		self.tail = other.tail
		i = 0
		self.q = other.q[:]

	def printQ(self):
		print self.q

	def getSize(self):
		return self.size
