# 45. Jump Game II
# class Solution(object):
#     def jump(self, nums):
#         goal = len(nums) - 1
#         arr = [0] * len(nums)

#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] + i >= goal:
#                 arr[i] = 1
#             else:
#                 if nums[i]:
#                     m = float("inf")
#                     for j in range(i+1, i+nums[i]+1,1):
#                         if arr[j]:
#                             m = min(m, arr[j])
#                     arr[i] = m + 1
#         return arr[0]
    
# Wrong!
# class Solution(object):
#     def jump(self, nums):
#         if len(nums) == 1:
#             return 0 if nums[0] > 0 else 0
#         reachable = [0] * len(nums)
#         checked = []
#         for i in range(1, min(nums[0] + 1, len(nums))):
#             reachable[i] = 1
#             checked.append(i)
#         while checked:
#             p = checked.pop()
#             if p == len(nums) - 1:
#                 continue
#             for i in range(p+1, min(p + nums[p] + 1, len(nums))):
#                 if not reachable[i]:
#                     reachable[i] = reachable[p] + 1
#                     checked.append(i)
#                 else:
#                     reachable[i] = min(reachable[i], reachable[p] + 1)
        
#         return reachable[len(nums) - 1]

class Solution(object):
    def jump(self, nums):
        jumps = 0 # 현재까지 점프 횟수
        current_end = 0 # 현재 점프 횟수로 갈 수 있는 최대 위치
        farthest = 0 # 지금까지 도달 가능한 최대 위치

        for i in range(len(nums) - 1):
            # 현재 위치에서 갈 수 있는 최대 거리 업데이트
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                jumps += 1
                return

            # 현재 점프로 갈 수 있는 범위 끝에 도달하면
            if i == current_end:
                jumps += 1 # 점프 횟수 증가
                current_end = farthest # 다음 점프 범위로 확장
                
        return jumps

if __name__ == "__main__":
    solution = Solution()
    nums = [2,1]
    result = solution.jump(nums)
    print(result)