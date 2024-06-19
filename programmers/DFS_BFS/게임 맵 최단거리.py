import sys
from collections import deque

def bfs(maps,x,y):
    # 맵의 크기
    n = len(maps) #행
    m = len(maps[0]) #열
    
    queue = deque()
    queue.append((x, y))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft() 
        for i in range(4): 

            nx = x + dx[i] 
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m: 
                #맵의 범위를 벗어나면 무시합니다.
                continue

            if maps[nx][ny] == 0: #벽인지 확인
                continue

            if maps[nx][ny] == 1: #방문하지 않은 길인지 확인하고 이동
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                #방문하지 않은 길(값이 1)인 경우, 현재 위치의 값에 1을 더하여 거리 값을 기록합니다.
                #새로운 위치 (nx, ny)를 큐에 추가합니다.

    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else:
        return -1
    #BFS 탐색을 통해 목표 지점까지의 최단 거리를 계산합니다.
    # 탐색이 끝난 후, 목표 지점의 값이 1보다 큰지 확인합니다.
    # 값이 1보다 큰 경우, 이는 시작점에서 목표 지점까지의 최단 거리를 의미합니다.
    # 값이 1인 경우, 이는 목표 지점에 도달하지 못했음을 의미합니다.
    # 목표 지점의 값이 1보다 큰 경우, 그 값을 반환하고, 그렇지 않으면 -1을 반환합니다.    
    
def solution(maps):    
    return bfs(maps, 0, 0)
