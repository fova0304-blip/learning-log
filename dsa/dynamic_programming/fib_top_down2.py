memo = [None] * 100

def fib(n):
    # 이미 계산 한적있으면 꺼내씀 
    if memo[n] is not None:
        return memo[n]
    
    # 재귀는 이미 쓰고있으니 베이스 케이스 필수
    if n ==1 or n == 0:
        return n
    
    # 아직 계산 안했고, 베이스 케이스도 아님 - 재귀로 작은 문제를 구해서 memo[n] 저장 및 구함
    # 안구해본애면 재귀로 베이스 케이스까지 무조건 가야함 
    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]


print(fib(7))

