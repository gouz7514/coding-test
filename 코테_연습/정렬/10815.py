# 숫자 카드
# https://www.acmicpc.net/problem/10815
# 이진 탐색 이용
# 나의 풀이
# 1. 비재귀
# import sys

# answer = []
# N = int(sys.stdin.readline())

# cards = list(map(int, sys.stdin.readline().strip().split()))
# cards.sort()

# M = int(sys.stdin.readline())

# nums = list(map(int, sys.stdin.readline().strip().split()))

# def binary_search(arr, target):
#   first, last = 0, len(arr) - 1

#   while first <= last:
#     mid = (first + last) // 2

#     if arr[mid] == target:
#       return 1
#     elif arr[mid] < target:
#       first = mid + 1
#     else:
#       last = mid - 1

#   return 0

# for n in nums:
#   result = binary_search(cards, n)
#   answer.append(result)

# print(" ".join(map(str, answer)))

# 2. 재귀
import sys

answer = []
N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().strip().split()))
cards.sort()

M = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().strip().split()))

start, end = 0, len(cards) -1

def binary_search(arr, target, first, last):
  if first > last:
    return 0
  
  mid = (first + last) // 2

  if arr[mid] == target:
    return 1
  elif arr[mid] < target:
    first = mid + 1
  else:
    last = mid - 1

  return binary_search(arr, target, first, last)

for n in nums:
  result = binary_search(cards, n, start, end)
  answer.append(result)

print(" ".join(map(str, answer)))

# 다른 사람의 풀이
# import sys

# n = int(sys.stdin.readline())
# s = set(sys.stdin.readline().split())
# m = int(sys.stdin.readline())
# data_m = sys.stdin.readline().split()

# count = ["1" if item in s else "0" for item in data_m]
# print(" ".join(count))