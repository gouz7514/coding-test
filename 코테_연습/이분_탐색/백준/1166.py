# 선물
# 실버 3
# https://www.acmicpc.net/problem/1166
# 나의 풀이 - 실패..
import sys

N, L, W, H = map(int, sys.stdin.readline().strip().split(' '))

start, end = 0, max([L, W, H])

for _ in range(10000):
  mid = (start + end) // 2
  result = (L // mid) * (W // mid) * (H // mid)

  if result >= N:
    start = mid
  else:
    end = mid

print("%.10f" %(end))

# 다른 사람의 풀이
import sys

N, L, W, H = map(int, sys.stdin.readline().strip().split(' '))
start, end = 0, max(L, W, H)

while end - start > 0.00000001:
  mid = (start + end) / 2
  if (L // mid) * (W // mid) * (H // mid) >= N:
    start = mid
  else:
    end = mid

print("%.10f" %(end))

# 다른 사람의 풀이 2
import sys

N, L, W, H = map(int, sys.stdin.readline().split())
S, E = 0, max(L, W, H)

for _ in range(10000):
    M = (S + E) / 2
    count = (L // M) * (W // M) * (H // M)
    if count >= N:
        S = M
    else:
        E = M

print("%.10f" %(E))