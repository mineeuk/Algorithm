# 피보나치 함수 - DP로 구현
# fibo(N)호출 시 0,1 각각 호출 수 
T = int(input())

for _ in range(T):
    N = int(input())
    a, b = 1, 0
    for i in range(N):
        a, b = b, a+b
    print(a,b)
