"""
given an integer array, output all the unique pairs that sum up to a specific value k

example:
pair_sum([1,3,2,2], 4)

return two pairs:
(1,3)
(2,2)
"""


# solution 1 - brute force - O(n^2)
def pair_sum_1(arr, goal):
	if len(arr) <= 1:
		return None
	
	results = []
	for a in range(len(arr)):
		for b in range(a + 1, len(arr)):
			if arr[a] + arr[b] == goal:
				if not (arr[a], arr[b]) in results:
					results.append((arr[a], arr[b]))
	return results


# solution 2 -
def pair_sum_2(arr, goal):
	if len(arr) <= 1:
		return None
	
	results = []
	pairs = {}
	
	for a in arr:
		if a not in pairs.keys():
			pairs[goal - a] = a
		else:
			if not (a, goal - a) in results:
				results.append((a, goal - a))
	return results


arr = [1, 3, 2, 2]
goal = 4
print(pair_sum_1(arr, goal))
print(pair_sum_2(arr, goal))
