# 핸드폰 요금
# https://www.acmicpc.net/problem/1267
# 브론즈 3
# 나의 풀이
N = int(input())
calls = list(map(int, input().split(' ')))
M, Y = 0, 0
answer =[]

for call in calls:
  Y += (call // 30 + 1) * 10
  M += (call // 60 + 1) * 15

cheap = 'Y' if Y < M else ('M' if Y > M else 'Y M')
cost = Y if Y <= M else M
print(cheap, cost)