'''
Problem: Given an array of integers nums, 
find all the duplicates in the array using a hash table (dictionary).

Input:

A list of integers nums.

힌트:
각 숫자마다:
1. seen에 없으면 -> seen에 넣기
2. seen에 있으면 -> duplicate 후보
3. 후보인데 duplicates에 아직 없으면 -> duplicates에 넣기
'''

def find_duplicates(nums):
    seen = {}
    duplicates = []
    for num in nums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen[num] = True
    return duplicates





print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

