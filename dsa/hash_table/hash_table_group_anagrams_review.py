'''
Review: Group Anagrams

Given a list of strings,
group the anagrams together.

Anagrams are words that use the same letters with the same counts,
but in a different order.

Examples:
"eat", "tea", "ate" are anagrams.
"tan", "nat" are anagrams.
"bat" has no matching anagram in the sample input.

Hint:
anagram끼리는 sorted 했을 때 같은 key가 된다.

"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"

Flow:
1. 빈 dictionary를 만든다.
2. word 하나씩 본다.
3. ''.join(sorted(word)) 로 key를 만든다.
4. key가 dictionary에 없으면 빈 list를 만든다.
5. dictionary[key]에 원래 word를 append 한다.
6. 마지막에 dictionary의 values를 list로 바꿔서 return 한다.
'''


def group_anagrams(strings):
    anagrams = {}


    for string in strings:
        word = ''.join(sorted(string))

        if word not in anagrams:
            anagrams[word] = []

        anagrams[word].append(string)

    return list(anagrams.values())



print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

print("\n4th set:")
print(group_anagrams([]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

    4th set:
    []

"""
