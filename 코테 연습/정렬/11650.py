# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
### 나의 풀이
# import sys

# N = int(sys.stdin.readline())

# arr = []

# for _ in range(N):
#     arr.append(sys.stdin.readline().split())

# arr.sort(key = lambda x : (int(x[0]), int(x[1])))
# for i in arr:
#     print(" ".join(i))
###

### 다른 사람 풀이
import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort()

# 리스트 언패킹
for i in arr:
    print(*i)