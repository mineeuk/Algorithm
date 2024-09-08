n, m = map(int, input().split()) # 바구니 n개, 공 바꿀 m번 횟수

baskets = [i for i in range(1, n+1)] # 바구니 생성
temp = 0 # 임시 바구니

for _ in range(m):
    i,j = map(int, input().split())
    temp = baskets[i-1] # 리스트의 인덱스가 0부터 시작
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

    """
    1 ) temp(임시) 바구니에  i값을 저장

    2 ) i번 바구니에 j번 바구니의 값을 저장

    3 ) j번 바구니에 temp값을 저장 
    """ 
for x in range(n):
    print(baskets[x], end=" ")