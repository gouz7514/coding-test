# 미로 탐색
# https://www.acmicpc.net/problem/2178
# 실버 1
# 나의 풀이
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):  
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 체크
      if (nx < 0 or nx >= n or ny < 0 or ny >= m):
        continue
      if maze[nx][ny] == 0:
        continue
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))

  return maze[n-1][m-1]
  
print(bfs(0, 0))
print(maze)

# 나의 과거 코드
# from collections import deque

# N, M = map(int, input().split())
# arr = [list(map(int, list(input()))) for _ in range(N)]

# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))

#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             nx = a + dx[i]
#             ny = b + dy[i]
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#             if arr[nx][ny] == 0:
#                 continue
#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = arr[a][b] + 1
#                 queue.append((nx, ny))
#     return arr[N-1][M-1]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# print(bfs(0,0))
