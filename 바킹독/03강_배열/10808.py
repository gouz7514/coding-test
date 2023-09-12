# 알파벳 개수
# https://www.acmicpc.net/problem/10808
# 브론즈 4
# 나의 풀이 - 배열만 쓰고 풀어보기
arr = [0] * 26

for w in input():
  idx = ord(w) - 97
  arr[idx] += 1

print(*arr)