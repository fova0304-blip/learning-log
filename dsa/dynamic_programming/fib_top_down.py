memo = [None] * 100

count = 0

def fib(n):
    global count
    count += 1

    if memo[n] is not None:
        return memo[n]

    if n == 0 or n ==1:
        return n


    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]


print(fib(8))
print(count)

'''
DP = overlap 찾기 + simplest까지 쪼개기 + 저장하기
'''