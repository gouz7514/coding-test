# DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 실버 2
# 나의 풀이 - 인접 행렬
# from collections import deque

# N, M, V = list(map(int, input().split(' ')))
# visit = [0 for _ in range(N + 1)]
# adj = [[0] * (N + 1) for _ in range(N + 1)]

# for _ in range(M):
#   x, y = list(map(int, input().split(' ')))
#   adj[x][y] = 1
#   adj[y][x] = 1

# def dfs(v):
#   print(v, end = ' ')
#   visit[v] = 1

#   for i in range(1, N + 1):
#     if adj[v][i] == 1 and visit[i] == 0:
#       dfs(i)

# def bfs(v):
#   queue = deque([v])
#   visit[v] = 1

#   while queue:
#     x = queue.popleft()
#     print(x, end = ' ')
#     for i in range(1, N + 1):
#       if adj[x][i] == 1 and visit[i] == 0:
#         queue.append(i)
#         visit[i] = 1

# dfs(V)
# visit = [0 for _ in range(N + 1)]
# print()
# bfs(V)

# 인접 리스트를 사용해보자
from collections import deque

N, M, V = list(map(int, input().split(' ')))
visit = [0 for _ in range(N + 1)]
adj = {}

for i in range(1, N + 1):
  adj[i] = []

for _ in range(M):
    x, y = list(map(int, input().split(' ')))
    adj[x].append(y)
    adj[y].append(x)

def dfs(v):
  print(v, end=' ')
  visit[v] = 1

  for i in range(1, N + 1):
    if i in adj[v] and visit[i] == 0:
      dfs(i)

def bfs(v):
  queue = deque([v])
  visit[v] = 1

  while queue:
    x = queue.popleft()
    print(x, end=' ')
    for i in range(1, N + 1):
      if i in adj[x] and visit[i] == 0:
        queue.append(i)
        visit[i] = 1

dfs(V)
visit = [0 for _ in range(N + 1)]
print()
bfs(V)