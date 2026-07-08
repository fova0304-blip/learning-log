def selection_sort(ls):
    for i in range(len(ls)-1): #끝까지가면 index out of range
        min_index = i
        for j in range(i+1, len(ls)): #j는 끝까지 가도됨
            if ls[j] < ls[min_index]:
                min_index = j

        if i != min_index: #min_index가 i랑 같은경우는 걍 스킵해도됨
            temp = ls[i]
            ls[i] = ls[min_index]
            ls[min_index] = temp

    return ls


'''
현재 위치부터 끝까지 보면서 minimum index를 찾고,
그 minimum 값을 현재 위치와 한 번 swap한다.
'''




print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

