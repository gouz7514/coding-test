# 보물
# https://www.acmicpc.net/problem/1026
# 나의 풀이
# import sys

# answer = 0

# N = int(sys.stdin.readline())

# A = list(map(int, sys.stdin.readline().strip().split()))
# B = list(map(int, sys.stdin.readline().strip().split()))

# A.sort(reverse=True)
# B.sort()

# for n in range(N):
#   answer += A[n] * B[n]

# print(answer)

# 다른 사람의 풀이
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse = True)
B.sort()

print(sum([A[i] * B[i] for i in range(N)]))