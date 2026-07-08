def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j+1] < my_list[j]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return my_list


'''
Bubble Sort:
큰 값이 오른쪽 끝으로 간다.
오른쪽 끝은 매번 정렬 완료된다.
그래서 i는 5,4,3,2,1처럼 줄어든다.

처음부터 끝까지 adjacent pair를 비교하면서 바꿔준다.
큰 값이 오른쪽으로 이동한다.


'''


print(bubble_sort([4,2,6,5,1,3]))

 
 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """