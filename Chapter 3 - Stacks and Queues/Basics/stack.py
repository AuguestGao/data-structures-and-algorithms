"""
Stacks
via Array
* can also be done with Linked List*
"""


class Stack:
	def __init__(self):
		self.stack = []
		
	def pop(self):
		self.stack.pop()
	
	def push(self, item):
		self.stack.append(item)
	
	def peek(self):
		return self.stack[-1]
	
	def isEmpty(self):
		return len(self.stack) == 0
	
	def size(self):
		return len(self.stack)
	
if __name__ == '__main__':
	xx = Stack()
	print(xx.isEmpty())  # True
	xx.push(1)
	print(xx.isEmpty())  # False
	print(xx.size())  # 1
	xx.push(2)
	print(xx.peek())  # 2
	print(xx.size())  # 2
	xx.pop()
	print(xx.peek())  # 1
	print(xx.size())  # 1
