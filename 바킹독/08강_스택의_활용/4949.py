# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
# 실버 4
# 나의 풀이
import sys
input = sys.stdin.readline

while True:
  string = input().rstrip()
  stack = []
  isBalanced = True

  if string == '.':
    break

  for s in string:
    if s == '(' or s == '[':
      stack.append(s)
    if s == ')':
      if not stack or stack[-1] != '(':
        isBalanced = False
        break
      stack.pop()
    if s == ']':
      if not stack or stack[-1] != '[':
        isBalanced = False
        break
      stack.pop()

  if stack:
    isBalanced = False

  print('yes' if isBalanced else 'no')