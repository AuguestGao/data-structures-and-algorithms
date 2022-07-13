"""
Singly linked list
Python implementation
"""


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
	
	def __repr__(self):
		if self.next is not None:
			msg = f'value {self.value}, next {self.next.value}'
		else:
			msg = f'value {self.value}, next None'
		
		return msg


class LinkedList:
	def __init__(self, arr=None):
		self.head = None
		if arr is not None:
			node = Node(arr.pop(0))
			self.head = node
			while arr:
				next_node = Node(arr.pop(0))
				node.next = next_node
				node = next_node
	
	def insert_first(self, value):
		if not value:
			print('invalid insertion')
			return None;
		node = Node(value)
		
		if not self.head:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	
	def delete_first(self):
		if not self.head:
			print('nothing to delete')
			return None
		else:
			self.head = self.head.next
			print(self.__repr__()) #print
			
	def find_value(self, value):
		node = self.head
		count = 0
		while node:
			if node.value == value:
				print(f'node at {count}: {node}')
				return None
			else:
				count += 1
				node = node.next
		print(f'value {value} not found')
		return None

		
		
	def __repr__(self):
		node = self.head
		
		if not node:
			return 'No node'
		
		display = ''
		while node is not None:
			display += f' -> {node.value}'
			node = node.next
		return display[4:]

	def reverse(self):
		prev_node = self.head
		
		if not prev_node:
			return None
		
		node = prev_node.next
		prev_node.next = None
		
		while node:
			next_node = node.next
			node.next = prev_node
			prev_node = node
			node = next_node
			
		self.head = prev_node
		return None
	

# x = Node('1')
# y = Node('2')
# print(x)
# print(y)
# x.next = y
# print(x)
# print(y)

# ll = XLL(['a', 'b', 'c', 'd', 'e'])
# print(ll)
# ll.insert_first('')
# print(ll)
# ll.insert_first('zero')
# print(ll)
# ll.delete_first()
#
# ll.find_value('two')
# ll.find_value('ttt')
#
# ll.insert_first('what')
# ll.reverse()
# print(ll)

