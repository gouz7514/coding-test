# 수 찾기
# https://www.acmicpc.net/problem/1920
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split(' ')))

A.sort()

M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split(' ')))

for b in B:
    start, end = 0, N - 1
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == b:
            answer = 1
            break
        elif A[mid] < b:
            start = mid + 1
        else:
            end = mid - 1
            
    print(answer)