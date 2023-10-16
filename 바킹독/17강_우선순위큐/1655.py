# 가운데를 말해요
# https://www.acmicpc.net/problem/1655
# 골드 2
# 나의 풀이
# PriorityQueue와 heapq 차이점 알아야 한다
# import sys
# from heapq import heappush, heappop

# input = sys.stdin.readline

# lowerThanMedian = []
# higherThanMedian = []
# median = 0

# for i in range(int(input())):
#   n = int(input())

#   if i == 0:
#     median = n
#     print(median)
#     continue

#   # 현재 중간값보다 큰 수라면
#   if n >= median:
#     heappush(higherThanMedian, n)

#     if abs(len(higherThanMedian) - len(lowerThanMedian)) > 1:
#       # low heap에 넣고 high heap에서 빼서 median으로 바꿔야 됨
#       heappush(lowerThanMedian, median * -1)
#       median = heappop(higherThanMedian)
#   else:
#     heappush(lowerThanMedian, n * -1)

#     if len(lowerThanMedian) > len(higherThanMedian):
#       # median은 high heap으로 가고, low heap에서 뺀 값이 median으로
#       heappush(higherThanMedian, median)
#       median = -1 * heappop(lowerThanMedian)

#   print(median)

# 다른 사람의 풀이
import heapq
import sys

input = sys.stdin.readline
N = int(input())

left = []
right = []

for _ in range(N):
  number = int(input())

  if len(left) == len(right):
    heapq.heappush(left, -number)
  else:
    heapq.heappush(right, number)

  if left and right and -left[0] > right[0]:
    left_temp = -heapq.heappop(left)
    right_temp = heapq.heappop(right)

    heapq.heappush(left, -right_temp)
    heapq.heappush(right, left_temp)

  print(left, right)

  print(-left[0])