# 대표값2
# https://www.acmicpc.net/problem/2587
# 브론즈 2
# 나의 풀이
arr = []

for _ in range(5):
  arr.append(int(input()))

print(sum(arr) // 5)
print(sorted(arr)[2])