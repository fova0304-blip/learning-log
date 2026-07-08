def insertion_sort(ls):
    for i in range(1,len(ls)):
        temp = ls[i]
        j = i -1
        while temp < ls[j] and j > -1:
            ls[j+1] = ls[j]
            ls[j] = temp
            j -=1

    return ls

'''
현재 값을 왼쪽의 정렬된 구간 안으로 끼워 넣는다.
작으면 왼쪽으로 계속 swap하면서 이동한다.

temp를 들고 왼쪽으로 이동한다.
왼쪽 값이 temp보다 크면 그 값을 오른쪽으로 한 칸 옮긴다.
그 자리에 temp를 넣는다.
j를 줄이면서 계속 왼쪽을 확인한다.
j가 -1이 되거나, temp보다 작거나 같은 값을 만나면 멈춘다-> 왼쪽 구간은 항상 정렬되어 있다고 가정
'''


print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

