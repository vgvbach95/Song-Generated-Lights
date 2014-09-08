from tQueue import tQueue

class Ring:
	
	def __init__(self, number):				
		self.collected = [False]*48
		self.currRing = tQueue()
		self.currRing.put(number)
		self.collected[number] = True
		self.done = False

	def getRing(self):
		toReturn = tQueue()
		toReturn.copy(self.currRing)
		return toReturn 

	def isDone(self):
		return self.done
	
	def ringSize(self):
		return self.currRing.getSize()
	
	def advanceRing(self):
		length = self.currRing.getSize()
		if length == 0:
			self.done = True
		while length != 0:
			currNumber = self.currRing.get()
			length -= 1
			if (currNumber+1)%6 != 0 and self.collected[currNumber+1] == False:
				self.currRing.put(currNumber+1)
				self.collected[currNumber+1] = True
	
			if (currNumber-1)%6 != 5 and self.collected[currNumber-1] == False:
				self.currRing.put(currNumber-1)
				self.collected[currNumber-1] = True
	
			if currNumber+6 < 48 and self.collected[currNumber+6] == False:
				self.currRing.put(currNumber+6)
				self.collected[currNumber+6] = True
	
			if currNumber-6 > -1 and self.collected[currNumber-6] == False:
				self.currRing.put(currNumber-6)
				self.collected[currNumber-6] = True
		
		

	def prevRings(self):
		prev = tQueue()
		i = 0
		while i != 48:
			if self.collected[i] == True:
				prev.put(i)
			i +=1
		return prev
