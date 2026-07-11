def merge(ls1,ls2):
    combined = []
    i = 0
    j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] < ls2[j]:
            combined.append(ls1[i])
            i += 1
        else:
            combined.append(ls2[j])
            j += 1

    while i < len(ls1):
        combined.append(ls1[i])
        i += 1

    while j < len(ls2):
        combined.append(ls2[j])
        j += 1

    return combined




print(merge([1,2,7,8], [3,4,5,6]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
    
"""