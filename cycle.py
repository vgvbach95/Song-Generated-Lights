from tQueue import tQueue

class Cycle:
	def __init__(self, direction):	
		self.lines = [
				[6,13,20,27,34,41],
				[1,7,14,20,27,33,40,46],
				[2,8,14,20,27,33,39,45],
				[3,9,8,15,21,26,32,38,44],
				[4,10,15,21,26,32,37,43],
				[11,16,21,26,31,36],
				[17,23,22,21,26,25,24,30],
				[35,29,28,27,20,19,18,12]
			]
		self.lineNumber = 0
		self.dir = direction #false for right, true for left
	
	def cycleAdvance(self):
		if(self.dir == False):
			self.lineNumber += 1
			if self.lineNumber == 8:
				self.lineNumber = 0
		else:
			self.lineNumber -= 1
			if self.lineNumber == -1:
				self.lineNumber = 7
	
	def currCycle(self):
		return self.lines[self.lineNumber]
	
	def prevCycle(self):
		prev = []
		for i in range(0, 7):
			if i != self.lineNumber:
				prev += self.lines[i]
		return prev
