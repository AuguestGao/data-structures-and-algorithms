"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e.,
the lowest level comes first. You should populate the values of all nodes in each level from left to right in
separate sub-arrays.

time: O(n)
space: O(n)  n space for queue + n space for the return list
"""

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def traverse(root):
	result = deque()
	
	if not root:
		return result
	
	q = deque()
	q.append(root)
	
	while q:
		level_size = len(q)
		level_nodes = []
		
		for _ in range(level_size):
			node = q.popleft()
			level_nodes.append(node.val)
			
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
			
		result.appendleft(level_nodes)
		
	return result
	

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Reverse level order traversal: " + str(traverse(root)))


main()