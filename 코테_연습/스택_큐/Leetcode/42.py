# https://leetcode.com/problems/trapping-rain-water/
# hard
# 나의 풀이 - GG
# def trap(height):
#   answer = 0
#   stack = []
#   cur_h = 0

#   for i in range(len(height)):
#     if i == 0 or cur_h == 0:
#       cur_h = height[i]
#       continue

#     if height[i] < cur_h:
#       # 스택에 넣기 전에 이미 있는지 판단. 즉, 같은 높이에서 만나는지 판단
#       if height[i] in stack:
#         idx = stack.index(height[i])
#         for j in range(idx + 1, len(stack)):
#           answer += (abs(height[i] - stack[j]))
#           stack[j] += abs(height[i] - stack[j])
#       stack.append(height[i])
#     else:
#       result = sum([cur_h - s for s in stack])
#       answer += result
#       stack = []
#       cur_h = height[i]

#   print(stack, answer)

#   if len(stack) >= 2 and stack[-1] > stack[-2]:
#     for i in range(len(stack) - 1):
#       if stack[i] < stack[-1]:
#         answer += abs(stack[-1] - stack[i])

#   return answer

# 다른 사람의 풀이 wow...
def trap(height):
  if not height:
    return 0

  answer = 0
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]

  while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)

    # 더 높은 쪽을 향해 투 포인터 이동
    if left_max <= right_max:
      answer += left_max - height[left]
      left += 1
    else:
      answer += right_max - height[right]
      right -= 1

  return answer

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4, 2, 0, 3, 2, 5]
# height = [4, 1, 2, 3]
# height = [3, 2, 1, 0, 1]
height = [5, 4, 1, 2]
height = [0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]
print(trap(height))