"""Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the
node values of that path equals ‘S’.

time: O(n) : number of tree nodes
space: O(n): used to store recursion
"""


class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def has_path(root, sum):
	
	if root is None:
		return False
	
	sum -= root.val
	
	if not root.left and not root.right and sum == 0:
		return True
		
	return has_path(root.left, sum) or has_path(root.right, sum)


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree has path: " + str(has_path(root, 23)))
	print("Tree has path: " + str(has_path(root, 16)))


main()