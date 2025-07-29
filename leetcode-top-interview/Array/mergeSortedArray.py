# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing orders, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array in non-decreasing order.
# The final sorted array should not be returned by the function,but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 이건 진짜 최악의 풀이
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         c = m + n - 1
#         l, r = m - 1, n - 1
#         while c > 0:
#             if r < 0 or l < 0: break
#             if nums1[l] >= nums2[r]:
#                 nums1[c] = nums1[l]
#                 nums1[l] = 0
#                 l -= 1
#             else:
#                 nums1[c] = nums2[r]
#                 nums2.pop()
#                 r -= 1
#             c -= 1
#             print(nums1)
        
#         if len(nums2):
#             for i in range(len(nums2)):
#                 nums1[i] = nums2[i]
            
class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1  # nums1의 마지막 실제 값
        p2 = n - 1  # nums2의 마지막 값
        p = m + n - 1  # nums1의 마지막 인덱스 (빈 공간 끝)

        # 뒤에서부터 큰 값을 채워 넣기
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # nums2에 남은 값이 있으면 채우기
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
                
        
if __name__ == "__main__":
    solution = Solution()

    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)