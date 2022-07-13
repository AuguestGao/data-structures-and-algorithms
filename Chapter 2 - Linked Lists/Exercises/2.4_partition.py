# import class
import sys
sys.path.insert(1, '../Basics')
from singly_linked_list import Node, LinkedList


class XLL(LinkedList):
	def partition(self, value):
		# move all node values < the given value before the node's value == the given value
		tail = self.head
		counter = 0
		while tail.next:
			counter += 1
			tail = tail.next
		
		prev_node = self.head
		node = prev_node.next # skip the first node
		
		for _ in range(counter - 1):
			if node.value >= value:
				prev_node.next = node.next
				tail.next = node
				tail = tail.next
				node = node.next
				tail.next = None
			else:
				prev_node = node
				node = node.next

		# deal with the first node
		node = self.head
		if node.value >= value:
			self.head = node.next
			tail.next = node
			node.next = None
		
			
ll = XLL([10, 50, 30, 60, 40, 20])
print(ll)
ll.partition(25)
print(ll)