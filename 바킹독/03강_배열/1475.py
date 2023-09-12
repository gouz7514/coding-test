# 방 번호
# https://www.acmicpc.net/problem/1475
# 실버 5
# 나의 풀이 - 9와 6을 동일하게 취급할 수 있다
import math

num = input()
arr = [0] * 9
cnt = 0

for n in num:
  if n == '6' or n == '9':
    arr[6] += 1
  else:
    arr[int(n)] += 1

for i in range(9):
  if i == 6:
    cnt = max(cnt, math.ceil(arr[i] / 2))
  else:
    cnt = max(cnt, arr[i])

print(cnt)

# 다른 사람의 풀이
# wow...
num = list(map(int, input()))
arr = [0] * 10

for i in range(len(num)):
  if num[i] == 6 or num[i] == 9:
    if arr[6] <= arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1
  else:
    arr[num[i]] += 1

print(max(arr))