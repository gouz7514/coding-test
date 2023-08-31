# 수들의 합
# https://www.acmicpc.net/problem/1789
# 실버 5
# 나의 풀이
s = int(input())

n = 1

while True:
  result = True if n * (n + 3) > 2 * s - 2 else False
  if result:
    break
  else:
    n += 1

print(n)

# 다른 사람의 풀이
s = int(input())
n = 0

while n < s:
  n += 1
  s -= n

print(n)