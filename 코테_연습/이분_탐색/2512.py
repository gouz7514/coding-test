# 예산
# 실버 3
# https://www.acmicpc.net/problem/2512
# 나의 풀이 - 정답
import sys

# 지방의 수
N = int(sys.stdin.readline().strip())
# 각 지방의 예산요청
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
# 총 예산
M = int(sys.stdin.readline().strip())
nums.sort()

start, end, answer = 1, nums[-1], 0

def sum_num(arr, mid):
  sum = 0
  for i in arr:
    if i >= mid:
      sum += mid
    else:
      sum += i
  return sum

while start <= end:
  mid = (start + end) // 2

  result = sum_num(nums, mid)

  if result < M:
    answer = mid
    start = mid + 1
  elif result > M:
    answer = mid - 1
    end = mid - 1
  else:
    answer = mid
    break

# 모든 요청이 배정될 수 있는 경우에는 그대로 배정
if sum(nums) <= M:
  print(nums[-1])
else:
  print(answer)

# 나의 풀이 - 간단하게
n = int(input())
budget = list(map(int, input().split()))
total = int(input())

budget.sort()
start, end, answer = 0, budget[-1], 0

while start <= end:
  cur = 0
  mid = (start + end) // 2

  for b in budget:
    if b >= mid:
      cur += mid
    else:
      cur += b

  if cur <= total:
    answer = mid
    start = mid + 1
  else:
    end = mid - 1

print(answer)