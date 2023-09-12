# 에디터
# https://www.acmicpc.net/problem/1406
# 실버 2
# 나의 풀이
# 각 연산에 대해 arr2와 왔다갔다한다
# import sys

# arr = list(sys.stdin.readline().strip())
# arr2 = []

# for _ in range(int(sys.stdin.readline().strip())):
#   order = list(sys.stdin.readline().strip().split(' '))

#   if order[0] == 'L':
#     arr2.append(arr.pop()) if arr else None
#   if order[0] == 'D':
#     arr.append(arr2.pop()) if arr2 else None
#   if order[0] == 'B':
#     arr.pop() if arr else None
#   if order[0] == 'P':
#     arr.append(order[1])

# print(''.join(arr + list(reversed(arr2))))

# 다른 사람의 풀이
# 연결 리스트 활용하기
import sys
input = sys.stdin.readline

mx = 1000001
dat = [-1] * mx
pre = [-1] * mx
nxt = [-1] * mx
unused = 1

def traverse():
  cur = nxt[0]
  while cur != -1:
    print(chr(dat[cur] + ord('a')), end='')
    cur = nxt[cur]

def insert(addr, num):
  global unused
  dat[unused] = num
  pre[unused] = addr
  nxt[unused] = nxt[addr]

  if nxt[addr] != -1:
    pre[nxt[addr]] = unused
  nxt[addr] = unused

  unused += 1

def erase(addr):
  nxt[pre[addr]] = nxt[addr]
  if nxt[addr] != -1:
    pre[nxt[addr]] = pre[addr]

inp = input().rstrip()
cur = 0
for c in inp:
  insert(cur, ord(c) - ord('a'))
  cur += 1

for _ in range(int(input())):
  command = list(input().rstrip().split())
  if command[0] == 'L':
    if pre[cur] != -1:
      cur = pre[cur]
  elif command[0] == 'D':
    if nxt[cur] != -1:
      cur = nxt[cur]
  elif command[0] == 'B':
    if pre[cur] != -1:
      erase(cur)
      cur = pre[cur]
  else:
    insert(cur, ord(command[1]) - ord('a'))
    cur = nxt[cur]

traverse()