# 숫자
# https://www.acmicpc.net/problem/10093
# 브론즈 2
# 나의 풀이
# 두 양의 정수에 대해, 두 수 사이에 있는 정수를 모두 출력
# 시간 제한 1초
import sys

A, B = sys.stdin.readline().strip().split(' ')
A = int(A)
B = int(B)

(A, B) = (A, B) if A <= B else (B, A)

count = B - A - 1
# 둘 사이에 정수가 없는 경우를 고려해야 한다
if A == B or A + 1 == B:
  count = 0
print(count)

arr = [str(i) for i in range(A+1, B)]
print(' '.join(arr))