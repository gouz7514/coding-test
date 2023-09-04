# https://www.acmicpc.net/problem/10866
# 덱
# 실버 4
import sys

N = int(sys.stdin.readline().strip())

deque = []

for _ in range(N):
  command = sys.stdin.readline().strip().split(' ')
  if command[0] == 'push_front':
    deque = [int(command[1])] + deque
  if command[0] == 'push_back':
    deque.append(int(command[1]))
  if command[0] == 'pop_front':
    print(deque.pop(0)) if len(deque) else (print(-1))
  if command[0] == 'pop_back':
    print(deque.pop()) if len(deque) else print(-1)
  if command[0] == 'size':
    print(len(deque))
  if command[0] == 'empty':
    print(1) if len(deque) == 0 else print(0)
  if command[0] == 'front':
    print(deque[0]) if len(deque) else print(-1)
  if command[0] == 'back':
    print(deque[len(deque) - 1]) if len(deque) else print(-1)