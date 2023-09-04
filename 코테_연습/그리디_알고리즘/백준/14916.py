# 거스름돈
# https://www.acmicpc.net/problem/14916
# 실버 5
# 나의 풀이 - 실패 why? - for 문 범위 문제...
n = int(input())

dp = [-1] * 100001
dp[1] = -1
dp[2] = 1
dp[3] = -1

for i in range(4, 100001):
  if (i % 2 == 0): # 짝수일 때
    if (i % 10 == 0):
      dp[i] = i // 5
    else:
      dp[i] = dp[i - 2] + 1
  else: # 홀수일 때
    if (i % 5 == 0):
      dp[i] = i // 5
    else:
      dp[i] = dp[i - 2] + 1

print(dp[n])

# 나의 풀이 2 - 아래 코드는 맞음
# n = int(input())

# dp = [-1] * (n + 8)
# dp[2] = 1
# dp[4]=2
# dp[5]=1
# dp[6]=3
# dp[7]=2
# dp[8]=4

# for i in range(9, n + 1):
#   if (i % 2 == 0): # 짝수일 때
#     if (i % 10 == 0):
#       dp[i] = i // 5
#     else:
#       dp[i] = dp[i - 2] + 1
#   else: # 홀수일 때
#     if (i % 5 == 0):
#       dp[i] = i // 5
#     else:
#       dp[i] = dp[i - 2] + 1

# print(dp[n])
#####
# 다른 사람의 풀이
# n = int(input())

# dp = [-1] * (n + 8)

# dp[2]=1
# dp[4]=2
# dp[5]=1
# dp[6]=3
# dp[7]=2
# dp[8]=4

# for i in range(9, n+1):
#     dp[i] = min(dp[i-2], dp[i-5])+1

# print(dp[n])
#######
# 다른 사람의 풀이 2
# n = int(input())

# cnt = 0
# i = 0
# while True:
#     if n % 5 == 0:
#         cnt += n // 5
#         break
#     else:
#         n -= 2
#         cnt += 1
#     if n < 0:
#         break
    
# if (n < 0):
#     print(-1)
# else:
#     print(cnt)