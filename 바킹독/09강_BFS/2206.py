# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
# 골드 3
# 나의 풀이 - 시간 초과 (브루트포스니까 당연하다)
# 벽을 부수는 작업을 어떻게 해야 할까...
import sys
sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split(' ')))
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y, arr, visited, dist):
  queue = deque()
  queue.append((x, y, 0))
  visited[x][y] = True
  dist[x][y][0] = 1
  dist[x][y][1] = 1

  while queue:
    cx, cy, broken = queue.popleft()

    if cx == n - 1 and cy == m - 1:
      return dist[cx][cy][broken]

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if arr[nx][ny] == 0 and dist[nx][ny][broken] == 0:
        dist[nx][ny][broken] = dist[cx][cy][broken] + 1
        queue.append((nx, ny, broken))
      # (nx, ny를 부수는 경우)
      if not broken and arr[nx][ny] == 1 and dist[nx][ny][broken] == 0:
        dist[nx][ny][1] = dist[cx][cy][broken] + 1
        queue.append((nx, ny, 1))

  return -1

visited = [[False for _ in range(m)] for _ in range(n)]
dist = [[[0,0] for _ in range(m)] for _ in range(n)]

print(bfs(0, 0, arr, visited, dist))
print(dist)