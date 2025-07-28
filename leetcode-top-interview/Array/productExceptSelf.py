# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums except nums[i]
# The product of any previx or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# O(1) extra space complexity

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Calculate left products
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate right products and combine with left products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer

if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)