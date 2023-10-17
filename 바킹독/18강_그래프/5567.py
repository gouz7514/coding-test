# 결혼식
# https://www.acmicpc.net/problem/5567
# 실버 2
# 나의 풀이
# 1번과 친구, 걔네와 친구인 애들만 보면 되니까 이렇게 풀었는데... 맘에 들지 않는다
# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n = int(input())

# visit = [False for _ in range(n+1)]
# graph = [[] for _ in range(n+1)]
# cnt = 0

# for _ in range(int(input())):
#   x, y = list(map(int, input().split(' ')))
#   graph[x].append(y)
#   graph[y].append(x)

# for i in graph[1]:
#   if not visit[i]:
#     visit[i] = True
#     cnt += 1

#   for j in graph[i]:
#     if j != 1 and not visit[j]:
#       cnt += 1
#       visit[j] = True

# print(cnt)

# 다른 사람의 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     u,v = map(int,input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# q = [(0, 1)]

# invited = set()
# while q:
#   d, v = q.pop()

#   if d <= 2:
#     if d <= 1:
#       for ad in graph[v]:
#         if ad not in invited:
#           q.append((d + 1, ad))
#     invited.add(v)

# print(len(invited) - 1)

# 다른 사람의 풀이 (BFS)
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visited[next]:
                visited[next] = visited[x] + 1
                q.append(next)

n = int(input())
m = int(input())
visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(visited)