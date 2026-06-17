# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
'''
현재까지의 sum에서 target을 뺀 값이 이전 sum들 중에 있으면,
그 이전 sum 다음 index부터 현재 index까지의 구간 합이 target이다.
'''


def subarray_sum(nums,target):
    dict = {0:-1}
    current_sum = 0

    for index, num in enumerate(nums):
        current_sum += num
        needed = current_sum - target

        if needed in dict:
            return [dict[needed]+1, index]
        
        dict[current_sum] = index

    return []






nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
