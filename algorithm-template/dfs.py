def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [], # 인덱스 0에 대한 노드 1은 비워두기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현
# 1~8번 노드까지, 0은 사용하지 않기위해 9
visited = [False] * 9
# 정의된 BFS 함수 호출
dfs(graph,1,visited)