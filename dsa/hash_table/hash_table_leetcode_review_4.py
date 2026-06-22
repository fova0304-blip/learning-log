'''
Hash Table / Set Review - 6 Problems

No hints in this file.
Read the function name and problem statement, then implement each function.
'''


'''
Problem 1: Remove Duplicates

Given a list, return a new list with duplicates removed.
The order of the result does not matter.
'''


def remove_duplicates(my_list):
    new_list = list(set(my_list))
    return new_list

    


'''
Problem 2: Find Duplicates

Given a list of integers, return a list of numbers that appear more than once.
Each duplicate number should appear only once in the result.
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


'''
Problem 3: First Non-Repeating Character

Given a string, return the first character that appears only once.
If every character repeats, return None.
'''


def first_non_repeating_char(strings):
    seen = {}

    for string in strings:
        if string not in seen:
            seen[string] = 1
        else:
            seen[string] += 1

    for string in strings:
        if seen[string] ==1:
            return string
        


'''
Problem 4: Group Anagrams

Given a list of strings, group the anagrams together.
Return a list of lists.
'''


def group_anagrams(strings):
    dict = {}
    
    for string in strings:
        word = "".join(sorted(string))

        if word not in dict:
            dict[word] = []

        dict[word].append(string)

    return list(dict.values())



'''
Problem 5: Two Sum

Given a list of integers and a target,
return the indices of the two numbers that add up to the target.
If no pair exists, return an empty list.
'''


def two_sum(nums, target):
    dict = {}

    for index,num in enumerate(nums):
        complement = target - num

        if complement not in dict:
            dict[num] = index
        else:
            return [dict[complement], index]
        
    return []



'''
Problem 6: Subarray Sum

Given a list of integers and a target,
return the start and end indices of a continuous subarray
whose sum equals the target.
If no such subarray exists, return an empty list.
'''


def subarray_sum(nums, target):
    dict= {0:-1}
    sum = 0

    for index, num in enumerate(nums):
        
        sum += num
        complement = sum - target

        if complement not in dict:
            dict[sum] = index
        else:
            return [dict[complement]+1, index]
        
    return []
    


print("Problem 1: Remove Duplicates")
print(remove_duplicates([1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]))
print(remove_duplicates([]))

print("\nProblem 2: Find Duplicates")
print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))

print("\nProblem 3: First Non-Repeating Character")
print(first_non_repeating_char("leetcode"))
print(first_non_repeating_char("hello"))
print(first_non_repeating_char("aabbcc"))
print(first_non_repeating_char(""))

print("\nProblem 4: Group Anagrams")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))
print(group_anagrams([]))

print("\nProblem 5: Two Sum")
print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))

print("\nProblem 6: Subarray Sum")
print(subarray_sum([1, 2, 3, 4, 5], 9))
print(subarray_sum([-1, 2, 3, -4, 5], 0))
print(subarray_sum([2, 3, 4, 5, 6], 3))
print(subarray_sum([], 0))


"""
    EXPECTED OUTPUT:
    ----------------
    Problem 1: Remove Duplicates
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    []

    Problem 2: Find Duplicates
    []
    [1, 2]
    [1]
    [3, 4]

    Problem 3: First Non-Repeating Character
    l
    h
    None
    None

    Problem 4: Group Anagrams
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]
    []

    Problem 5: Two Sum
    [1, 4]
    [1, 3]
    [1, 3]
    []

    Problem 6: Subarray Sum
    [1, 3]
    [0, 3]
    [1, 1]
    []

    Note:
    For remove_duplicates and group_anagrams, order may be different.
"""
