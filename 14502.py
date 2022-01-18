# 뒤집어서 봐도 DFS, BFS
# 벽을 세우고 안전 영역을 파악하자..
import copy
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = []
virus = deque()
result = 0

#입력을 토대로 그래프를 그려보세
for i in range(N):
    arr.append(list(map(int, stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if arr[i][j] ==2:
            virus.append((i, j))

def wall(cnt):
    global result
    if cnt==3: # 벽 3개를 모두 채웠을 때
        result_arr = copy.deepcopy(arr) #벽 3개를 채운 그래프를 저장해둔다고 생각.
        bfs(result_arr) # DFS를 돌려보는거지..
        safe = sum(k.count(0) for k in result_arr) #벽 3개 채운 그래프에서 0 개수 찾기.
        result = max(result, safe) # safe 저장해놓는거지.
        return True # 어짜피 result는 global이다.

    else: # 벽 3개를 모두 채우지 못했을 때
        for i in range(N): #0에서 시작
            for j in range(M):
                if arr[i][j] ==0: # 0으로 채워진 공간은 벽을 세울 수 있는 공간이다.
                    arr[i][j] =1 # 벽을 한번 세워보고
                    wall(cnt+1) #돌려보는거지
                    arr[i][j]=0 # 다시 돌려놓는 것을 잊지 말자."""

def bfs(arr):
    while virus:
        x, y = virus.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<= n_x <N and 0<= n_y < M:
                if arr[n_x][n_y] ==0:
                    arr[n_x][n_y] =2
                    virus.append((n_x, n_y))

wall(0)
print(result)