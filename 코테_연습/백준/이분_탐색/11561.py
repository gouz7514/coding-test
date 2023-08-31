# 징검다리
# https://www.acmicpc.net/problem/11561
# 실버 3
# 나의 풀이
import sys

for _ in range(int(sys.stdin.readline().strip())):
  N = int(sys.stdin.readline().strip())

  if N <= 2:
    print(1)
  else:
    start, end, answer = 1, N, 1

    while start <= end:
      mid = (start + end) // 2

      if mid * (mid + 1) // 2 > N:
        end = mid - 1
      else:
        answer = mid
        start = mid + 1

    print(answer)