# 42. Trapping Rain Water
#Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

class Solution(object):
  def trap(self, height):
    answer = 0
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    for i in range(n):
      if i == 0:
        max_left[i] = height[i]
        continue
      max_left[i] = max(max_left[i - 1], height[i])

    for i in range(n - 1, -1, -1):
      if i == n - 1:
        max_right[i] = height[i]
        continue
      max_right[i] = max(max_right[i + 1], height[i])
    
    for i in range(n):
      answer += min(max_left[i], max_right[i]) - height[i]
    
    return answer

if __name__ == "__main__":
    solution = Solution()

    height = [4,2,0,3,2,5]
    result = solution.trap(height)
    print(result)