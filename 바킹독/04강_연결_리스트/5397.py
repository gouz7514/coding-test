# 키로거
# https://www.acmicpc.net/problem/5397
# 실버 2
# 나의 풀이
import sys

for _ in range(int(sys.stdin.readline().strip())):
  orders = list(sys.stdin.readline().strip())
  arr = []
  arr2 = []

  for a in orders:
    if a == '<':
      arr2.append(arr.pop()) if arr else None
    elif a == '>':
      arr.append(arr2.pop()) if arr2 else None
    elif a == '-':
      arr.pop() if arr else None
    else:
      arr.append(a)

  print(''.join(arr + list(reversed(arr2))))