# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
    print(i)