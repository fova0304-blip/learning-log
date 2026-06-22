def find_pairs(arr1, arr2, target):
    result = []
    set1 = set(arr1)
    for i in arr2:
        complement = target - i
        if complement in set1:
            result.append((complement,i))

    return result





arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""