# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
# 실버 2
# 나의 풀이 - bfs 순회할 때마다 cnt+1
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))
visit = [False for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
cnt = 0

for _ in range(M):
  u, v = list(map(int, input().split(' ')))
  graph[u].append(v)
  graph[v].append(u)

def dfs(v):
  visit[v] = True

  for i in graph[v]:
    if not visit[i]:
      dfs(i)

for i in range(1, N + 1):
  if not visit[i]:
    dfs(i)
    cnt += 1

print(cnt)