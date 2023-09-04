# 캠핑
# https://www.acmicpc.net/problem/4796
# 브론즈 1
# 나의 풀이
import sys

case = 1

while True:
  answer = 0
  L, P, V = map(int, sys.stdin.readline().strip().split(' '))

  if L == 0 and P == 0 and V == 0:
    break

  answer = (V // P) * L + min(V % P, L)
  print(f'Case {case}: {answer}')
  case += 1