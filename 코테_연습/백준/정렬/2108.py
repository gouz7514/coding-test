# 통계학
# https://www.acmicpc.net/problem/2108
# 해결 못한 줄 알았는데 input()에서 초과 뜨고 있었네ㅋㅋ
import sys
N = int(sys.stdin.readline().strip())

nums = []
dic = dict()

for _ in range(N):
  num = int(sys.stdin.readline().strip())

  if num in dic:
    dic[num] += 1
  else:
    dic[num] = 1

for num, cnt in sorted(dic.items()):
  for _ in range(cnt):
    nums.append(num)

# 산술평균
print(int(round(sum(nums) / len(nums), 0)))

# 중앙값
print(nums[(len(nums) // 2)])

# 최빈값, 여러 개 있으면 최빈값 중 두번쨰로 작은 값
sorted_dic = sorted(dic.items(), key = lambda x : (x[1], -x[0]), reverse = True)
if N > 1:
  if sorted_dic[0][1] == sorted_dic[1][1]:
    print(sorted_dic[1][0])
  else:
    print(sorted_dic[0][0])
else:
  print(sorted_dic[0][0])

# 범위
print(max(nums) - min(nums))