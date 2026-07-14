'''
List Sort Review

Implement:
1. bubble_sort(my_list)
2. selection_sort(my_list)
3. insertion_sort(my_list)
'''


def bubble_sort(ls):
    for i in range(len(ls)-1,0,-1):
        for j in range(i): #틀린곳: i가 5,4,3.. 이런식으로 줄어서 i로만 해도 됨
            if ls[j] > ls[j+1]:
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp

    return ls

    


def selection_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i,len(ls)):

            if ls[min_index] > ls[j]:
                min_index = j

        if i != min_index:
            temp = ls[i]
            ls[i] = ls[min_index]
            ls[min_index] = temp

    return ls


def insertion_sort(ls):
    for i in range(1,len(ls)):
        temp = ls[i]
        j = i - 1
        while temp < ls[j] and j > -1:
            ls[j+1] = ls[j]
            ls[j] = temp
            j -= 1

    return ls


def check(sort_name, sort_func, test_cases):
    print(sort_name)
    for original, expected in test_cases:
        test_input = original[:]
        actual = sort_func(test_input)
        print("Input:   ", original)
        print("Expected:", expected)
        print("Actual:  ", actual)
        print("PASS" if actual == expected else "FAIL")
        print()


tests = [
    ([4, 2, 6, 5, 1, 3], [1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([3, 2, 2, 1, 3], [1, 2, 2, 3, 3]),
    ([], []),
    ([7], [7]),
]


check("Bubble Sort", bubble_sort, tests)
check("Selection Sort", selection_sort, tests)
check("Insertion Sort", insertion_sort, tests)


"""
    EXPECTED OUTPUT:
    ----------------
    Every test should print PASS.
"""
