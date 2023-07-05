# 30
# https://www.acmicpc.net/problem/10610
# 나의 풀이
import sys

N = list(map(int, sys.stdin.readline().strip()))

if 0 in N:
  if sum(N) % 3 == 0:
    N.sort(reverse = True)
    print(''.join(map(str, N)))
  else:
    print(-1)
else:
  print(-1)


# 다른 사람의 풀이
N = list(map(int, input()))

if 0 not in N or sum(N) % 3 != 0:
  print(-1)
else:
  N.sort(reverse = True)

  for x in N:
    print(x, end = '')