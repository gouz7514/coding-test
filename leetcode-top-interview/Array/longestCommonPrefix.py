# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         prefix = ''
#         c = 0
#         loop = True
#         while loop:
#             exist = False
#             for s in strs:
#                 if not s or c >= len(s) or s[c] != strs[0][c]:
#                     loop = False
#                     exist = False
#                     break
#                 elif s[c] == strs[0][c]:
#                     exist = True
#             if exist:
#                 prefix += strs[0][c]
#                 exist = False
#                 c += 1
#         return prefix

# 가장 짧은 문자열 길이 미리 확인하기?
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         prefix = ''
#         # 공통 인덱스
#         c = 0
#         # 가장 짧은 문자열 길이
#         n = float('inf')
#         for s in strs:
#             n = min(n, len(s))

#         for i in range(n):
#             exist = True
#             for s in strs:
#                 if i >= len(s) or s[i] != strs[0][i]:
#                     exist = False
#                     break
            
#             if not exist:
#                 break
#             c += 1
#         return strs[0][:c]
                
# Leetcode 답안
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if not strs: return ''
#         first = strs[0]
#         for i in range(len(first)):
#             ch = first[i]

#             for s in strs[1:]:
#                 if i >= len(s) or s[i] != ch:
#                     return first[:i]
#         return first

# Claude : Horizontal Scanning (경이롭다)
# 뒤에서 빼는 식으로..
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix: return ""
        return prefix

if __name__ == "__main__":
    solution = Solution()
    strs = ["flower","flow","flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)