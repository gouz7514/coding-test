# 빙산
# https://www.acmicpc.net/problem/2573
# 골드 4
# 나의 풀이
from collections import deque

N, M = map(int, input().split())

ice = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def count_icebergs():
  visited = [[False] * M for _ in range(N)]
  cnt = 0

  for i in range(N):
    for j in range(M):
      if ice[i][j] > 0 and not visited[i][j]:
        bfs(i, j, visited)
        cnt += 1

  return cnt

# 녹이는 함수
def melt(ice):
  # 바닷물과 접해있는 갯수 카운트
  melt_cnt = [[0] * M for _ in range(N)]

  for i in range(N):
    for j in range(M):
      if ice[i][j] != 0:
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          
          if ice[nx][ny] == 0:
            melt_cnt[i][j] += 1
  
  for i in range(N):
    for j in range(M):
      if melt_cnt[i][j]:
        ice[i][j] = ice[i][j] - melt_cnt[i][j] if ice[i][j] >= melt_cnt[i][j] else 0
  return ice

def bfs(x, y, visited):
  queue = deque([(x, y)])
  visited[x][y] = True

  while queue:
    cx, cy = queue.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if visited[nx][ny] or ice[nx][ny] == 0:
        continue
      visited[nx][ny] = True
      queue.append((nx, ny))

year = 0

while True:
  cnt = count_icebergs()
  if cnt == 0:
    print(0)
    break
  elif cnt >= 2:
    print(year)
    break

  ice = melt(ice)
  year += 1