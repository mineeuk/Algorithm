import math

def position(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    # x1, x2, y1, y2 : 원의 좌표
    # r1, r2 : 반지름

    if distance == 0 and r1 == r2 : # 완전 겹침
        return -1
    elif distance == r1+r2 or distance == abs(r1-r2): # 한점
        return 1
    elif distance > r1+r2 or distance < abs(r1-r2): # 만나지않음
        return 0
    else : # 두점
        return 2
    
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    result = position(x1, y1, r1, x2, y2, r2)
    print(result)