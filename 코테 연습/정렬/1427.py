# 소트 인사이드
# https://www.acmicpc.net/problem/1427

# 나의 풀이
# import sys

# numbers = dict()
# N = list(sys.stdin.readline().strip())

# for i in N:
#     if i in numbers:
#         numbers[i] += 1
#     else:
#         numbers[i] = 1

# result = ''

# for num, cnt in sorted(numbers.items(), reverse = True):
#     for _ in range(cnt):
#         result += num

# print(result)

## 다른 사람의 풀이
N = int(input())

li = []

for i in str(N):
    li.append(int(i))

li.sort(reverse = True)

for i in li:
    print(i, end = '')