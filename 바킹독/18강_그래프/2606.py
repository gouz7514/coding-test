# 바이러스
# https://www.acmicpc.net/problem/2606
# 실버 3
# 나의 풀이
# 1번이 걸렸을 때, 1번을 통해 걸리게 되는 컴퓨터의 수니까 dfs 재귀 도는 횟수 카운트
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())

visit = [False for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
cnt = 0

def dfs(v):
  visit[v] = True
  global cnt

  for i in graph[v]:
    if not visit[i]:
      dfs(i)
      cnt += 1

for _ in range(int(input())):
  x, y = list(map(int, input().split(' ')))
  graph[x].append(y)
  graph[y].append(x)

dfs(1)
print(cnt)