# 이코테
# 음료수 얼려 먹기
# 출처 : https://www.youtube.com/watch?v=e7_H8SLZlHY

# N,M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
graph = [] #얼음 틀 모양의 2차원 그래프 생성

for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    # 연결된 모든 노드들 방문할 때마다 카운트
    if dfs(i, j) == True:
      result += 1
print(result) #정답 출력


# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y, graph):
    # 위치에서 벗어날 때는 False, 행렬의 범위를 벗어나는 경우의 종료 조건
    # 탐색이 얼음 틀의 유효한 범위 내에서만 이루어지도록 경계를 확인하는 역할
    if x <= -1 or x >= n or y <= -1 or y >= m:
        # x <= -1: x가 0보다 작은지 확인 / n: 행의 총 개수
        return False
    
    # 현재 위치가 방문하지 않은 곳 0 일때 (얼음이 얼 수 있는 곳)
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y,graph)
        dfs(x + 1, y, graph)
        dfs(x, y - 1, graph)
        dfs(x, y + 1, graph)
        # 연결된 모든 노드들 방문한 이후에는 True값 반환
        return True
    # 현재 노드를 이미 방문했다면 False값 반환
    return False

