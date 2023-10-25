# 텀 프로젝트
# https://www.acmicpc.net/problem/9466
# 골드 3
# 나의 풀이 - 시간 초과 (으아악)
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(stack, numbers, visited):
#   print('dfs')
#   arr = []
  
#   while stack:
#     x = stack.pop()
#     num = numbers[x - 1]

#     if not visited[num]:
#       visited[num] = True
#       stack.append(num)
#       arr.append(x)
#     else:
#       arr.append(num)
#   print(arr)

#   return ''

# for _ in range(int(input())):
#   n = int(input())
#   numbers = list(map(int, input().split(' ')))
#   answer = n

#   for i in range(1, n + 1):
#     visited = [False for _ in range(n + 1)]
#     visited[i] = True
#     stack = [i]
#     dfs(stack, numbers, visited)
#     answer -= 1

#   print(answer)


# 다른 사람의 풀이
# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def dfs(n):
#   global count

#   visited[n] = True
#   cycle_list.append(n)

#   if visited[arr[n]]:
#     if arr[n] in cycle_list:
#       count -= len(cycle_list[cycle_list.index(arr[n]):])
#   else:
#     dfs(arr[n])

# for _ in range(int(input())):
#   N = int(input())
#   arr = [0]
#   arr.extend([int(x) for x in input().rstrip().split()])

#   visited = [False] * (N + 1)
#   count = N

#   for i in range(1, N + 1):
#     if not visited[i]:
#       cycle_list = []
#       dfs(i)

#   print(count)

# 다시 풀어보기
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
  global cnt
  visited[n] = True
  cycle_list.append(n)

  if visited[arr[n]]:
    if arr[n] in cycle_list:
      cnt -= len(cycle_list[cycle_list.index(arr[n]):])
  else:
    dfs(arr[n])

for _ in range(int(input())):
  n = int(input())
  arr = [0] + list(map(int, input().split()))
  visited = [False for _ in range(n + 1)]
  cnt = n

  for i in range(1, n + 1):
    if not visited[i]:
      cycle_list = []
      dfs(i)

  print(cnt)
