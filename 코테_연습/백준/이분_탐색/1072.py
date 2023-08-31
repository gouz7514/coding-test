# 게임
# 실버 3
# https://www.acmicpc.net/problem/1072
# 나의 풀이 - 정답
import sys

X, Y = map(int, sys.stdin.readline().strip().split(' '))
# 초기 승률
Z = Y * 100 // X

start, end, answer = 0, X, 1

# 99% 이상 승률은 더 올라갈 수 없다
if Z >= 99:
  answer = -1
else:
  while start <= end:
    mid = (start + end) // 2

    new_Z = (mid + Y) * 100 // (mid + X)

    if new_Z > Z:
      if new_Z == Z + 1:
        answer = mid
        end = mid - 1
      else:
        end = mid - 1
    else:
      start = mid + 1

print(answer)

# 나의 풀이 - 간단하게
import sys

X, Y = map(int, sys.stdin.readline().strip().split(' '))
Z = Y * 100 // X
start, end, answer = 0, X, 1

if Z >= 99:
  answer = -1
else:
  while start <= end:
    mid = (start + end) // 2

    new_Z = (mid + Y) * 100 // (mid + X)

    if new_Z > Z:
      answer = mid
      end = mid - 1
    else:
      start = mid + 1

print(answer)

# 다른 사람의 풀이
import math

x, y = map(int, input().split(" "))
z = y*100//x
if z >=99:
    print(-1)
else:
    n1 = (z+1)*x-100*y
    n2 = (99-z)

    print(math.ceil(n1/n2))