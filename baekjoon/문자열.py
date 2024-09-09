# Q.27866

S = input()
i = int(input())
print(S[i-1])

# *key point: 파이썬에서는 문자열 안의 문자를 index로 접근할 수 있다.
# -------------------------------------------------------- #

# Q.2743

S = input()
print(len(S))

# -------------------------------------------------------- #

# Q.9086
t = int(input())

for _ in range(t):
    i = str(input())
    print(i[0]+i[-1])

# -------------------------------------------------------- #

# Q.11654

S = input()
print(ord(S))
# *key point: 문자->아스키 : ord(), 아스키->문자 : chr()
# -------------------------------------------------------- #

# Q.11718

while True :
    try :
        # 예외가 발생할 수 있는 코드 
        print(input())
    except EOFError:
        # 예외 처리
        break
        # 예외 발생시 while 루프 종료

# *key point: 입력을 받아 그대로 출력하기
# -------------------------------------------------------- #

