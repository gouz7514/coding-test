# 개수 세기
# https://www.acmicpc.net/problem/10807
# 브론즈 5
# 나의 풀이 - 나는 왜 이렇게 복잡하게 푸는가
N = int(input())
nums = list(map(int, input().split(' ')))
dic = dict()

for n in nums:
  if n in dic:
    dic[n] += 1
  else:
    dic[n] = 1

v = int(input())
if v in dic:
  print(dic[v])
else:
  print(0)

# 다른 사람의 풀이
n = int(input())
nums = list(map(int, input().split(' ')))
v = int(input())
answer = 0

for n in nums:
  if n == v:
    answer += 1
print(answer)

# 다른 사람의 풀이 2
n = int(input())
nums = input().split()
v = input()

print(nums.count(v))