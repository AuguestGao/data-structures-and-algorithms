# import class
import sys
sys.path.insert(1, '../Basics')
from singly_linked_list import Node, LinkedList


class XLL(LinkedList):
	
	def delete_value(self, value):
		prev_node = self.head
		if not prev_node:
			print('No such node')
			return None
		
		node = prev_node.next
		while node:
			if node.value == value:
				prev_node.next = node.next
				del node
				return None
			else:
				prev_node = node
				node = node.next
		print("No such node")
	
	
ll = XLL(['a', 'b', 'c', 'd', 'e'])
print(ll)
ll.delete_value('c')
print(ll)