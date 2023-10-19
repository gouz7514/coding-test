# 다리 만들기
# https://www.acmicpc.net/problem/2146
# 골드 3
# 나의 풀이 - 오래 걸렸지만 정답..! but, 시간 복잡도가 많이 떨어진다
# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())
# arr = [list(map(int, list(input().strip().split(' ')))) for _ in range(N)]

# visited = [[False for _ in range(N)] for _ in range(N)]
# grounds = [] # 각 육지의 좌표
# answer = sys.maxsize

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# def count_ground(i, j):
#   ground = []
#   queue = deque()
#   queue.append((i, j))
#   visited[i][j] = True

#   while queue:
#     x, y = queue.popleft()
#     ground.append([x, y])

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if (nx < 0 or nx >= N or ny < 0 or ny >= N):
#         continue
#       if visited[nx][ny] or arr[nx][ny] == 0:
#         continue

#       visited[nx][ny] = True
#       queue.append((nx, ny))

#   grounds.append(ground)

# for i in range(N):
#   for j in range(N):
#     if arr[i][j] == 1 and not visited[i][j]:
#       count_ground(i, j)

# def dfs(grounds, visited, distance):
#   queue = deque()
#   for ground in grounds:
#     queue.append(ground)

#   while queue:
#     x, y = queue.popleft()

#     for k in range(4):
#       nx = x + dx[k]
#       ny = y + dy[k]

#       if (nx < 0 or nx >= N or ny < 0 or ny >= N):
#         continue
#       if visited[nx][ny]:
#         continue
#       if arr[nx][ny] == 1:
#         if [nx, ny] in grounds:
#           visited[nx][ny] = True
#           queue.append((nx, ny))
#           continue
#         else:
#           return distance[x][y]
      
#       visited[nx][ny] = True
#       queue.append((nx, ny))
#       distance[nx][ny] = distance[x][y] + 1

# # grounds 순회하면서 다음 육지 닿을 때 거리 측정
# for ground in grounds:
#   visited = [[False for _ in range(N)] for _ in range(N)]
#   distance = [[0 for _ in range(N)] for _ in range(N)]
#   answer = min(answer, dfs(ground, visited, distance))

# print(answer)


# 다른 사람의 풀이
from sys import stdin
from collections import deque

graph = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS_mark(sx, sy, mark):
    queue = deque()
    queue.append((sx, sy))
    visit[sx][sy] = True
    graph[sx][sy] = mark

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny))
                graph[nx][ny] = mark


def BFS():
    queue = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                queue.append((i, j))
                depth[i][j] = 0
    
    ans = 2 * N

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[cx][cy] == graph[nx][ny]:
                continue
            if graph[nx][ny] != 0:
                ans = min(ans, depth[cx][cy] + depth[nx][ny])
            else:
                graph[nx][ny] = graph[cx][cy]
                depth[nx][ny] = depth[cx][cy] + 1
                queue.append((nx, ny))

    return ans

N = int(input())
for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

# Marking - DFS
visit = [[False for _ in range(N)] for _ in range(N)]
mark = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visit[i][j]:
            BFS_mark(i, j, mark)
            mark += 1

print(graph)

# Finding Min Distance
depth = [[-1 for _ in range(N)] for _ in range(N)]
print(BFS())
print(graph)