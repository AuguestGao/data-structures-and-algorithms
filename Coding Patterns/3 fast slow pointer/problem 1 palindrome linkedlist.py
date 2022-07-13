"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm
is finished. The algorithm should have O(N)O(N)O(N) time complexity where ‘N’ is the number of nodes in the
LinkedList.
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		

# solution
# time: O(n)
# space: O(1)
def is_palindromic_linked_list(head):
	slow, fast = head, head
	
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		
	second_head = reverse_second_half(slow)
	tail = second_head
	
	while head and second_head:
		if head.value != second_head.value:
			break
		
		head, second_head = head.next, second_head.next
	
	reverse_second_half(tail)
	
	if not head or not second_head:
		return True
	
	return False
	

def reverse_second_half(node):
	prev = None
	
	while node:
		nxt = node.next
		node.next = prev
		prev = node
		node = nxt

	return prev
	
	
def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(2)
	
	print("Is palindrome: " + str(is_palindromic_linked_list(head)))
	
	head.next.next.next.next.next = Node(2)
	print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()