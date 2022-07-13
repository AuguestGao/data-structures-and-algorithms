def permutations(arr):
    if len(arr) == 1:
        return [arr]

    results = []

    while arr:
        i = arr.pop()
        perms = permutations(arr)

        for perm in perms:
            for j in range(len(perm) + 1):
                perm_copy = perm[:]
                perm_copy.insert(j, i)
                results.append(perm_copy)

    return results


if __name__=='__main__':
    arr=[1, 2, 3]
    results = permutations(arr)
    print(results)
    print(len(results))