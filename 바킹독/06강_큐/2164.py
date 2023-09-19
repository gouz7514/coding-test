# 카드2
# https://www.acmicpc.net/problem/2164
# 실버 4
# 나의 풀이
from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])

while len(queue) > 1:
  queue.popleft()
  if len(queue) == 1:
    break

  left = queue.popleft()
  queue.append(left)

print(queue[0])