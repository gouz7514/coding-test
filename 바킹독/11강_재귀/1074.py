# Z
# https://www.acmicpc.net/problem/1074
# 실버 1 - 으아아아아
N, r, c = list(map(int, input().split()))

def func(n, r, c):
  if n == 0:
    return 0
  half = 2 ** (n - 1)
  if r < half and c < half:
    return func(n-1, r, c)
  if r < half and c >= half:
    return half * half + func(n-1, r, c-half)
  if r >= half and c < half:
    return 2 * half * half + func(n-1, r-half, c)
  return 3*half*half + func(n-1, r-half, c-half)

print(func(N, r, c))