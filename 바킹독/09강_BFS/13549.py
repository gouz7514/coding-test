# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 골드 5
# 나의 풀이 - 좀 오래 걸렸지만 해결!
# 더 빠르게 이동하는 경우 즉, 순간이동하는 경우를 먼저 고려해야 한다
from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(100001)]
seconds = [0 for _ in range(100001)]

queue = deque([N])

if N == K:
  print(0)
else:
  def bfs(x):
    isExit = False
    visited[x] = True

    while queue:
      x = queue.popleft()
      arr = [x * 2, x - 1, x + 1]

      for i in range(len(arr)):
        # 범위 벗어나는지 체크
        if arr[i] < 0 or arr[i] > 100000:
          continue
        # 이미 방문했는지 체크
        if visited[arr[i]]:
          continue
        visited[arr[i]] = True
        queue.append(arr[i])
        if i > 0:
          seconds[arr[i]] = seconds[x] + 1
        else:
          seconds[arr[i]] = seconds[x]
        if arr[i] == K:
          print(seconds[arr[i]])
          isExit = True
          break
      
      if isExit:
        break

  bfs(N)

# 다른 사람의 풀이
from collections import deque

N, K = map(int, input().split())
MAX = [100001]
distance = [-1] * MAX

def bfs(start):
  queue = deque()
  queue.append(start)
  distance[start] = 0

  while queue:
    now = queue.popleft()
    if now == K:
      return distance[now]
    for next in (now * 2, now - 1, now + 1):
      if 0 <= next < MAX and distance[next] == -1:
        if next == now * 2:
          distance[next] = distance[now]
          queue.appendleft(next)
        else:
          distance[next] = distance[now] + 1
          queue.append(next)

print(bfs(N))