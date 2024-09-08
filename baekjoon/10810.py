# 공이 들어있지 않은 바구니는 0을 출력

n, m = map(int, input().split())

baskets = [0] * n

for i in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        baskets[l] = k # i번 바구니부터 j번 바구니까지에 k번 번호, 바구니에 공을 넣는 작업을 수행
        
for i in range(n):
    print(baskets[i], end=' ')
    # 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력
    