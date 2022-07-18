"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the
root node to the nearest leaf node.

time: O(n)
space: O(n)
"""

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_minimum_depth(root):
	if not root:
		return 0
	
	q = deque()
	q.append(root)
	
	minimum_depth = 1
	
	while q:
		level_size = len(q)
		
		for _ in range(level_size):
			node = q.popleft()
			
			if not node.left and not node.right:
				return minimum_depth
			
			if node.left:
				q.append(node.left)
			
			if node.right:
				q.append(node.right)
		
		minimum_depth += 1


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
