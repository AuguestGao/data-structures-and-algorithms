"""
Implement SetOfStacks to automatically create a new stack when the old stack reaches a limit

Contains a follow up question
"""

class SetOfStacks:
	def __init__(self, size=2):
		self.arrays = []
		self.arrIndex = None
		self.size = size
		
		
	def push(self, value):
		if not self.arrays:
			self.arrays.append([value])
			self.arrIndex = 0
		else:
			if len(self.arrays[self.arrIndex]) < self.size:
				self.arrays[self.arrIndex].append(value)
			else:
				self.arrays.append([value])
				self.arrIndex += 1
	
	def pop(self):
		self.arrays[self.arrIndex].pop()
		if not self.arrays[self.arrIndex]:
			self.arrays.pop()
			self.arrIndex -= 1
	
	def __repr__(self):
		display = ''
		for a in self.arrays:
			line = ''
			for e in a:
				line += f', {e}'
			display += f'{line[2:]} \n'
		return display
		
	def popAt(self, idx):
		if idx == self.arrIndex:
			self.pop()
			self.arrIndex -= 1
			return 0;
		
		self.arrays[idx].pop()

		idx += 1
		while idx < len(self.arrays):
			self.arrays[idx-1].append(self.arrays[idx][0])
			if len(self.arrays[idx]) == 1:
				self.arrays.pop()
				self.arrIndex -= 1
			else:
				self.arrays[idx] = self.arrays[idx][1:]
			idx += 1
			
		
if __name__ == '__main__':
	s = SetOfStacks(3)
	for i in range(10):
		s.push(i)
	print(s)
	
	s.popAt(1)
	print(s)
	
	