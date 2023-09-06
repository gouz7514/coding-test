# 카드 역배치
# https://www.acmicpc.net/problem/10804
# 브론즈 2
# 나의 풀이
arr = [i for i in range(1, 21)]

for _ in range(10):
  X, Y = list(map(int, input().split(' ')))
  arr[X-1:Y] = arr[X-1:Y][::-1]

print(*arr)