# 탑
# https://www.acmicpc.net/problem/2493
# 골드 5
# 나의 풀이 - 시간 초과를 줄여야 한다 O(n)으로, 어렵네....
n = int(input())
towers = list(map(int, input().split(' ')))
# towers = towers[::-1]
arr = [] # 비교할 임시 배열
answer = []

for i in range(n):
  while arr:
    if arr[-1][1] > towers[i]:
      answer.append(arr[-1][0] + 1)
      break
    else:
      arr.pop()
  if not arr:
    answer.append(0)
  arr.append([i, towers[i]])
  print(arr)

print(*answer)

# 다른 사람의 풀이
# n = int(input())
# towers = list(map(int, input().split(' ')))
# stack = []
# answer = []

# for i in range(n):
#     while stack:
#         if stack[-1][1] > towers[i]:
#             answer.append(stack[-1][0] + 1)
#             break
#         else:
#             stack.pop()
#     if not stack:
#         answer.append(0)
#     stack.append([i, towers[i]])

# print(answer)