# 회장뽑기
# https://www.acmicpc.net/problem/2660
# 골드 5
# 나의 풀이 - 25분!
# bfs로 가는게 맞고, 거리 측정해야 한다
# 자기 자신으로 가는 거 막기 위해 visit 배열 활용
# 여기서 메모리를 줄이려면 dist 배열 대신 다른 방법 사용할 수 있을 것 같다
# from collections import deque
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# score = dict()

# while True:
#   i, j = list(map(int, input().split(' ')))

#   if i == -1 and j == -1:
#     break

#   graph[i].append(j)
#   graph[j].append(i)

# def bfs(start):
#   queue = deque([start])
#   visit[start] = True

#   while queue:
#     x = queue.popleft()

#     for i in graph[x]:
#       if not dist[i] and not visit[i]:
#         dist[i] = dist[x] + 1
#         visit[i] = True
#         queue.append(i)

# for i in range(1, n + 1):
#   dist = [0 for _ in range(n + 1)]
#   visit = [False for _ in range(n + 1)]
#   bfs(i)
#   if max(dist) in score:
#     score[max(dist)].append(i)
#   else:
#     score[max(dist)] = [i]

# sorted_score = sorted(score.items())
# print(sorted_score[0][0], len(sorted_score[0][1]))
# print(*sorted(sorted_score[0][1]))

# 나의 풀이 보완
# from collections import deque
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n + 1)]
# score = [0 for _ in range(n + 1)]

# while True:
#   i, j = list(map(int, input().split(' ')))

#   if i == -1 and j == -1:
#     break

#   graph[i].append(j)
#   graph[j].append(i)

# def bfs(start):
#   queue = deque()
#   queue.append((start, 0))
#   visit[start] = 1

#   while queue:
#     x, dist = queue.popleft()

#     for i in graph[x]:
#       if not visit[i]:
#         queue.append((i, dist + 1))
#         visit[i] = dist + 1

# for i in range(1, n + 1):
#   visit = [0 for _ in range(n + 1)]
#   bfs(i)
#   score[i] = max(visit)

# cand = []
# cnt = 0
# for i, val in enumerate(score[1:]):
#   if val == min(score[1:]):
#     cand.append(i + 1)
#     cnt += 1
# print(min(score[1:]), cnt)
# print(*cand)

# 다른 사람의 풀이
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

while True:
  a, b = map(int, input().split())
  if a == -1 and b == -1:
      break
  graph[a].append(b)
  graph[b].append(a)

def bfs(s, visited):
  visited[s] = 1
  q = deque()
  q.append((s, 0))

  while q:
    x, dist = q.popleft()
    for nx in graph[x]:
      if visited[nx]:
        continue
      q.append((nx, dist + 1))
      visited[nx] = dist + 1

def sol():
  arr = [sys.maxsize] * (n + 1)
  for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i, visited)
    arr[i] = max(visited)
  print(arr)
  cand = []
  cnt = 0
  for i, val in enumerate(arr):
    if val == min(arr):
      cand.append(i)
      cnt += 1
  print(min(arr), cnt)
  print(*cand)

sol()