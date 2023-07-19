# 선분 위의 점
# https://www.acmicpc.net/problem/11663
# 실버 3
# 나의 풀이 - 정답
# import sys

# N, M = map(int, sys.stdin.readline().strip().split(' '))

# arr = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

# for _ in range(M):
#   x, y = map(int, sys.stdin.readline().strip().split(' '))

#   start, end, small, big = 0, N - 1, 0, 0

#   # arr에서 x보다 작은 원소 찾기
#   while start <= end:
#     mid = (start + end) // 2
#     if arr[mid] == x:
#       small = mid
#       break
#     elif arr[mid] < x:
#       small = mid + 1
#       start = mid + 1
#     else:
#       end = mid - 1

#   start, end = 0, N - 1

#   # arr에서 y보다 큰 원소 찾기
#   while start <= end:
#     mid = (start + end) // 2
#     if arr[mid] == y:
#       big = N - mid - 1
#       break
#     elif arr[mid] < y:
#       start = mid + 1
#     else:
#       big = N - mid
#       end = mid - 1
  
#   print(N - small - big)

# 다른 사람의 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([*map(int, input().split())])

def find_min_idx(num):
  s, e = 0, n - 1
  while s <= e:
    mid = (s + e) // 2
    if arr[mid] < num:
      s = mid + 1
    else:
      e = mid - 1
  
  return e + 1

def find_max_idx(num):
  s, e = 0, n - 1
  while s <= e:
    mid = (s + e) // 2
    if arr[mid] > num:
      e = mid - 1
    else:
      s = mid + 1

  return e

for _ in range(m):
  x, y = map(int, input().split())
  si = find_min_idx(x)
  ei = find_max_idx(y)
  print(ei - si + 1)