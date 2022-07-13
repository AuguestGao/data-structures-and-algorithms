# import class
import sys
sys.path.insert(1, '../Basics')
from singly_linked_list import Node, LinkedList


class XLL(LinkedList):
	# no temporary buffer needed required
	def remove_dups(self):
		# remove duplicates
		
		slow_node = self.head
		
		while slow_node:
			fast_node = slow_node.next
			temp_node = slow_node
			while fast_node:
				if fast_node.value == slow_node.value:
					temp_node.next = fast_node.next
					del fast_node
					fast_node = temp_node.next
				else:
					temp_node = temp_node.next
					fast_node = fast_node.next
			slow_node = slow_node.next

	def remove_dups2(self):
		node = self.head
		buffer = {}
		
		while node.next:
			if node.value not in buffer.keys():
				buffer[node.value] = True
				node = node.next
			else:
				next_node = node.next
				node.next = next_node.next
				del next_node
				

if __name__ == '__main__':
	s = 'bshvsscas'
	ll = XLL(list(s))
	print(ll)
	# ll.remove_dups()
	ll.remove_dups2()
	print(ll)
	
	


