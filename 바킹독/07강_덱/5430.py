# AC
# https://www.acmicpc.net/problem/5430
# 골드 5
# 나의 풀이 - reverse 연산이 O(n)이므로 뒤집는 횟수가 홀수라면 뒤집는다
import sys
from collections import deque

for _ in range (int(sys.stdin.readline().strip())):
  isError = False
  commands = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline().strip())
  nums = sys.stdin.readline().strip()
  rev = 0
  
  if nums != '[]':
    nums = deque(list(nums[1:-1].split(',')))
  else:
    nums = []

  for command in commands:
    if command == 'R':
      rev += 1
    if command == 'D':
      if nums:
        if rev % 2 == 0:
          nums.popleft()
        else:
          nums.pop()
      else:
        isError = True
        break

  if isError:
    print('error')
  else:
    if rev % 2 == 0:
      print('[' + ','.join(list(nums)) + ']')
    else:
      nums.reverse()
      print('[' + ','.join(list(nums)) + ']')