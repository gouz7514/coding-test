# 회전하는 큐
# https://www.acmicpc.net/problem/1021
# 실버 3
# 나의 풀이
import sys
from collections import deque
input = sys.stdin.readline
answer = 0

N, M = list(map(int, input().split(' ')))
locations = list(map(int, input().split(' ')))
arr = deque([i for i in range(1, N + 1)])

for location in locations:
  while arr[0] != location:
    idx = arr.index(location)
    if idx >= len(arr) - idx:
      right = arr.pop()
      arr.appendleft(right)
      answer += 1
    else:
      left = arr.popleft()
      arr.append(left)
      answer += 1
  arr.popleft()

print(answer)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# [3, 4, 5, 6, 7, 8, 9, 10, 1]
# [1, 3, 4, 5, 6, 7, 8, 9, 10]
# [10, 1, 3, 4, 5, 6, 7, 8, 9]
# [9, 10, 1, 3, 4, 5, 6, 7, 8]
# [10, 1, 3, 4, 5, 6, 7, 8]