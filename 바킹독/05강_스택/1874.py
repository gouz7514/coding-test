# 스택 수열
# https://www.acmicpc.net/problem/1874
# 실버 2
# 나의 풀이 - 20분 내로 해결!!
import sys

input = sys.stdin.readline
n = int(input())

# 나타내야 할 수열
arr = []
answer = []
stack = []
num = 1

for _ in range(n):
  arr.append(int(input()))

arr = arr[::-1]

while arr:
  # if num > n:
  #   break
  if stack:
    if stack[-1] == arr[-1]:
      arr.pop()
      stack.pop()
      answer.append('-')
    else:
      if num > n:
        answer = 'NO'
        break
      stack.append(num)
      answer.append('+')
      num += 1
  else:
    stack.append(num)
    answer.append('+')
    num += 1

if isinstance(answer, list):
  for i in answer:
    print(i)
else:
  print(answer)

# 다른 사람의 풀이
import sys
input = sys.stdin.readline
n = int(input())

stack = []
result = []
flag = 0
now = 1

for i in range(n):
  num = int(input())
  while now <= num:
    stack.append(now)
    result.append('+')
    now += 1
  if stack[-1] == num:
    stack.pop()
    result.append('-')
  else:
    print('NO')
    flag = 1
    break

if flag == 0:
  for i in result:
    print(i)