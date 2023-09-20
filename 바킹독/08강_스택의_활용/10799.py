# 쇠막대기
# https://www.acmicpc.net/problem/10799
# 실버 2
# 나의 풀이
stack = []
cnt = 0
string = input()

# range(len(string)) 대신 enumeate를 사용할 수도 있다
# for i, v in enumerate(string):
for i in range(len(string)):
  if string[i] == '(':
    stack.append((i, string[i]))
  else:
    (x, y) = stack.pop()
    if x + 1 == i:
      cnt += len(stack)
    else:
      cnt += 1

print(cnt)

# 다른 사람의 풀이
# stack = []
# cnt = 0
# s = input()

# for i in range(len(s)):
#   if s[i] == '(':
#     stack.append('(')
#   else:
#     if s[i-1] == '(':
#       stack.pop()
#       cnt += len(stack)
#     else:
#       stack.pop()
#       cnt += 1
# print(cnt)