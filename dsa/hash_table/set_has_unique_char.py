def has_unique_chars(strings):
    my_list = []
    for string in strings:
        my_list.append(string)
    
    no_duplicate_list = list(set(my_list))

    if len(my_list) == len(no_duplicate_list):
        return True
    else:
        return False




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""