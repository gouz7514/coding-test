# 27. Remove Element
# 나의 풀이 - O(n) 공간 복잡도
class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)

# GPT 풀이 1.
# 이렇게 하면 k는 맞는데... nums의 조건에 안 맞지 않나?
# this is crazy
class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # 새로 채워질 위치를 가리키는 포인터
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            print('nums : ', nums)
        return k

if __name__ == "__main__":
    solution = Solution()

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(nums, result)