# 홀수
# https://www.acmicpc.net/problem/2576
# 브론즈 3
# 나의 풀이
import sys

minimum = sys.maxsize
answer = 0

for _ in range(7):
  n = int(input())
  if n % 2 == 1:
    answer += n
    minimum = min(minimum, n)

if answer == 0:
  print(-1)
else:
  print(answer)
  print(minimum)