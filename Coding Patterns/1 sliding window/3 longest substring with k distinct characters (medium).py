"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

examples:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

thought: let next one coming into the window, then judge and maybe reduce the starting side
tag: dynamic window, hash table

time: O(n) i.e. n == len(string)
space: O(n) i.e. n == k

"""


def solution(string, k):
	start = 0
	char_freq = {}
	ret = float('-inf')
	
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char not in char_freq:
			char_freq[end_char] = 0
		char_freq[end_char] += 1
		
		while len(char_freq) > k:
			start_char = string[start]
			char_freq[start_char] -= 1
			if char_freq[start_char] == 0:
				del char_freq[start_char]
			start += 1
				
		ret = max(ret, end - start + 1)
	
	return ret


if __name__ == '__main__':
	inputs = [("araaci", 2), ("araaci", 1), ("cbbebi", 3)]
	for string, k in inputs:
		res = solution(string, k)
		print(res)
