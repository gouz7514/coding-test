# 프린터 큐
# 실버 3
# https://www.acmicpc.net/problem/1966
# 나의 풀이
import sys

for _ in range(int(sys.stdin.readline().strip())):
  N, M = map(int, sys.stdin.readline().strip().split(' '))
  priorities = list(map(int, sys.stdin.readline().strip().split(' ')))
  answer = 0
  
  queue = [(i, p) for i, p in enumerate(priorities)]

  while queue:
    element = queue.pop(0)
    if any(element[1] < q[1] for q in queue):
      queue.append(element)
    else:
      answer += 1
      if element[0] == M:
        break

  print(answer)
