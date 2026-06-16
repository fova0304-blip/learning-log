'''
Review 1: Find Duplicates

Given a list of integers nums,
return a list of numbers that appear more than once.

Each duplicate number should appear only once in the result.

Hint:
seen은 이미 본 숫자를 기록한다.
duplicates는 중복으로 확정된 숫자를 기록한다.

각 숫자마다:
1. seen에 없으면 -> seen에 넣기
2. seen에 있으면 -> duplicate 후보
3. 후보인데 duplicates에 아직 없으면 -> duplicates에 넣기
'''


def find_duplicates(nums):
    seen ={}
    duplicates = []

    for num in nums:
        if num not in seen:
            seen[num] = True
        else:
            if num not in duplicates:
                duplicates.append(num)

    return duplicates



'''
Review 2: First Non-Repeating Character

Given a string,
return the first character that appears only once.
If every character repeats, return None.

Hint:
첫 번째 for-loop:
각 char가 몇 번 나왔는지 dict에 count한다.
처음 보는 char면 count를 1로 만들고,
이미 본 char면 count를 += 1 한다.

두 번째 for-loop:
문자열을 처음부터 다시 보면서,
count가 1인 char를 만나면 바로 그 char를 return한다.
끝까지 없으면 None을 return한다.
'''


def first_non_repeating_char(string):
    repeat = {}

    for char in string:
        if char not in repeat:
            repeat[char] = 1
        else:
            repeat[char] += 1
    
    for char in string:
        if repeat[char] == 1:
            return char
        
    return None


print("Find Duplicates")
print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([]))

print("First Non-Repeating Character")
print(first_non_repeating_char("leetcode"))
print(first_non_repeating_char("hello"))
print(first_non_repeating_char("aabbcc"))
print(first_non_repeating_char(""))


"""
    EXPECTED OUTPUT:
    ----------------
    Find Duplicates
    []
    [1, 2]
    [1]
    [3, 4]
    []
    First Non-Repeating Character
    l
    h
    None
    None

"""
