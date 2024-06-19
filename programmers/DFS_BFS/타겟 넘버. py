cnt = 0

def dfs(i, result, numbers, target) :
    global cnt
    if i == len(numbers) :
        if result == target : 
            cnt+=1
            return
    else :
        dfs(i+1, result+numbers[i], numbers, target) #더한 경우 탐색 
        dfs(i+1, result-numbers[i], numbers, target)

def solution(numbers, target):
    result = 0
    dfs(0, result, numbers, target)
    
    return cnt


#solution 함수는 DFS 탐색을 시작하는 함수입니다.
# dfs 함수는 재귀적으로 각 숫자를 더하거나 빼서 모든 가능한 합계를 탐색합니다.
# 모든 숫자를 탐색한 후 합계가 목표 값과 같으면 cnt를 증가시킵니다.
# solution 함수는 최종적으로 cnt 값을 반환하여 목표 값을 만드는 경우의 수를 알려줍니다.
