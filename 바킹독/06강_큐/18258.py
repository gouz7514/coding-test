# 큐 2
# https://www.acmicpc.net/problem/18258
# 실버 4
# 나의 풀이 - pop()을 하는 과정에서 O(n)의 시간복잡도가 소요된다
# 따라서, quee or deque를 사용해야 한다
# import sys

# input = sys.stdin.readline
# queue = []

# for _ in range(int(input())):
#   command = input().strip().split(' ')

#   if command[0] == 'push':
#     queue.append(command[1])
#   elif command[0] == 'pop':
#     if queue:
#       print(queue[0])
#       del queue[0]
#     else:
#       print(-1)
#   elif command[0] == 'size':
#     print(len(queue))
#   elif command[0] == 'empty':
#     print(0) if queue else print(1)
#   elif command[0] == 'front':
#     print(queue[0]) if queue else print(-1)
#   elif command[0] == 'back':
#     print(queue[len(queue) - 1]) if queue else print(-1)
#####
import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

for _ in range(int(input())):
  command = input().strip().split(' ')

  if command[0] == 'push':
    queue.append(command[1])
  elif command[0] == 'pop':
    print(queue.popleft()) if len(queue) else print(-1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    print(0) if len(queue) else print(1)
  elif command[0] == 'front':
    print(queue[0]) if len(queue) else print(-1)
  elif command[0] == 'back':
    print(queue[len(queue) - 1]) if len(queue) > 0 else print(-1)