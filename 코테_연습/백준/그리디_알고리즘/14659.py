# 한조서열정리하고옴ㅋㅋ
# https://www.acmicpc.net/problem/14659
# 브론즈 1
# 나의 풀이
import sys

N = int(sys.stdin.readline().strip())

heights = list(map(int, sys.stdin.readline().strip().split(' ')))

cur_height = heights[0] # 현재 활잡이
max_cnt, cur_cnt = 0, 0 # 최대 처치횟수, 현재 처치횟수

if N < 2:
  max_cnt = 0
else:
  # 첫번째 봉우리 제외
  for height in heights[1:]:
    if height > cur_height: # 다음 봉우리가 현재 봉우리보다 높다면, 활잡이, 처치횟수 초기화
      cur_cnt = 0
      cur_height = height
    else: # 다음 봉우리가 현재 봉우리보다 낮다면 처치 가능. 현재 및 최대 처치횟수 증가
      cur_cnt += 1
      max_cnt = max(max_cnt, cur_cnt)
  
print(max_cnt)

# 나의 풀이 2
import sys

N = int(sys.stdin.readline().strip())

heights = list(map(int, sys.stdin.readline().strip().split(' ')))
cur_height, cur_cnt, max_cnt = 0, 0, 0

for height in heights:
  if height > cur_height:
    max_cnt = max(max_cnt, cur_cnt)
    cur_cnt = 0
    cur_height = height
  else:
    cur_cnt += 1

# 다른 사람의 풀이
N = int(input())

L = list(map(int, input().split())) + [100001]

best, cnt, maxCnt = 0, 0, 0

for i in L:
  if i > best:
    maxCnt = max(maxCnt, cnt)
    cnt = 0
    best = i
  else:
    cnt += 1

print(maxCnt)