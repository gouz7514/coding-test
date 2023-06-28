# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

# 어디서 메모리 초과가 발생할까?
# 해결하지 못함
# 계수 정렬?

## 아래가 나의 코드
# import sys

# N = int(sys.stdin.readline())

# arr = []

# for _ in range(N):
#     arr.append(int(sys.stdin.readline(5)))

# # 퀵 정렬
# def quick_sort(arr):
#   if len(arr) <= 1:
#     return arr
  
#   pivot = arr[0]
#   tail = arr[1:]
    
#   left_side = [x for x in tail if x <= pivot]
#   right_side = [x for x in tail if x > pivot]

#   return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# arr = quick_sort(arr)

# for i in arr:
#     print(i)
######

import sys

n = int(sys.stdin.readline())
# 계수 정렬
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)