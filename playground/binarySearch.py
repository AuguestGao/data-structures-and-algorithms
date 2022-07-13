# Array


def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if target > nums[middle]:
            left = middle + 1
        elif target < nums[middle]:
            right = middle - 1
        else:
            return middle
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2

result = search(nums, target)
print(result)
