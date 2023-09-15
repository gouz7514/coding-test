# 옥상 정원 꾸미기
# https://www.acmicpc.net/problem/6198
# 골드 5
# 나의 풀이
# import sys
# input = sys.stdin.readline
# buildings = []
# stack = []
# answer = []

# n = int(input())

# for _ in range(n):
#   buildings.append(int(input()))

# buildings = buildings[::-1]

# for i in range(n):
#   cnt = 0

#   while stack:
#     # 높거나 같은 빌딩이 있다면 다음 빌딩들을 보지 못한다
#     if stack[-1][1] >= buildings[i]:
#       answer.append(cnt)
#       break
#     else:
#       # 없앤 게 있다면 + 해준다
#       if answer[stack[-1][0]]:
#         cnt += answer[stack[-1][0]]
#         cnt += 1
#       else:
#         cnt += 1
#       stack.pop()

#   if not stack:
#     answer.append(cnt)

#   stack.append([i, buildings[i]])

# print(answer)

# 다른 사람의 풀이
# 각 빌딩이 자신을 볼 수 있는 이전 빌딩의 갯수를 기록한다
# [10, 3, 7, 4, 12, 2]
# [0, 1, 1, 2, 0, 1]
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = 0

for i in arr:
  while stack and stack[-1] <= i:
    stack.pop()
  stack.append(i)
  
  ans += len(stack) - 1

print(ans)