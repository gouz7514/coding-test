# 151. Reverse Words in a String
# f the string data type is mutable in your language,
# can you solve it in-place with O(1) extra space?
# not bad - 3ms, beats 38.73%
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(list(filter(lambda x: x != '', s.split(' ')))[::-1])

# What would be the fastest way?
# Answer! much much faster
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))



if __name__ == "__main__":
    solution = Solution()
    s = "a good   example"
    result = solution.reverseWords(s)
    print(result)