"""
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Same as 3 longest substring with k distinct characters with k = 2

time: O(n)
space: O(1) i.e. 3 fruits
"""


def solution(fruits):
	start = 0
	baskets = {}
	ret = float('-inf')
	
	for end in range(len(fruits)):
		last_fruit = fruits[end]
		
		if last_fruit not in baskets:
			baskets[last_fruit] = 0
		baskets[last_fruit] += 1
		
		while len(baskets) > 2:
			first_fruit = fruits[start]
			baskets[first_fruit] -= 1
			
			if baskets[first_fruit] == 0:
				del baskets[first_fruit]
				
			start += 1
			
		ret = max(ret, end - start + 1)

	return ret


if __name__ == '__main__':
	inputs = [['A', 'B', 'C', 'A', 'C'], ['A', 'B', 'C', 'B', 'B', 'C']]
	for fruits in inputs:
		res = solution(fruits)
		print(res)