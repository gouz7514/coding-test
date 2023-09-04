# 두 수의 합
# https://www.acmicpc.net/problem/3273
# 나의 풀이
# import sys
# sys.setrecursionlimit(10**6)

# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().strip().split()))
# x = int(sys.stdin.readline().strip())

# def counting_sort(arr):
#   if len(arr) <= 1:
#     return arr

#   # 입력 배열에서 최댓값과 최솟값을 구합니다.
#   max_val = max(arr)
#   min_val = min(arr)

#   # 카운트 배열을 초기화합니다.
#   count = [0] * (max_val - min_val + 1)

#   # 입력 배열에서 각 원소의 개수를 세어서 카운트 배열에 저장합니다.
#   for num in arr:
#     count[num - min_val] += 1

#   # 카운트 배열을 누적 합 배열로 변환합니다.
#   for i in range(1, len(count)):
#     count[i] += count[i - 1]

#   # 입력 배열을 역순으로 순회하면서 각 원소를 정렬된 위치에 배치합니다.
#   sorted_arr = [0] * len(arr)
#   for num in reversed(arr):
#     index = count[num - min_val] - 1
#     sorted_arr[index] = num
#     count[num - min_val] -= 1

#   return sorted_arr

# sorted_arr = counting_sort(arr)

# first, last, answer = 0, len(sorted_arr) - 1, 0

# def find(arr, first, last, answer):
#   if first >= last:
#     return answer
  
#   result = arr[first] + arr[last]

#   if result == x:
#     answer += 1
#     first += 1
#     return find(arr, first, last, answer)
#   elif result > x:
#     last -= 1
#     return find(arr, first, last, answer)
#   else:
#     first += 1
#     return find(arr, first, last, answer)

# print(find(sorted_arr, first, last, answer))

# 다른 사람의 풀이
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())

arr.sort()

start, end, count = 0, n - 1, 0

while start < end:
  if arr[start] + arr[end] == x:
    count += 1
    start += 1
    end -= 1
  elif arr[start] + arr[end] > x:
    end -= 1
  else:
    start += 1

print(count)