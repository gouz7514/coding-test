# 세탁소 사장 동혁
# https://www.acmicpc.net/problem/2720
# 브론즈 3
# 나의 풀이
import sys

coins = [25, 10, 5, 1]

for _ in range(int(sys.stdin.readline().strip())):
  cost = int(input())
  result = []

  for coin in coins:
    result.append(cost // coin)
    cost %= coin

  print(*result)