"""
Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

Input: str1="xy#z", str2="xzz#"
Output: true
Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

Input: str1="xy#z", str2="xyz#"
Output: false
Explanation: After applying backspaces the strings become "xz" and "xy" respectively.

Input: str1="xp#", str2="xyz##"
Output: true
Explanation: After applying backspaces the strings become "x" and "x" respectively.
In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.

Input: str1="xywrrmp", str2="xywrrmu#p"
Output: true
Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.
"""


def solution(s1, s2):
	
	idx1 = len(s1) - 1
	idx2 = len(s2) - 1
	
	while idx1 >= 0 or idx2 >= 0:
		idx1 = get_next_idx(s1, idx1)
		idx2 = get_next_idx(s2, idx2)
		
		if idx1 < 0 and idx2 < 0: #  reached the end for both strings
			return True
		
		if idx1 < 0 or idx2 < 0: #  reached the end of one string but not the other
			return False
		
		if s1[idx1] != s2[idx2]:
			return False
		
		idx1 -= 1
		idx2 -= 1
	
	return True


def get_next_idx(s, idx):
	backspace_count = 0
	while s[idx] == '#':
		backspace_count += 1
		idx -= 1
	return idx - backspace_count


if __name__ == '__main__':
	inputs = [("xy#z", "xzz#"), ("xy#z", "xyz#"), ("xp#", "xyz##"), ("xywrrmp", "xywrrmu#p"), ('a', 'aaa')]
	for s1, s2 in inputs:
		res = solution(s1, s2)
		print(res)