# 56. Jump Game
# given an integer array nums
# initially positioned at the array's first index
# each element in the array represents your maximum jump length at that position
# return true fi you can reach the last index, or false otherwise
# idea 1 : 앞에서부터 가는 게 맞아..
# taks so long.... only beast 8%....
class Solution(object):
    def canJump(self, nums):
        a = False
        if len(nums) == 1:
            return True
        checked = [False] * len(nums)
        # array of reachable index
        reachable = list(range(1, min(nums[0] + 1, len(nums))))
        if len(reachable) == 0:
            return False
        
        for i in range(reachable[-1]):
            checked[i] = True

        while reachable:
            c = reachable.pop()
            if c == len(nums) - 1:
                a = True
                break
            if not nums[c]:
                continue
            for i in range(c+1, min(c+nums[c]+1,len(nums))):
                if not checked[i]:
                  reachable.append(i)
                  checked[i] = True

        return a

# wow....
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,0,1]
    result = solution.canJump(nums)
    print(result)