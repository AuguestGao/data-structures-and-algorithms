"""
Queue
via Array
* can also be done with Linked List*
"""


class Queue:
	def __init__(self):
		self.queue = []
	
	def dequeue(self):
		self.queue.pop(0)
	
	def enqueue(self, item):
		self.queue.append(item)
	
	def peek(self):
		return self.queue[0]
	
	def isEmpty(self):
		return len(self.queue) == 0
	
	def size(self):
		return len(self.queue)


xx = Queue()
print(xx.isEmpty())  # True
xx.enqueue(1)
print(xx.isEmpty())  # False
print(xx.size())  # 1
xx.enqueue(2)
print(xx.peek())  # 1
print(xx.size())  # 2
xx.dequeue()
print(xx.peek())  # 2
print(xx.size())  # 1