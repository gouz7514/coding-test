# 불
# https://www.acmicpc.net/problem/5427
# 골드 4
# 나의 풀이 - 실패..
# from collections import deque

# for _ in range(int(input())):
#   w, h = map(int, input().split())
#   maze = [list(input()) for _ in range(h)]

#   sangeun = deque()
#   fire = deque()

#   dist_sangeun = [[-1 for _ in range(w)] for _ in range(h)]
#   dist_fire = [[-1 for _ in range(w)] for _ in range(h)]

#   answer = 0
#   isExit = False

#   for i in range(h):
#     for j in range(w):
#       if maze[i][j] == '*':
#         fire.append((i, j))
#       if maze[i][j] == '@':
#         sangeun.append((i, j))

#   dx = [1, 0, -1, 0]
#   dy = [0, -1, 0, 1]

#   while fire:
#     x, y = fire.popleft()

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or nx >= h or ny < 0 or ny >= w:
#         continue
#       if dist_fire[nx][ny] >= 0 or maze[nx][ny] == '#':
#         continue
#       dist_fire[nx][ny] = dist_fire[x][y] + 1
#       fire.append((nx, ny))

#   while sangeun:
#     x, y = sangeun.popleft()

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx < 0 or nx >= h or ny < 0 or ny >= w:
#         continue
#       if dist_sangeun[nx][ny] >= 0 or maze[nx][ny] == '*' or maze[nx][ny] == '#':
#         continue
#       if dist_sangeun[nx][ny] != -1 or dist_fire[nx][ny] <= dist_sangeun[x][y] + 1:
#         continue
#       dist_sangeun[nx][ny] = dist_sangeun[x][y] + 1
#       sangeun.append((nx, ny))

#       # 탈출 조건
#       if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
#         if dist_sangeun[nx][ny] < dist_fire[nx][ny]:
#           answer = dist_sangeun[nx][ny] + 1
#           isExit = True

#     if isExit:
#       break

#   print(answer + 1 if isExit else 'IMPOSSIBLE')
#####
# 다른 사람의 풀이
# https://velog.io/@yeomja99/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-5427%EB%B2%88-%EB%B6%88
import sys
from collections import deque

input = sys.stdin.readline

# 0: 방문하지 않음 1: 상근이 방문함 2: 불이 방문함
def bfs(f_s, queue, visit): #불의 bfs인지 상근의 bfs인지 체크
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    while (queue):
        x, y, time = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and nx< h and ny >=0 and ny <w:
                if graph[nx][ny] == '.' or graph[nx][ny] == '@':
                    if visit[nx][ny] > time + 1:
                        visit[nx][ny] = time + 1
                        queue.append((nx, ny, visit[nx][ny]))
            elif f_s == 's':  # 상근이면 w, h를 벗어나는 순간 스탑
                print(time + 1)
                return
    if f_s == 's':
        print("IMPOSSIBLE")


for _ in range(int(input())):
    w, h = list(map(int, input().split()))
    graph = [[0 for _ in range(w)]for _ in range(h)]
    visit = [[1e9 for _ in range(w)]for _ in range(h)]

    fqueue = deque()
    squeue = deque()

    for i in range(h):
        temp = sys.stdin.readline() # 공백이 없음
        for j in range(w):
            graph[i][j] = temp[j]
            if temp[j] == '@':
                squeue.append((i, j, 0))
            elif temp[j] == '*':
                visit[i][j] = 0
                fqueue.append((i, j, 0))

    print(graph)

    # 불 먼저 bfs
    bfs('f', fqueue, visit)
    print(visit)
    bfs('s', squeue, visit)