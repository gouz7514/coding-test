# 13. Roman to Integer
# 4ms, beats 85.24%
# I thought, only these cases apply for substraction rule
class Solution(object):
    def romanToInt(self, s):
        roman = dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
        c = 0
        result = 0
        while c < len(s):
            if s[c] == "I":
                if c + 1 < len(s) and s[c + 1] in ["V", "X"]:
                    result += roman[s[c+1]] - roman[s[c]]
                    c += 2
                else:
                    result += roman[s[c]]
                    c += 1
            elif s[c] == "X":
                if c + 1 < len(s) and s[c + 1] in ["L", "C"]:
                    result += roman[s[c+1]] - roman[s[c]]
                    c += 2
                else:
                    result += roman[s[c]]
                    c += 1
            elif s[c] == "C":
                if c + 1 < len(s) and s[c + 1] in ["D", "M"]:
                    result += roman[s[c+1]] - roman[s[c]]
                    c += 2
                else:
                    result += roman[s[c]]
                    c += 1
            else:
                result += roman[s[c]]
                c += 1
        return result

# But, it is guaranteed that s is a valid roman numeral in the range [1,3999]
# so I can apply substraction rule when small number comes before big number
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50,
                'C':100, 'D':500, 'M':1000}
        
        result = 0
        for i in range(len(s)):
            curr = roman[s[i]]
            next_val = roman[s[i+1]] if i+1 < len(s) else 0
            
            if curr < next_val:
                result -= curr
            else:
                result += curr
        
        return result

if __name__ == "__main__":
    solution = Solution()
    s ="MCMXCIV"
    result = solution.romanToInt(s)
    print(result)