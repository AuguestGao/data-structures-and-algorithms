# import class
import sys
sys.path.insert(1, '../Basics')
from singly_linked_list import Node, LinkedList

class XLL(LinkedList):
	def nth_last(self, n):
		# return the node that is nth to last node
		node = self.head
		
		for i in range(n - 1):
			if not node.next:
				print('Invalid input n')
				return None
			node = node.next
		
		nth_node = self.head
		
		while node.next:
			nth_node = nth_node.next
			node = node.next
		
		print(nth_node)

ll = XLL(['a', 'b', 'c', 'd', 'e'])
ll.nth_last(3)