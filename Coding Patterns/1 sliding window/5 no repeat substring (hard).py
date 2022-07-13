"""
Given a string, find the length of the longest substring which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".


thought: use hash table to remember the latest index of a character, retrieve it when the end character has been seen
time: O(n)
space: O(n) i.e. n is distinct chars in the string, can also use fixed-size space O(1) of 26 English letters
"""


# provided answer
def solution(string):
	start = 0
	char_last_seen_idx = {}
	ret = float('-inf')
	
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char in char_last_seen_idx:
			# update start to be the index of last seen of this char + 1 or start itself, whichever is greater
			# since the only time moves start is when end char has been seen, thus, need to purge char from the beginning
			start = max(start, char_last_seen_idx[end_char] + 1)
			
		# update index for this char to be the last seen index
		char_last_seen_idx[end_char] = end
		
		ret = max(ret, end - start + 1)
		
	return ret


def my_solution(string):
	start = 0
	seen = {}
	ret = float('-inf')
	
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char not in seen:
			seen[end_char] = 0
		seen[end_char] += 1

		while end - start + 1 > len(seen):
			start_char = string[start]
			seen[start_char] -= 1
			
			if seen[start_char] == 0:
				del seen[start_char]
				
			start += 1
		
		ret = max(ret, end - start + 1)
	
	return ret


if __name__ == '__main__':
	inputs = ["aabccbb", "abbbb", "abccde"]
	for string in inputs:
		res = solution(string)
		print(res)
