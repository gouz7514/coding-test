# 제곱근
# 실버 4
# https://www.acmicpc.net/problem/13706
# 나의 풀이 - 정답!
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())

def binary_search(target, start, end):
  mid = (start + end) // 2

  if mid == 1:
    return 1
  
  if mid * mid == target:
    return mid
  elif mid * mid > target:
    return binary_search(target, start, mid - 1)
  else:
    return binary_search(target, mid + 1, end)
  
print(binary_search(N, 1, N // 2))