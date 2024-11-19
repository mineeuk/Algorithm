N = int(input())
n_list = []

for i in range(N):
    n_list.append(int(input())) # 입력받은 문자열을 즉시 정수로 변환하여 리스트에 추가할 수 있음.
num2 = n_list.sort()

for i in range(N):
    print(n_list[i])

num=int(input())
numbers=[]
for i in range(num):
    numbers.append(int(input()))
for i in sorted(numbers):
    print(i)