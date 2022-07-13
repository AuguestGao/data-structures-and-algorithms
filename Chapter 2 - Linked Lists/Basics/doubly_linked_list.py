class Node:
	def __init__(self, value=None):
		self.value = value
		self.prev = None
		self.next = None
		
	def __repr__(self):
		if not self.prev and not self.next:
			msg = f'value = {self.value}, prev = {self.prev}, next = {self.next}'
		elif not self.prev:
			msg = f'value = {self.value}, prev = {self.prev}, next = {self.next.value}'
		elif not self.next:
			msg = f'value = {self.value}, prev = {self.prev.value}, next = {self.next}'
		else:
			msg = f'value = {self.value}, prev = {self.prev.value}, next = {self.next.value}'
		return msg

# a = Node()
# b = Node('B')
# a.next = b
# print(a)
# print(b)


class Doubly_Linked_list:
	def __init__(self, arr = None):
		self.head = None
		if arr is not None:
			node = Node(arr.pop(0))
			self.head = node
			
			while arr:
				next_node = Node(arr.pop(0))
				node.next = next_node
				next_node.prev = node
				node = node.next
		
	def __repr__(self):
		if not self.head:
			return 'empty doubly linked list'
		
		node = self.head
		display = ''
		
		while node:
			display += f' <-> {node.value}'
			node = node.next
		return display[5:]
	
	
dl = Doubly_Linked_list(['a', 'b', 'c', 'd'])
print(dl)