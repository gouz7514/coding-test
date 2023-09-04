# 먹을 것인가 먹힐 것인가
# https://www.acmicpc.net/problem/7795
# 나의 풀이
# 해결 못함...
# import sys

# T = int(sys.stdin.readline().strip())

# for _ in range(T):
#   answer = 0

#   N, M = map(int, sys.stdin.readline().strip().split())
#   A = list(map(int, sys.stdin.readline().strip().split(' ')))
#   B = list(map(int, sys.stdin.readline().strip().split(' ')))
  
#   A.sort()

#   # 이분 탐색으로 찾으면서 A의 원소가 B보다 커지는 순간이 오면 그 idx가 B의 원소가 들어갈 위치
#   for i in B:
#     first, last = 0, len(A) - 1

# 다른 사람의 풀이
# https://jinho-study.tistory.com/311
# 이분 탐색을 사용해 B에서 A의 한 요소보다 작은 수들 중 제일 큰 수의 위치를 찾는 것
def binary_search(li, a):
    s, e = 0, len(li)-1
    res = -1
    while s <= e:
        m = (s + e) // 2
        if li[m] < a:
            res = m
            s = m + 1
        else:
            e = m - 1
    return res
    
    
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (binary_search(B, a) + 1)
    print(cnt)