# 단어 뒤집기
# 브론즈 1
# 나의 풀이
import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
  string = sys.stdin.readline().strip().split(' ')
  arr = []
  for s in string:
    arr.append(s[::-1])
  print(' '.join(arr))