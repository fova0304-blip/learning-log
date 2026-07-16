def remove_duplicates(ls):
    if len(ls) == 0:
        return 0

    if len(ls) >0:
        write = 1

        for read in range(1,len(ls)):
            if ls[read] != ls[read-1]:
                ls[write] = ls[read]
                write += 1

    return write
                

'''
write가 무조건 1인거는 당연히 리스트가 length가 1이 넘는순간 무조건 1개는 유니크한거고

read는 전꺼랑 비교해서 다르면 즉 무조건 다른숫자가 나왔다 그럼 유니크다 하면 그냥 ls에서 하나씩 하나씩 유니크숫자로 채워주고 += 1 해주고

-------------------------------------------------------------------------------------------------------------------

리스트가 비어있지 않다면 첫 번째 값은 무조건 unique로 인정
그래서 다음 unique를 넣을 자리는 index 1

전 값과 다르다
= 새로운 숫자가 시작됐다
= unique 값이다

'''






    
    


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


