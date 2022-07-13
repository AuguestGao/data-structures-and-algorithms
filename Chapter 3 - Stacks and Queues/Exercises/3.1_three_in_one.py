"""
Use 1 array to implement 3 stacks
"""

class Stacks:
	def __init__(self):
		self.arr = []
		self.idx0 = -3
		self.idx1 = -2
		self.idx2 = -1
		
	def push(self, stack, value):
		if not value:
			print("invalid value")
			return None
		
		if stack == 0:
			self.idx0 += 3
			if len(self.arr) - 1 < self.idx0:
				self.arr += [None, None, None]
			self.arr[self.idx0] = value
			
		elif stack == 1:
			self.idx1 += 3
			if len(self.arr) - 1 < self.idx1:
				self.arr += [None, None, None]
			self.arr[self.idx1] = value
		elif stack == 2:
			self.idx2 += 3
			if len(self.arr) - 1 < self.idx2:
				self.arr += [None, None, None]
			self.arr[self.idx2] = value
		else:
			print('no such stack')
		return None
	
	def pop(self, stack):
		if stack == 0:
			if self.idx0 == 0:
				return "empty stack 0, nothing to pop"
			else:
				self.arr[self.idx0] = None
				self.idx0 -= 3
		elif stack == 1:
			if self.idx1 == 1:
				return "empty stack 1, nothing to pop"
			else:
				self.arr[self.idx1] = None
				self.idx1 -= 3
		elif stack == 2:
			if self.idx2 == 2:
				return "empty stack 2, nothing to pop"
			else:
				self.arr[self.idx2] = None
				self.idx2 -= 3
		else:
			return "no such stack"
		
		while self.arr[-3:] == [None, None, None]:
			self.arr = self.arr[:-3]
		
		return None;

	def __repr__(self):
		display = ''
		for i in self.arr:
			display += f', {i}'
		return display[2:]
		
	
if __name__ == "__main__":
	s = Stacks()
	s.push(0, 'a')
	s.push(0, 'a1')
	s.push(1, 'b')
	s.push(2, 'c')
	s.push(2, 'c1')
	s.push(2, 'c2')
	s.push(0, 'a2')
	s.push(0, 'a3')
	print(s)
	s.pop(0)
	print(s)
	s.pop(0)
	print(s)
	s.pop(0)
	print(s)