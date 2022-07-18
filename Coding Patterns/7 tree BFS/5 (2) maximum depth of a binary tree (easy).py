"""Given a binary tree, find its maximum depth (or height)."""

from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_maximum_depth(root):
	if root is None:
		return 0
	
	q = deque()
	q.append(root)
	max_depth = 0
	
	while q:
		level_size = len(q)
		
		for _ in range(level_size):
			node = q.popleft()
			
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
				
		max_depth += 1
		
	return max_depth


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
	root.left.left = TreeNode(9)
	root.right.left.left = TreeNode(11)
	print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()