'''
hint:
첫 번째 for-loop:
각 char가 몇 번 나왔는지 dict에 count한다.
처음 보는 char면 count를 1로 만들고,
이미 본 char면 count를 += 1 한다.

두 번째 for-loop:
문자열을 처음부터 다시 보면서,
count가 1인 char를 만나면 즉시 바로 그 char를 return한다.
끝까지 없으면 None을 return한다.
'''

def first_non_repeating_char(characters):
    char_counts = {}

    for char in characters:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] ==1:
            return char




print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None


"""