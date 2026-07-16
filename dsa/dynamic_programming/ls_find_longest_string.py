def find_longest_string(ls):
    if len(ls) == 0:
        return ''

    longest = ls[0]

    for i in ls:
        if len(i) > len(longest):
            longest = i

    return longest

    


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""