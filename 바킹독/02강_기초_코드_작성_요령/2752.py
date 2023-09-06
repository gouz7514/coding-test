# 세수정렬
# https://www.acmicpc.net/problem/2752
# 브론즈 4
# 나의 풀이
import sys

arr = list(map(int, sys.stdin.readline().strip().split(' ')))

print(*[i for i in sorted(arr)])