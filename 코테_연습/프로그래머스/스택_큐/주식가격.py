# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 나의 풀이
def solution(prices):
  answer = [0] * len(prices)
  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      if prices[i] > prices[j]:
        answer[i] = j - i
        break
      else:
        answer[i] = j - i
  
  return answer

# 다른 사람의 풀이
def solution(prices):
  stack = [0]
  answer = [0] * len(prices)

  for i in range(len(prices)):
    while stack != [] and stack[-1][1] > prices[i]:
      past, _ = stack.pop()
      answer[past] = i - past
    stack.append([i, prices[i]])

  for i, s in stack:
    answer[i] = len(prices) - 1 - i
  return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))