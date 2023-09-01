# https://www.acmicpc.net/problem/10845
# 실버 4
# 나의 풀이
import sys

N = int(sys.stdin.readline().strip())

queue = []

for _ in range(N):
  command = sys.stdin.readline().strip().split(' ')
  if command[0] == 'push':
    queue.append(int(command[1]))
  if command[0] == 'pop':
    if len(queue):
      print(queue[0])
      del queue[0]
    else:
      print(-1)
  if command[0] == 'size':
    print(len(queue))
  if command[0] == 'empty':
    print(1) if len(queue) == 0 else print(0)
  if command[0] == 'front':
    print(queue[0]) if len(queue) else print(-1)
  if command[0] == 'back':
    print(queue[len(queue) - 1]) if len(queue) else print(-1)