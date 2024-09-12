n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i) + "*"*(2*i-1))
    
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))


# *key point: 별의 개수가 증가하는 부분과 감소하는 부분으로 나누고 for문을 활용
# ,range 함수의 범위를 역순으로 지정하고 싶을 때는 세번째 파라미터로 음수를 넣어준다.
# for i in range(시작값, 끝값, -1) -> 시작값부터 끝값까지 역순으로 출력, -1:증가/감소스텝