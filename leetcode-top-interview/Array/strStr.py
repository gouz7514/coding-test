# 28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        ans = -1
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle)+i] == needle:
                ans = i
                break
        return ans
        
if __name__ == "__main__":
    solution = Solution()
    haystack = "c"
    needle = "c"
    result = solution.strStr(haystack, needle)
    print(result)