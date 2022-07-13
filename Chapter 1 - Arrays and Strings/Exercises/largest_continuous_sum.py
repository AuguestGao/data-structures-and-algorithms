"""
Given an array of integers (incl. positive and negative)
Find the largest continuous sum
bonus: also return start and end index of the sum

example: [1, 2, -1, 3, 4, 10, 10, -10, -1]
return: 29
bonus return: 0, 6
"""

def method_1(arr):
	# O (n^2)
	chunks = chunking(arr)
	record = chunks[0]
	largest_sum = record['sum']
	
	startIdx = 0
	while startIdx < len(chunks):
		for endIdx in range(startIdx, len(chunks)):
			total = sum(item['sum'] for item in chunks[startIdx: endIdx+1])
			
			if total > largest_sum:
				largest_sum = total
				record = {
					'sum': total,
					'startIndex': chunks[startIdx]['startIndex'],
					'endIndex': chunks[endIdx]['endIndex']
				}
		startIdx += 1
	return record
	
	
def chunking(arr):
	# O(n)
	sums = arr[0]
	isPos = True if arr[0] > 0 else False
	startIndex = 0
	endIndex = startIndex
	chunks = []
	
	for i in range(1, len(arr)):
		if (arr[i] > 0) == isPos:
			sums += arr[i]
			endIndex = i
		else:
			chunks.append({'sum': sums, 'startIndex': startIndex, 'endIndex': endIndex})
			startIndex = i
			endIndex = startIndex
			isPos = not isPos
			sums = arr[i]
	chunks.append({'sum': sums, 'startIndex': startIndex, 'endIndex': endIndex})
	return chunks
	
	
def method_2(arr):
	# O(n)
	# curr_sum = arr[0]
	# max_sum = arr[0]
	
	# # return max_sum only
	# for num in arr[1:]:
	# 	curr_sum = max(curr_sum + num, num)
	# 	max_sum = max(max_sum, curr_sum)
	# return max_sum
	
	curr_sum = {
		'sum': arr[0],
		'start': 0,
		'end': 0
	}
	
	max_sum = curr_sum.copy()
	
	for i in range(1, len(arr)):
		if not curr_sum:
			curr_sum = {
				'sum': 0,
				'start': i,
				'end': i
			}
			
		if arr[i] > 0:
			curr_sum['sum'] += arr[i]
			curr_sum['end'] = i
			
			if curr_sum['sum'] > max_sum['sum']:
				max_sum = curr_sum.copy()
		else:
			if curr_sum['sum'] + arr[i] > 0:
				curr_sum['sum'] += arr[i]
				curr_sum['end'] = i
			else:
				curr_sum = None
				
	return {'sum': max_sum['sum'], 'startIndex': max_sum['start'], 'endIndex': max_sum['end']}


def largest_cont_sum(arr, answer):
	result1 = method_1(arr)
	result2 = method_2(arr)
	print(f"method 1 => {result1} vs answer {answer}")
	print(f"method 2 => {result2} vs answer {answer}")
	
	
if __name__ == '__main__':
	arrs = [[1, 2, -1, 3, 4, 10, 10, -10, -1], [1, -5, 4, 2, -1, -2, 4, 3], [1,2,-1,3,4,-1], [-1,1]]
	answers = [29, 10, 9, 1]
	
	for i in range(len(arrs)):
		largest_cont_sum(arrs[i], answers[i])
