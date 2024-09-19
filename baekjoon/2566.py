# 9x9 격자에서 최댓값과 위치 찾기
max_num = 0
max_row, max_col = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        if num > max_num:
            max_num = num
            max_row, max_col = i + 1, j + 1

print(max_num)
print(max_row, max_col)