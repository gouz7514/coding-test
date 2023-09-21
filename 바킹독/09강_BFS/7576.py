# 토마토
# https://www.acmicpc.net/problem/7576
# 골드 5
# 나의 풀이
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
answer = 0

# 익어있는 토마토를 queue에 넣는다
for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      queue.append((i, j))

if not queue: # 익은 토마토가 하나도 없는 경우
  answer = -1
elif len(queue) == m * n: # 모두 익어있는 토마토인 경우
  answer = 0
else:
  dx = [1, 0, -1, 0]
  dy = [0, -1, 0, 1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 체크
      if (nx < 0 or nx >= n or ny < 0 or ny >= m):
        continue
      if tomato[nx][ny] == -1 or tomato[nx][ny] >= 1:
        continue
      if tomato[nx][ny] == 0:
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append((nx, ny))

  for i in range(n):
    for j in range(m):
      if tomato[i][j] == 0:
        answer = -1
        break
      else:
        answer = max(answer, tomato[i][j])
    if answer == -1:
      break
print(answer - 1 if answer > 0 else answer)

# 과거 나의 풀이
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()

for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      queue.append([i, j])

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
      arr[nx][ny] = arr[x][y] + 1
      queue.append([nx, ny])

result = -2
# 안 익은게 있는지 체크하는 플래그
check = False

for i in arr:
  for j in i:
    if j == 0:
      check = True
    result = max(result, j)

if check:
  print(-1)
elif result == -1:
  print(0)
else:
  print(result - 1)

# 다른 사람의 풀이
import sys
from collections import deque

readl = sys.stdin.readline

C, R = map(int, readl().split())
mat = [list(map(int, readl().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
  Q = deque()
  for r in range(R):
    for c in range(C):
      if mat[r][c] == 1:
        Q.append((r, c))
  while Q:
    r, c = Q.popleft()
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0 <= nr < R and 0 <= nc < C and mat[nr][nc] == 0:
        mat[nr][nc] = mat[r][c] + 1
        Q.append((nr, nc))

bfs()
res = 0
for l in mat:
  for v in l:
    if v == 0:
      print(-1)
      exit(0) # 이 부분이 신기하다!
  res = max(res, max(l))
print(res - 1)
