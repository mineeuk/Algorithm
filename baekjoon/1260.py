N, M, V = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited_dfs = [0]*(N+1)
visited_bfs = visited_dfs.copy()

#dfs 함수 만들기
def dfs(V):
    visited_dfs[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited_dfs[i] == 0:
            dfs(i)
def bfs(V):
    queue = [V]
    visited_bfs[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited_bfs[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited_bfs[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)

    