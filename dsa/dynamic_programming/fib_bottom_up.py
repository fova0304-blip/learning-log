memo =[0,1]
count = 0

def fib(n):
    for index in range(2,n+1):
        global count
        count+=1
        value = memo[index-1] + memo[index-2]
        memo.append(value)

    return memo[n]


print(fib(7))
print(count)