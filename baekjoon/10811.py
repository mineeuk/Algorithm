n, m = map(int,input().spllit())

basket = [i for i in range(1, n+1)]
temp = 0

for _ in range(m):
    i,j = map(int,input().split())
    temp = basket[i-1:j] # i~j번까지 담기
    temp.reverse()
    basket[i-1:j] = temp # 뒤집은 순서 다시 담기
    
for i in range(n):
    print(basket[i], end=" ")
    