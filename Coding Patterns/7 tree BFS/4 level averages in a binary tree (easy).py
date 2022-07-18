"""
Given a binary tree, populate an array to represent the averages of all of its levels.

time: O(n)
space: O(n)
"""

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_level_averages(root):
	result = []
	
	q = deque()
	q.append(root)
	
	while q:
		level_size = len(q)
		level_sum = 0.0
		
		for _ in range(level_size):
			node = q.popleft()
			level_sum += node.val
			
			if node.left:
				q.append(node.left)
			
			if node.right:
				q.append(node.right)
		avg = round(level_sum / level_size, 1)
		result.append(avg)
	
	return result


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.left.right = TreeNode(2)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level averages are: " + str(find_level_averages(root)))


main()