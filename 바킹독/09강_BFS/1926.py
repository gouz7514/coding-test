# 그림
# https://www.acmicpc.net/problem/1926
# 실버 1
# 나의 풀이
import sys
input = sys.stdin.readline

board = []
n, m = list(map(int, input().split(' ')))
visited = [[False for i in range(m)] for j in range(n)]
# 그림의 개수
cnt = 0
# 가장 넓은 그림의 넓이
area = 0

for _ in range(n):
  board.append(list(map(int, input().split(' '))))

def bfs(x, y, result):
  # 이미 방문했다면 종료
  if visited[x][y]:
    return
  visited[x][y] = True
  if result == 0:
    return
  
  queue = []
  queue.append([x, y])

  while len(queue):
    x, y = queue.pop()
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 벗어나는지 체크
      if (nx < 0 or nx >= n or ny < 0 or ny >= m):
        continue
      if visited[nx][ny] or board[nx][ny] == 0:
        continue
      visited[nx][ny] = True
      queue.append([nx, ny])
      result += 1

  return result

for i in range(n):
  for j in range(m):
    result = bfs(i, j, int(board[i][j]))
    if result:
      cnt += 1
      area = max(area, result)

print(cnt)
print(area)

# 다른 사람의 풀이
# visited 배열을 굳이 만들지 않고 paint 배열을 그대로 사용
from collections import deque

N, M = map(int, input().split())
paint = []
size = []

for _ in range(N):
  paint.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(paint, x, y):
  q = deque()
  q.append((x, y))
  paint[x][y] = 0
  cnt = 1

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if paint[nx][ny] == 1:
        q.append((nx, ny))
        paint[nx][ny] = 0
        cnt += 1

  return cnt

for i in range(N):
  for j in range(M):
    if paint[i][j] == 1:
      size.append(bfs(paint, i, j))