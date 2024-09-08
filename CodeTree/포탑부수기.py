#삼성기출
from collections import deque

n,m,k = map(int,input().split()) #입력
# 1~4번까지 K번 반복

#to do
#1.공격자 선정 2.공격대상 3.레이저 공격 4.포탄 공격
#5.포탑 부서짐 6.포탑 정비

#[1] 공격자 선정 
# - 1)가장 약한 포탑, 2)가장 최근 공격한(포탑이공격한시기 history리스트), 
# 3)행과 열의 합이 가장 큰, 4)열 값이 가장 큰
# -> 선정후보가 여럿인 경우 우선 순위 정해야 함. (리스트 정렬 사용)
#-----------------------------------------

# n개의 행을 입력받아 2차원 리스트 game_map에 저장합니다.
# 각 행은 공백으로 구분된 m개의 정수로 이루어져 있습니다.
game_map = [list(map(int,input().split())) for _ in range(n)]

#공격한 순서 저장
history = [[0] * m for i in range(n)]
#history 리스트를 초기화합니다. 이는 공격한 순서를 저장하는 2차원 리스트입니다.
#n개의 행과 m개의 열을 가지며, 모든 값을 0으로 초기화합니다.

#우하좌상/상아 상좌 하우 하좌
dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

#공격자 선정
def select_attack(game_map):
    min_value = 6000
    candidate_a = []
    for i in range(n):
        for j in range(m):
            if game_map[i][j] < min_value and game_map[i][j] > 0:
                candidate_a = []  # 리스트 초기화
                min_value = game_map[i][j]  # min_value와 같은 공격력을 가졌다면 리스트에 추가
                candidate_a.append((history[i][j], i + j, j, i))  # 리스트 추가
            elif game_map[i][j] == min_value:
                candidate_a.append((history[i][j], i + j, j, i))

    candidate_a.sort(reverse=True)  # 우선순위 높은 순
    x, y = candidate_a[0][3], candidate_a[0][2]
    game_map[x][y] += (n + m)  # 공격력 증가
    history[x][y] += 1  # 공격한 순서 업데이트
    return x, y
    
#공격자의 공격
def select_defense(game_map, ax, ay):
    max_value = -1
    candidate_d = []
    for i in range(n):
        for j in range(m):
            if i == ax and j == ay:  # 공격자 제외
                continue
            if game_map[i][j] > max_value and game_map[i][j] > 0:
                max_value = game_map[i][j]
                candidate_d = [(history[i][j], i + j, j, i)]
            elif game_map[i][j] == max_value:
                candidate_d.append((history[i][j], i + j, j, i))

    candidate_d.sort()
    x, y = candidate_d[0][3], candidate_d[0][2]
    return x, y

#(1)레이저 공격-공격대상포탑까지 최단경로로 공격
def laser_attack(ax, ay, dex, dey, point):
    q = deque()
    q.append((ax, ay, [])) #공격자의 위치와 빈 리스트(경로 추적하기 위해)
    visited = [[0] * m for _ in range(n)] #방문
    #ax,ay 공격자
    visited[ax][ay] = True #시작위치 방문
    
    while q:
        x, y, route = q.popleft()
        #x,y 현재 탐색할 노드의 좌표
        for d in range(4): #상하좌우로 이동
            #nx,ny : 주위 8방향으로 이동한 새로운 위치
            nx = (x + dx[d]) % n # % n: 격자가 원형으로 연결된 것 처럼
            ny = (y + dy[d]) % m
            
            # 방문한 적이 있거나 부서진 포탑인 경우
            if visited[nx][ny]: continue
            if game_map[nx][ny] == 0: continue
            
            # 목표에 도달한 경우
            #dex, dey : 공격 대상 포탑
            if nx == dex and ny == dey:
                game_map[nx][ny] -= point #공격자 - 공격력

                for rx, ry in route:
                    #rx,ry 레이저 경로에 있는 포탑들의 좌표
                    game_map[rx][ry] -= point // 2 #주위 포탑 - 공격력/2
                    attack[rx][ry] = True #공격 받았음 표시
                attack[nx][ny] = True #공격 받았음 표시
                return True
            
            temp = route[:] #현재 경로 복사
            temp.append((nx, ny)) #새로운 위치를 경로에 추가
            visited[nx][ny] = True #새로운 위치를 방문한 것으로 표시
            q.append((nx, ny, temp)) #새로운 위치와 경로를 큐에 추가

    # 타겟에 도달하지 못한 경우
    return False

def potan(ax,ay,dex,dey,point):

    game_map[nx][ny] -= point

    for d in range(8):
        nx = (dex + dx[d]) % n 
        ny = (dey + dy[d]) % m

        #공격자 해당 공격 영향 x
        if nx == ax and ny == ay : continue
        game_map[nx][ny] -= point // 2 
        attack[nx][ny] = True

def break_potan():
    #격자 내 모든 포탑 탐색
    for i in range(n):
        for j in range(m):
            if game_map[i][j] < 0:
                 game_map[i][j] = 0

def max_check():
    return max(max(line) for line in game_map) #각 행에서 최대값 찾음

#check_potan함수에서 부서지지 않은 포탑이 하나만 남았을 때, 
#해당 포탑의 최대 공격력을 출력하고 게임을 종료하기 위해 max_check 함수를 사용
def check_potan():
    no_attack = [] #공격받지 않은 포탄 리스트
    no_attack_cnt = 0
    for i in range(n):
        for j in range(m):
            # 포탑이 부서진 경우
            if game_map[i][j] == 0:
                continue
            no_attack_cnt += 1
            # 공격과 관련이 있는 경우
            if attack[i][j]:
                continue
            no_attack.append((i, j))
    
    if no_attack_cnt == 1:
        print(check_potan())
        exit(0)
    
    for i, j in no_attack:
        game_map[i][j] += 1

no_attack = []
time = 1
for kk in range(k):
    attack = [[0] * m for _ in range(n)]  # 공격 맵 초기화
    ax, ay = select_attack(game_map)  # 가장 약한 포탑 공격자로 선정

    history[ax][ay] = time  # 공격자의 위치 기록
    time += 1

    attack[ax][ay] = 2  # 공격자의 위치를 공격맵에 표시

    dex, dey = select_defense(game_map, ax, ay)
    attack[dex][dey] = 2

    point = game_map[ax][ay]
    if not laser_attack(ax, ay, dex, dey, point):
        potan(ax, ay, dex, dey, point)

    break_potan()
    check_potan()

print(max_check())
