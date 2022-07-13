"""
Add a method to Stack data structure that allows it to return the min value in the stack
Ensure push, pop, and min to have O(1) time
"""


class Node:
	def __init__(self, value):
		self.value = value
		self.stackMin = None
		
		
class Stack:
	def __init__(self):
		self.array = []
		
	def push(self, value):
		if not len(self.array):
			node = Node(value)
			node.stackMin = value
		else:
			node = Node(value)
			last_node = self.array[-1]
			node.stackMin = node.value if node.value <= last_node.stackMin else last_node.stackMin
		self.array.append(node)
		
	def pop(self):
		self.array = self.array[:-1]
		
	def getMin(self):
		print(self.array[-1].stackMin)
		
	def __repr__(self):
		display = ''
		for i in self.array:
			display += f', {i.value}'
		return display[2:]
		
		
if __name__ == '__main__':
	s = Stack()
	print(s)
	s.push(1)
	print(s)
	s.getMin()
	s.push(4)
	s.push(3)
	print(s)
	s.getMin()
	s.push(0)
	print(s)
	s.getMin()
	s.pop()
	print(s)
	s.getMin()
	