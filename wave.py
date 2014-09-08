from tQueue import tQueue

class Wave:
	def __init__(self, direction):	
		self.lines = [
				[0,7,14,15,22,29,35,40,45,44],
				[0,6,13,20,21,28,35,41,46],
				[1,6,12,19,26,27,34,41,47],
				[3,2,7,12,18,25,32,33,40,47],
				[4,9,8,13,18,24,31,38,39,46],
				[5,10,15,14,19,24,30,37,44,45],
				[5,11,16,21,20,25,30,36,43],
				[4,11,17,22,27,26,31,36,42],
				[2,3,10,17,23,28,33,32,37,42],
				[1,8,9,16,23,29,34,39,38,43]
			]
		self.lineNumber = 0
		self.dir = direction 
	
	def advanceWave(self):
		if dir == True:
			self.lineNumber += 1
			if self.lineNumber == 10:
				self.lineNumber = 0
		else:
			self.lineNumber -= 1
			if self.lineNumber == -1:
				self.lineNumber = 9
	
	def currWave(self):
		return self.lines[self.lineNumber]
	
	def prevWave(self):
		prev = []
		for i in range(0, 9):
			if i != self.lineNumber:
				prev += self.lines[i]
		return prev
