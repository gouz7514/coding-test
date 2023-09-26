# 불!
# https://www.acmicpc.net/problem/4179
# 골드 4
# 나의 풀이 - 출발점이 두개
# from collections import deque

# r, c = map(int, input().split())
# maze = [list(input()) for _ in range(r)]

# jihoon = deque()
# fire = deque()
# temp_fire = deque()
# answer = 0
# isExit = False

# for i in range(r):
#   for j in range(c):
#     if maze[i][j] == 'J':
#       jihoon.append((i, j))
#     if maze[i][j] == 'F':
#       fire.append((i, j))

# # 지훈이 먼저 이동
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]

# while jihoon:
#   x, y = jihoon.popleft()

#   if x == 0 or x == r - 1 or y == c - 1:
#     isExit = True
#     break

#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

#     if (nx < 0 or nx >= r or ny < 0 or ny >= c):
#       continue
#     if maze[nx][ny] == '#' or maze[nx][ny] == 'F':
#       continue
#     if maze[nx][ny] == '.':
#       jihoon.append((nx, ny))
#       maze[nx][ny] = 'J'
#       answer += 1
#       if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
#         isExit = True
#         break

#   print('fire : ', fire)
#   while fire:
#     a, b = fire.popleft()

#     for j in range(4):
#       na = a + dx[j]
#       nb = b + dy[j]

#       if na < 0 or na >= r or nb < 0 or nb >= c:
#         continue
#       if maze[na][nb] == '#' or maze[na][nb] == 'F':
#         continue
#       temp_fire.append((na, nb))
#       maze[na][nb] = 'F'

#   fire = temp_fire

# print(answer + 1 if isExit else 0)

# 바킹독 해설
# 1. 각 칸에 불이 전파되는 시간을 구한다
# 2. 지훈이가 이동하면서 가능한 경우를 체크한다
# 3. 지훈이 탈출 가능할 때 바로 탈출
from collections import deque

r, c = map(int, input().split())
maze = [list(input()) for _ in range(r)]

fire = deque()
jihoon = deque()

dist_jihoon = [[-1 for _ in range(c)] for _ in range(r)]
dist_fire = [[-1 for _ in range(c)] for _ in range(r)]

answer = 0
isExit = False

for i in range(r):
  for j in range(c):
    if maze[i][j] == 'F':
      fire.append((i, j))
    if maze[i][j] == 'J':
      jihoon.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while fire:
  x, y = fire.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      continue
    if dist_fire[nx][ny] >= 0 or maze[nx][ny] == '#':
      continue
    dist_fire[nx][ny] = dist_fire[x][y] + 1
    fire.append((nx, ny))

while jihoon:
  x, y = jihoon.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 지훈이가 범위를 벗어났다는 것은 탈출에 성공했다는 것
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      answer = dist_jihoon[x][y] + 1
      isExit = True
      break
    if dist_jihoon[nx][ny] >= 0 or maze[nx][ny] == 'F' or maze[nx][ny] == '#':
      continue
    if dist_fire[nx][ny] != -1 and dist_fire[nx][ny] <= dist_jihoon[x][y] + 1:
      continue
    dist_jihoon[nx][ny] = dist_jihoon[x][y] + 1
    jihoon.append((nx, ny))

  if isExit:
    break

print(answer + 1 if isExit else 'IMPOSSIBLE')