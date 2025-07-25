# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps,
# where k is non-negative
# print(nums + nums2)

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
  
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    print(nums)  # Should print: [5, 6, 7, 1, 2, 3, 4]