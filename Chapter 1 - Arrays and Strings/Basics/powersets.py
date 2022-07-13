def powersets(arr):
    # print(arr)
    if len(arr) == 0:
        return [[]]

    for i in arr:
        arr_copy = arr[:]
        arr_copy.remove(i)

        perms = powersets(arr_copy)
        results = perms[:]

        for perm in perms:
            if len(perm) == 0:
                results.append([i])
            else:
                for index in range(len(perm) + 1):
                    perm_copy = perm[:]
                    perm_copy.insert(index, i)
                    results.append(perm_copy)
    return results


if __name__ == "__main__":
    arr = [1, 2, 3]
    answer = powersets(arr)
    print(answer)
    print(len(answer))
