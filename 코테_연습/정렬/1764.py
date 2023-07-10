# 듣보잡
# https://www.acmicpc.net/problem/1764
# N, M 은 500,000 이하의 자연수
# 나의 풀이 (오답)
# 이유 : 시간 초과
# 시간복잡도 : 최악의 경우 O(N ^ 2), `in` operator로 찾는 과정에서 N * M 번 순회할 수도 있다.
# import sys

# answer = []
# N, M = map(int, sys.stdin.readline().split(' '))
# L, S = [], []

# for i in range(N + M):
#   if i < N:
#     L.append(sys.stdin.readline().strip())
#   else:
#     S.append(sys.stdin.readline().strip())

# for name in L:
#   if name in S:
#     answer.append(name)

# answer.sort()

# print(len(answer))
# for name in answer:
#     print(name)

# 나의 풀이
# 시간 복잡도 : O(N log N)
import sys

names = dict()
N, M = map(int, sys.stdin.readline().split(' '))
L, S = [], []

for i in range(N + M):
  name = sys.stdin.readline().strip()
  if i < N:
    names[name] = 1
  else:
    if name in names:
      names[name] = 0
    else: names[name] = 1

answer = dict(filter(lambda element: element[1] == 0, sorted(names.items())))

print(len(list(answer.keys())))
for name in list(answer.keys()):
  print(name)