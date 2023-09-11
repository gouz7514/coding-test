# 주사위 세개
# https://www.acmicpc.net/problem/2480
# 브론즈 4
dic = dict()
nums = list(map(int, input().split(' ')))
answer = 0

for n in nums:
  if n in dic:
    dic[n] += 1
  else:
    dic[n] = 1

sorted_dict = sorted(dic.items(), key = lambda x : x[1], reverse=True)

if sorted_dict[0][1] == 3:
  answer = 10000 + sorted_dict[0][0] * 1000
elif sorted_dict[0][1] == 2:
  answer = 1000 + sorted_dict[0][0] * 100
else:
  answer = 100 * max(dic.keys())

print(answer)