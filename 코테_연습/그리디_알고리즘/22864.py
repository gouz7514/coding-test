# 피로도
# https://www.acmicpc.net/problem/22864
# 브론즈 2
# 나의 풀이
import sys

# 피로도+, 일, 피로도-, 최대 피로도
A, B, C, M = map(int, sys.stdin.readline().strip().split(' '))

work, day, cur = 0, 24, 0 # 총 일한 양, 하루 시간, 현재 피로도

for i in range(day):
  if A > M:
    break
  if cur + A <= M: # 일할 수 있다면
    work += B
    cur += A
  else:
    cur = max(cur - C, 0) #  단, 피로도가 음수로 내려가면 0으로 바뀐다.

print(work)