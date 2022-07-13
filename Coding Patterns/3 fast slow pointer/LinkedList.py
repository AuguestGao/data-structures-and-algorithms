"""Basic implementation of linked list to use for doing coding interviews"""


class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None
		
	def __repr__(self):
		next_val = self.next.val if self.next else None
		print(f'value {self.val}, next {next_val}')
		

class LinkedList:
	def __init__(self, arr=None):
		self.head = None
		
		if arr:
			node = Node(arr[0])
			self.head = node
			
			i = 1
			while i < len(arr):
				next_node = Node(arr[i])
				node.next = next_node
				node = node.next
				i += 1
				