# CD
# 실버 5
# https://www.acmicpc.net/problem/4158
# 나의 풀이
# 0 0 을 입력받는 조건을 해결하지 못함, 시간 초과
# import sys
# sys.setrecursionlimit(10**6)

# while True:
#   answer = 0
#   N, M = map(int, sys.stdin.readline().strip().split(' '))

#   if N == 0 and M == 0:
#     break

#   A, B = [], []

#   for _ in range(N):
#     A.append(int(sys.stdin.readline().strip()))

#   for _ in range(M):
#     B.append(int(sys.stdin.readline().strip()))

#   def binary_search(arr, val):
#     first, last = 0, len(arr) - 1

#     while first <= last:
#       mid = (first + last) // 2

#       if arr[mid] == val:
#         return mid
#       elif arr[mid] < val:
#         first = mid + 1
#       else:
#         last = mid - 1
    
#     return -1

#   for a in A:
#     if binary_search(B, a) >= 0:
#       answer += 1

# 나의 풀이 2
# import sys

# while (1):
#     N, M = map(int, sys.stdin.readline().split())
#     if N == 0 and M == 0:
#         break
    
#     A = [int(sys.stdin.readline()) for _ in range(N)]
#     B = [int(sys.stdin.readline()) for _ in range(M)]
#     answer = 0

#     cd = dict()

#     for a in A:
#         cd[a] = 1

#     for b in B:
#         if b in cd:
#             cd[b] = 0
#         else:
#             cd[b] = 1

#     answer = dict(filter(lambda x : x[1] == 0, cd.items()))
#     print(len(answer))

# 나의 풀이 3 : 나의 풀이 2를 좀 더 심플하게
# 왜 얘는 시간 초과?
# import sys

# while True:
#     N, M = map(int, sys.stdin.readline().split())
#     if N == 0 and M == 0:
#         break
    
#     cd = dict()
#     answer = 0

#     for _ in range(N):
#         cd[int(input())] = True
    
#     for _ in range(M):
#         if int(input()) in cd.keys():
#             answer += 1
    
#     print(answer)

# 다른 사람의 풀이
import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    cd = defaultdict(bool)
    n, m = map(int, input().split())
    cnt = 0

    if n == 0 and m == 0:
        break
    
    for _ in range(n):
        cd[int(input())] = True

    for _ in range(m):
        if cd[int(input())]:
            cnt += 1

    print(cnt)