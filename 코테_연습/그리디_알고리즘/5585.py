# 거스름돈
# https://www.acmicpc.net/problem/5585
# 브론즈 2
# 나의 풀이
cost = int(input())
coins = [500, 100, 50, 10, 5, 1]

def greedy(coins, change):
  coins.sort(reverse = True)
  cnt = 0

  for coin in coins:
    cnt += change // coin
    change %= coin

  return cnt

print(greedy(coins, 1000 - cost))