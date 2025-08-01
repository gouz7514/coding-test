# 58. Length of Last Word
# solved but slow
# class Solution(object):
#     def lengthOfLastWord(self, s):
#         r = 0
#         for i in list(s)[::-1]:
#             if i == ' ':
#                 if not r:
#                     continue
#                 break
#             r += 1
#         return r

# solved but slow too... what would be the faster way?         
# hint : avoid unnecessary operation
# class Solution(object):
#     def lengthOfLastWord(self, s):
#             a, b = 0, 0
#             for i in list(s):
#                 if i == ' ':
#                     if b:
#                         a = b
#                         b = 0
#                 else:
#                     b += 1
#             if b:
#                 a = b
#             return a

class Solution(object):
    def lengthOfLastWord(self, s):
        r = 0
        for i in s[::-1]:
            if i == ' ':
                if r:
                    break
            else:
                r += 1
        return r
        
if __name__ == "__main__":
    solution = Solution()

    s = "luffy is still joyboy"
    result = solution.lengthOfLastWord(s)
    print(result)