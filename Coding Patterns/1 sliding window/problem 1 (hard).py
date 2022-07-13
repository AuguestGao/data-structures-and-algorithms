"""
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


# time: O(n + m), n = len(string), m = len(pattern)
# space: O(m)
def solution(string, pattern):
	
	start = 0
	matches = 0
	chars_in_pattern = {}
	
	for char in pattern:
		if char not in chars_in_pattern:
			chars_in_pattern[char] = 0
		chars_in_pattern[char] += 1
		
	for end in range(len(string)):
		end_char = string[end]
		
		if end_char in chars_in_pattern:
			chars_in_pattern[end_char] -= 1
			if chars_in_pattern[end_char] == 0:
				matches += 1
			
		if matches == len(chars_in_pattern):
			return True
		
		if end - start + 1 >= len(pattern):
			start_char = string[start]
			if start_char in chars_in_pattern:
				if chars_in_pattern[start_char] == 0:
					matches -= 1
				chars_in_pattern[start_char] += 1
			start += 1
	
	return False
	

# time: O(n^2*log(n)) but save some time by skipping the char when char of string not in pattern
def solution2(string, pattern):
	chars_set = {char : 1 for char in pattern}
	sorted_pattern = ''.join(sorted(list(pattern)))
	start = 0
	
	for end in range(len(string)):
		if string[end] not in chars_set:
			start = end + 1
			continue
		
		if end - start + 1 == len(pattern):
			partial = ''.join(sorted(list(string[start: end + 1])))
			if partial == sorted_pattern:
				return True
			start += 1
		
	return False


# time: O(n^2*log(n))
def solution1(string, pattern):
	size = len(pattern)
	pattern = ''.join(sorted(list(pattern)))
	
	start = 0
	for end in range(size - 1, len(string)):
		
		partial = string[start : end + 1]
		partial = ''.join(sorted(list(partial)))
		
		if partial == pattern:
			return True
		
		start += 1
		
	return False


if __name__ == '__main__':
	inputs = [("oidbcaf", "abc"), ("odicf", "dc"), ("bcdxabcdy", "bcdyabcdx"), ("aaacb", "abc")]
	for string, pattern in inputs:
		res = solution(string, pattern)
		print(res)