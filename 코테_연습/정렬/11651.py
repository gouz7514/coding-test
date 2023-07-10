# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

# 나의 풀이
import sys

N = int(sys.stdin.readline())

coordinates = dict()

for i in range(N):
  x, y = map(int, sys.stdin.readline().split(' '))
  
  if y in coordinates:
    coordinates[y].append(x)
  else:
    coordinates[y] = [x]

for y, x in sorted(coordinates.items()):
  for xx in sorted(x):
    print(xx, y)


# 다른 사람의 풀이
# import sys

# N = int(sys.stdin.readline())

# coords = [tuple(map(int, input().rstrip().split())) for _ in range(N)]

# for x, y in sorted(coords, key = lambda x: (x[1], x[0])):
#     print(f"{x} {y}")