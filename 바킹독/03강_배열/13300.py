# 방 배정
# https://www.acmicpc.net/problem/13300
# 브론즈 2
# 나의 풀이 - 방에 한 명이라도 들어가면 cnt += 1, k명 되면 다시 비움
n, k = list(map(int, input().split(' ')))
arr = [0 for i in range(12)]
cnt = 0

for _ in range(n):
  s, y = list(map(int, input().split(' ')))
  idx = s + (y - 1) * 2
  arr[idx] += 1

for a in arr:
  if a:
    if a % k == 0:
      cnt += a // k
    else:
      cnt += (a // k + 1)

print(cnt)