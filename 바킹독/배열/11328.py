# Strfy
# https://www.acmicpc.net/problem/11328
# 브론즈 2
# 나의 풀이
# for _ in range(int(input())):
#   arr = [0] * 26
#   str1, str2 = list(input().split(' '))
  
#   for s in str1:
#     arr[ord(s) - ord('a')] += 1

#   for s in str2:
#     arr[ord(s) - ord('a')] += 1

#   # 여기서 체크하는 방법 다름
#   is_possible = all(count == 0 for count in arr)

#   if is_possible:
#     print('Possible')
#   else:
#     print('Impossible')

# 다른 사람의 풀이
# 정렬해서 같은지 본다
# 아래 방식이 시간이 훨씬 빠르다 - sys 활용
import sys

for _ in range(int(input())):
  str1, str2 = list(sys.stdin.readline().strip().split(' '))
  is_possible = True

  str1 = sorted(str1)
  str2 = sorted(str2)
  length = len(str1)

  for i in range(length):
    if str1[i] == str2[i]:
      is_possible = True
    else:
      is_possible = False
      break

  if is_possible:
    print('Possible')
  else:
    print('Impossible')