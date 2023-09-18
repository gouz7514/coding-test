# 오아시스 재결합
# https://www.acmicpc.net/problem/3015
# 플래티넘 5
# 나의 풀이 - 어렵다...
# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = [int(input()) for _ in range(n)]
# stack = []
# answer = [0 for _ in range(n)]

# for i in range(n):
#   cnt = 0

#   while stack:
#     if stack[-1] > arr[i]:
#       cnt += 1
#       break
#     elif stack[-1] == arr[i]:
#       cnt = len(stack)
#       break
#     else:
#       stack.pop()
#       cnt += 1
#   stack.append(arr[i])
#   answer[i] = cnt

# print(answer)
# print(sum(answer))

# arr = [int(input()) for _ in range(int(input()))]
# stack = []
# answer = 0

# for a in arr:
#   # 스택 끝 값보다 키가 크다면 pop
#   while stack and stack[-1][0] < a:
#     answer += stack.pop()[1]

#   # 스택이 비어있다면 해당 키 append
#   if not stack:
#     stack.append((a, 1))
#     continue

#   # 스택 끝 값이 키와 같다면
#   if stack[-1][0] == a:
#     cnt = stack.pop()[1]
#     answer += cnt

#     if stack:
#       answer += 1
#     stack.append((a, cnt + 1))
#   # 스택 끝 값이 키보다 작다면
#   else:
#     stack.append((a, 1))
#     answer += 1

# print(answer)

# 다른 사람의 풀이 - 예술적이네..
# https://doitdoik.tistory.com/298
import sys

input = sys.stdin.readline
n = int(input())
stack = []
res = 0

for _ in range(n):
  now = int(input())
  cnt = 1

  while stack and stack[-1][0] <= now:
    height, cnt = stack.pop()
    if height == now:
      res += cnt
      cnt += 1
    elif height < now:
      res += cnt
      cnt = 1

  if stack:
    res += 1
  stack.append((now, cnt))
  print(stack, res)

print(res)