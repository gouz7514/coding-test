# 오큰수
# https://www.acmicpc.net/problem/17298
# 골드 4
# 나의 풀이
# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# nums = nums[::-1]
# arr = []
# answer = []

# for i in range(n):
#   while arr:
#     if arr[-1] > nums[i]:
#       answer.append(arr[-1])
#       break
#     else:
#       arr.pop()

#   if not arr:
#     answer.append(-1)

#   arr.append(nums[i])

# print(*answer[::-1])

# 다른 사람의 풀이
n = int(input())
nums = list(map(int, input().split()))

stack = []
answer = [-1] * n

for i in range(n):
  while stack and nums[stack[-1]] < nums[i]:
    answer[stack.pop()] = nums[i]
  stack.append(i)
print(*answer)