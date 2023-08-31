# 커트라인
# https://www.acmicpc.net/problem/25305

N, k = map(int, input().split())
score = sorted(list(map(int, input().split())), reverse=True)

print(score)
