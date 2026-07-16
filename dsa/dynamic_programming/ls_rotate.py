# WRITE ROTATE FUNCTION HERE #
def rotate(ls,k):
    if k == 0:
        return ls
    
    k = k % len(ls)

    ls[:] = ls[-k:] + ls[:-k]

    return ls

    


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""