# 애너그램 만들기
# https://www.acmicpc.net/problem/1919
# 브론즈 2
# 나의 풀이
import sys

arr = [0] * 26
answer = 0

str1 = sys.stdin.readline().strip()
for s in str1:
  arr[ord(s) - ord('a')] += 1

str2 = sys.stdin.readline().strip()
for s in str2:
  arr[ord(s) - ord('a')] -= 1

for a in arr:
  if a != 0:
    answer += abs(a)

print(answer)