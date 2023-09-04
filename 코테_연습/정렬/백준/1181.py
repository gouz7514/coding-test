# 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

# 중복 제거
arr = list(set(arr))

# 정렬
# 처음엔 길이 순으로, 길이가 같으면 알파벳 순으로 정렬
arr.sort(key = lambda x: (len(x), x))

for i in arr:
    print(i)
