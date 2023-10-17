# 적록색약
# https://www.acmicpc.net/problem/10026
# 골드 5
# 나의 풀이
# from collections import deque

# paint = []
# cnt_normal = 0
# cnt_rg = 0

# N = int(input())

# visited = [[False for _ in range(N)] for _ in range(N)]

# for _ in range(N):
#   paint.append(list(input()))

# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# # 적록색약 아닌 사람
# def bfs(paint, x, y, visited):
#   queue = deque()
#   queue.append((x, y))
#   visited[x][y] = True

#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or nx >= N or ny < 0 or ny >= N:
#         continue
#       if not visited[nx][ny] and paint[nx][ny] == paint[x][y]:
#         queue.append((nx, ny))
#         visited[nx][ny] = True

#   return


# for i in range(N):
#   for j in range(N):
#     if not visited[i][j]:
#       bfs(paint, i, j, visited)
#       cnt_normal += 1

# # 적록색약인 경우
# def bfs_special(paint, x, y, visited):
#   queue = deque()
#   queue.append((x, y))
#   visited[x][y] = True

#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or nx >= N or ny < 0 or ny >= N:
#         continue
#       if not visited[nx][ny]:
#         if paint[x][y] == 'R' or paint[x][y] == 'G':
#           if paint[nx][ny] == 'R' or paint[nx][ny] == 'G':
#             queue.append((nx, ny))
#             visited[nx][ny] = True
#         else:
#           if paint[nx][ny] == 'B':
#             queue.append((nx, ny))
#             visited[nx][ny] = True

#   return

# visited = [[False for _ in range(N)] for _ in range(N)]

# for i in range(N):
#   for j in range(N):
#     if not visited[i][j]:
#       bfs_special(paint, i, j, visited)
#       cnt_rg += 1

# print(cnt_normal)
# print(cnt_rg)

# 다른 사람의 풀이
# 적록색약은 R, G 를 같은 색깔로 보니까 G를 R로 바꿔도 된다
# 굳이 새로운 bfs 알고리즘 구현하지 않아도 된다
from collections import deque

N = int(input())
paint = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

cnt1 = 0
cnt2 = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if visited[nx][ny]:
        continue
      if paint[x][y] != paint[nx][ny]:
        continue
      visited[nx][ny] = True
      queue.append((nx, ny))

for i in range(N):
  for j in range(N):
    if visited[i][j]:
      continue
    bfs(i, j)
    cnt1 += 1

# 적록색약은 G를 R로 초기화
for i in range(N):
  for j in range(N):
    if paint[i][j] == 'G':
      paint[i][j] = 'R'

visited = [[False] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if visited[i][j]:
      continue
    bfs(i, j)
    cnt2 += 1

print(cnt1)
print(cnt2)