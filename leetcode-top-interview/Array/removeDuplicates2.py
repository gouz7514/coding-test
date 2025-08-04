# 26. Remove Duplicates from Sorted Array II
# remove some duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return 1
        k = 2
        
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k


        """
        :type nums: List[int]
        :rtype: int
        """
        
if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    result = solution.removeDuplicates(nums)
    print(result, nums)