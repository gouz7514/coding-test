# 우유 축제
# https://www.acmicpc.net/problem/14720
# 브론즈 3
# 나의 풀이
import sys

N = int(sys.stdin.readline().strip())

milks = list(map(int, sys.stdin.readline().strip().split(' ')))
cur, answer = 0, 0 # 현재 마셔야 할 우유, 총 마신 우유

for milk in milks:
  if cur == milk:
    cur = (cur + 1) % 3
    answer += 1

print(answer)