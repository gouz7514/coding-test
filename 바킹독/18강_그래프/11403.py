# 경로 찾기
# https://www.acmicpc.net/problem/11403
# 실버 1
# 나의 풀이 - 25분
# 각 노드에 대해 dfs 순회하면서 연결된 노드 모두 찾는다
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, list(input().strip().split(' ')))) for _ in range(N)]
adj = []
answer = []

for a in arr:
  list = []
  for i in range(len(a)):
    if a[i] == 1:
      list.append(i)
  adj.append(list)

def dfs(v, result):

  for i in adj[v]:
    if not visit[i]:
      result[i] = 1
      visit[i] = True
      dfs(i, result)

  return result

for a in range(N):
  visit = [False for _ in range(N)]
  answer.append(dfs(a, [0 for _ in range(N)]))

for a in answer:
  print(*a)

# 다른 사람의 풀이
# graph 자체를 인접리스트처럼 사용할 수 있네!
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(num):
  for j in range(n):
    if graph[num][j] and not visited[j]:
      visited[j] = 1
      dfs(j)

visited = [0] * n

for i in range(n):
  dfs(i)
  print(' '.join(map(str, visited)))
  visited = [0] * n