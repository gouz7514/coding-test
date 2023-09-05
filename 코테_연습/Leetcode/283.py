# https://leetcode.com/problems/move-zeroes
# easy
# 나의 풀이
def moveZeroes(nums):
  start, end = 0, len(nums) - 1

  while start < end:
    if nums[start] == 0:
      del nums[start]
      nums.append(0)
      end -= 1
    elif nums[end] == 0:
      del nums[end]
      nums.append(0)
      end -= 1
    else:
      start += 1

  return nums

nums = [1, 0, 1]
print(moveZeroes(nums))