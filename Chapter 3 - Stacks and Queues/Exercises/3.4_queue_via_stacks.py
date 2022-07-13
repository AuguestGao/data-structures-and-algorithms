# import class
import sys
sys.path.insert(1, '../Basics')
from stack import Stack

class QueueBy2Stacks(Stack):
	def __init__(self):
		self.s1 = []
		self.s2 = []
	
	def enqueue(self, value):
		while len(self.s2):
			value1 = self.s2.pop(0)
			self.s1.append(value1)
		self.s1.append(value)
		while len(self.s1):
			value2 = self.s1.pop(0)
			self.s2.append(value2)
	
	def dequeue(self):
		self.s2.pop(0)
	
	def __repr__(self):
		display = ''
		for i in range(len(self.s2)):
			display += f', {self.s2[i]}'
		return display[2:]
	
	
if __name__ == '__main__':
	q = QueueBy2Stacks()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q)
	q.dequeue()
	print(q)
	q.enqueue(4)
	print(q)
	q.dequeue()
	print(q)
	q.enqueue(5)
	print(q)
	q.dequeue()
	print(q)
	