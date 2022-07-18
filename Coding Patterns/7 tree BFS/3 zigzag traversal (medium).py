"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the
values of all nodes of the first level from left to right, then right to left for the next level and keep alternating
in the same manner for the following levels.

time: O(n)
space: O(n)
"""

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def traverse(root):
	result = []
	
	if not root:
		return result
	
	q = deque()
	q.append(root)
	
	ltr = True  # left to right
	
	while q:
		level_size = len(q)
		level_nodes = deque()
		
		for _ in range(level_size):
			node = q.popleft()
			
			if ltr:
				level_nodes.append(node.val)
			else:
				level_nodes.appendleft(node.val)
			
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		
		ltr = not ltr
		result.append(list(level_nodes))
		
	return result


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("Zigzag traversal: " + str(traverse(root)))


main()
