"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

time: O(n)
space: O(n) max n == 26 for only lower case English letters
"""


def solution(string, k):
	start = 0
	seen = {}
	ret = float('-inf')
	max_repeated_char_count = 0
	
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char not in seen:
			seen[end_char] = 0
		seen[end_char] += 1
		
		max_repeated_char_count = max(max_repeated_char_count, seen[end_char])
		
		if end - start + 1 - max_repeated_char_count > k:
			start_char = string[start]
			seen[start_char] -= 1
			start += 1
			
		ret = max(ret, end - start + 1)
	return ret
		
	
if __name__ == '__main__':
	inputs = [("aabccbb", 2), ("abbcb", 1), ("abccde", 1)]
	for string, k in inputs:
		res = solution(string, k)
		print(res)