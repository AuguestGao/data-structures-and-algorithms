"""
Given a string of opening and closing parentheses, check whether it's balanced.
brackets (), [], or {}

example:
([]) balanced
([)] un balanced

assume no spaces in the given string
"""

# import class
import sys
sys.path.insert(1, '../Basics')
from stack import Stack


def bal_check(string):
	
	if len(string)%2 != 0:
		return False
	
	ps = Stack()  # parenthesis_stack
	for char in string:
		if char == "(":
			ps.push(")")
		elif char == '[':
			ps.push(']')
		elif char == "{":
			ps.push('}')
		else:
			need = ps.peek()
			ps.pop() # pop deletes but does not return the deletion
			if need != char:
				return False
	return True


if __name__ == '__main__':
	strings = ['({{}})', '([{})}', '()(){}[][)', '()[]{}']
	answers = [True, False, False, True]
	
	for i in range(len(strings)):
		result = bal_check(strings[i])
		print(f"{strings[i]} => {result} VS answer {answers[i]}")
		
		
