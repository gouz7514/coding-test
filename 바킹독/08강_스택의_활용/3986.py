# 좋은 단어
# https://www.acmicpc.net/problem/3986
# 실버 4
# 나의 풀이
import sys
input = sys.stdin.readline
answer = 0

for _ in range(int(input())):
  string = input().strip()
  stack = []
  isGood = True

  for s in string:
    if not stack:
      stack.append(s)
    else:
      if stack[-1] == s:
        stack.pop()
      else:
        stack.append(s)

  if stack:
    isGood = False

  if isGood:
    answer += 1

print(answer)

# 다른 사람의 풀이
import sys
input = sys.stdin.readline
answer = 0

for _ in range(int(input())):
  string = input().strip()
  stack = []

  for s in string:
    if stack and stack[-1] == s:
      stack.pop()
    else:
      stack.append(s)

  if not stack:
    answer += 1

print(answer)