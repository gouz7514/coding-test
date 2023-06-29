# 나이순 정렬
# https://www.acmicpc.net/problem/10814
# 나의 풀이

# N = int(input())

# arr = []

# for i in range(N):
#     age, name = input().split(' ')
#     age = int(age)
#     arr.append([age, name, i])

# arr.sort(key = lambda x: (x[0], x[2]))

# for a in arr:
#     print(a[0], a[1])
###

# 다른 사람의 풀이
# 나이가 같으면 먼저 가입한 사람이 앞에 온다. 즉, 나이 기준으로 가입한 사람의 이름을 추가한 뒤 정렬하면 된다.
import sys
N = int(sys.stdin.readline())

members = dict()

for i in range(N):
  age, name = sys.stdin.readline().split(' ')

  age = int(age)
  if age in members:
    members[age].append(name.rstrip())
  else:
    members[age] = [name.rstrip()]

for age, names in sorted(members.items()):
  for name in names:
    print(f"{age} {name}", end="\n")