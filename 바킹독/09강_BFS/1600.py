# 말이 되고픈 원숭이
# https://www.acmicpc.net/problem/1600
# 골드 3
# 나의 풀이 - 반례가 무엇일까..
# import sys
# from collections import deque

# input = sys.stdin.readline

# # 원숭이는 K번만 말처럼 움직일 수 있다
# K = int(input())
# W, H = list(map(int, input().split(' ')))
# arr = [list(map(int, input().split(' '))) for _ in range(H)]

# # 원숭이의 이동 방식
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# # 말의 이동 방식
# hx = [-2, -2, -1, -1, 1, 1, 2, 2]
# hy = [1, -1, 2, -2, 2, -2, 1, -1]

# def bfs(x, y, visited, dist):
#   queue = deque()
#   queue.append((x, y, 0))
#   visited[x][y] = True

#   while queue:
#     cx, cy, cnt = queue.popleft() # cnt : 말처럼 이동한 횟수

#     if cx == H - 1 and cy == W - 1:
#       return dist[cx][cy]
    
#     # 나이트의 이동을 먼저 진행
#     if cnt < K:
#       for i in range(8):
#         nx = cx + hx[i]
#         ny = cy + hy[i]

#         if nx < 0 or nx >= H or ny < 0 or ny >= W:
#           continue
#         if arr[nx][ny] == 1 or visited[nx][ny]:
#           continue
#         visited[nx][ny] = True
#         queue.append((nx, ny, cnt + 1))
#         dist[nx][ny] = dist[cx][cy] + 1

#     # 원숭이의 이동
#     for i in range(4):
#       nx = cx + dx[i]
#       ny = cy + dy[i]

#       if nx < 0 or nx >= H or ny < 0 or ny >= W:
#         continue
#       if arr[nx][ny] == 1 or visited[nx][ny]:
#         continue
#       visited[nx][ny] = True
#       queue.append((nx, ny, cnt))
#       dist[nx][ny] = dist[cx][cy] + 1

#   return -1


# visited = [[False for _ in range(W)] for _ in range(H)]
# dist = [[0 for _ in range(W)] for _ in range(H)]
# print(bfs(0, 0, visited, dist))

# 바킹독 풀이
# K번까지 나이트처럼 이동가능하므로 해당 경우를 visited사용해서 구현한다
import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
W, H = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for _ in range(H)]
visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K + 1)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [1, -1, 2, -2, 2, -2, 1, -1]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

while queue:
  cnt, cx, cy = queue.popleft()

  if cnt < K:
    for i in range(8):
      nx = cx + hx[i]
      ny = cy + hy[i]

      if nx < 0 or nx >= H or ny < 0 or ny >= W:
        continue
      if arr[nx][ny]:
        continue
      if visited[cnt + 1][nx][ny]:
        continue
      visited[cnt + 1][nx][ny] = visited[cnt][cx][cy] + 1
      queue.append((cnt + 1, nx, ny))

  for i in range(4):
    nx = cx + dx[i]
    ny = cy + dy[i]

    if nx < 0 or nx >= H or ny < 0 or ny >= W:
      continue
    if arr[nx][ny] == 1 or visited[cnt][nx][ny]:
      continue
    visited[cnt][nx][ny] = visited[cnt][cx][cy] + 1
    queue.append((cnt, nx, ny))

answer = float('inf')
for i in range(K + 1):
  if visited[i][H - 1][W - 1]:
    answer = min(answer, visited[i][H - 1][W - 1])
if answer != float('inf'):
  print(answer - 1)
else:
  print(-1)