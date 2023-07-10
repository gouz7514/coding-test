# K번째 수
# https://www.acmicpc.net/problem/11004
# 시간 복잡도 : O(N log N)
import sys

N, K = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().strip().split()))

arr.sort()

print(arr[K - 1])