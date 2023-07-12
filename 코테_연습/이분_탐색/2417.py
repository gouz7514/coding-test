# 정수 제곱근
# 실버 4
# https://www.acmicpc.net/problem/2417
import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

def binary_search(target, start, end):
  mid = (start + end) // 2

  if mid <= 1:
    return mid
  
  if mid ** 2 == target:
    return mid
  elif mid ** 2 > target:
    if (mid - 1) ** 2 == target:
      return mid - 1
    elif (mid - 1) ** 2 < target:
      return mid
    else:
      return binary_search(target, start, mid - 2)
  else: # mid ** 2 < target
    if (mid + 1) ** 2 == target:
      return mid + 1
    elif (mid + 1) ** 2 > target:
      return mid + 1
    else:
      return binary_search(target, mid + 2, end)
    
print(binary_search(n, 1, n))