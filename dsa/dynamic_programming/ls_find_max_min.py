def find_max_min(ls):
    return(max(ls),min(ls))


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""


def find_max_min(ls):
    max_num = ls[0]
    min_num = ls[0]

    for i in ls:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i


    return (max_num,min_num)