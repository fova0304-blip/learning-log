def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0
    current_count = 1
    max_count = 1

    ls = sorted(set(nums))

    for i in range(len(ls)-1):
        if ls[i]+1 == ls[i+1]:
            current_count +=1
        else:
            current_count =1

        if current_count > max_count:
            max_count = current_count
    return max_count



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""