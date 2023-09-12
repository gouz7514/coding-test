# 두 수의 합
# https://www.acmicpc.net/problem/3273
# 실버 3
import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
x = int(sys.stdin.readline().strip())

nums.sort()
start, end, cnt = 0, n - 1, 0

while start < end:
  if nums[start] + nums[end] == x:
    cnt += 1
    start += 1
    end -= 1
  elif nums[start] + nums[end] > x:
    end -= 1
  else:
    start += 1

print(cnt)