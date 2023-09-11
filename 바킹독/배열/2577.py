# 숫자의 개수
# https://www.acmicpc.net/problem/2577
# 브론즈 2
# 나의 풀이
a = int(input())
b = int(input())
c = int(input())

res = a * b * c
arr = [0] * 10

while res > 0:
  arr[res % 10] += 1
  res //= 10

for a in arr:
  print(a)