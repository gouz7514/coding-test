# 제로
# https://www.acmicpc.net/problem/10773
# 실버 4
# 나의 풀이 - sys를 쓰면 더 빨리 풀 수 있다
import sys

input = sys.stdin.readline
stack = []

for _ in range(int(input())):
  n = int(input())
  stack.append(n) if n else stack.pop()

print(sum(stack))