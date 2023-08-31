# 암기왕
# 실버 4
# https://www.acmicpc.net/problem/2776
# 나의 풀이
# 1. 테스트 케이스 여러 개 들어오는 거 고려 안함
# 2. 시간초과
# 이분탐색이 시간 초과가 나면 어떻게 해야하지
# import sys

# T = int(sys.stdin.readline())

# for _ in range(T):
#   N = int(sys.stdin.readline().strip())
#   A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

#   M = int(sys.stdin.readline().strip())
#   B = list(map(int, sys.stdin.readline().strip().split(' ')))

#   words = dict()

#   for a in A:
#     words[a] = True

#   for b in B:
#     if b in words:
#       print(1)
#     else:
#       print(0)

# 다른 사람의 풀이
# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#   n = int(input())
#   note1 = set(map(int, input().split()))
#   m = int(input())
#   note2 = set(map(int, input().split()))

#   for j in note2:
#     print(1 if j in note1 else 0)

# 나의 풀이 2
# import sys
# sys.setrecursionlimit(10**6)

# T = int(input())

# def binary_search(arr, val, first, last):
#   if first > last:
#     return 0
  
#   mid = (first + last) // 2

#   if arr[mid] == val:
#     return 1
#   elif arr[mid] < val:
#     first = mid + 1
#   else:
#     last = mid - 1

#   return binary_search(arr, val, first, last)

# for _ in range(T):
#   N = int(sys.stdin.readline().strip())
#   A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

#   M = int(sys.stdin.readline().strip())
#   B = list(map(int, sys.stdin.readline().strip().split(' ')))

#   for b in B:
#     print(binary_search(A, b, 0, N - 1))

# 다른 사람의 풀이 2
# 재귀 이진탐색
import sys
sys.setrecursionlimit(10**6)

T = int(input())

def binary_search(arr, s, e, t):
  if s > e:
    return 0
  mid = (s + e) // 2
  if arr[mid] == t:
    return 1
  elif arr[mid] > t:
    return binary_search(arr, s, mid - 1, t)
  else:
    return binary_search(arr, mid + 1, e, t)

for _ in range(T):
  N = int(sys.stdin.readline().strip())
  A = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

  M = int(sys.stdin.readline().strip())
  B = list(map(int, sys.stdin.readline().strip().split(' ')))

  for b in B:
    print(binary_search(A, 0, N - 1, b))