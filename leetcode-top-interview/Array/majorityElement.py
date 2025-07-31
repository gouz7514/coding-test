# 169. Majority Element
# Given an array nums of size n, return the majority element
# THe majority element is the element that appears more than n/2 times
# You may assume that the majority element always exist in the array
class Solution(object):
    def majorityElement(self, nums):
        candidate, count = 0, 0
        
        for i in range(len(nums)):
            if not count:
                candidate = nums[i]
                count += 1
                continue
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate
                

        
if __name__ == "__main__":
    solution = Solution()

    nums = [3,2,3]
    result = solution.majorityElement(nums)
    print(result)