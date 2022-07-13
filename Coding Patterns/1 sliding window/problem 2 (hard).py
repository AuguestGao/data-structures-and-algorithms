"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

"""


def solution(string, pattern):
	start = 0
	anagrams = []
	char_freq = {}
	matches = 0
	
	for char in pattern:
		if char not in char_freq:
			char_freq[char] = 0
		char_freq[char] += 1
		
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char in char_freq:
			char_freq[end_char] -= 1
			if char_freq[end_char] == 0:
				matches += 1
			
		if matches == len(char_freq):
			anagrams.append(start)
		
		if end - start + 1 == len(pattern):
			start_char = string[start]
			if start_char in char_freq:
				if char_freq[start_char] == 0:
					matches -= 1
				char_freq[start_char] += 1
			start += 1
	
	return anagrams
	

if __name__ == '__main__':
	inputs = [("ppqp", "pq"), ("abbcabc", "abc")]
	for string, pattern in inputs:
		res = solution(string, pattern)
		print(res)