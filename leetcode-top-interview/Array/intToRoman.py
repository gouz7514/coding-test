# 12. Integer to Roman
# 어찌어찌.. 풀었다...
# 15ms, Beats 19.75%
# class Solution(object):
#     def intToRoman(self, num):
#         s = ''
#         roman=[('M',1000),('D',500),('C',100),('L',50),('X',10),('V',5),('I',1)]

#         while num > 0:
#             i = 0
#             for k,v in roman:
#                 if v <= num:
#                     if str(num)[0] == '9':
#                         s += roman[i+1][0]
#                         s += roman[i-1][0]
#                         num %= roman[i+1][1]
#                     elif str(num)[0] == '4':
#                         s += k
#                         s += roman[i-1][0]
#                         num %= v
#                     else:
#                         ss = k * (num // v)
#                         s += ss
#                         num %= v
#                     break
#                 else:
#                     i += 1
#         return s
        
# Hint by Cluade : 모든 숫자 조합을 미리 리스트에 포함시키기
# 15ms, Beats 19.75%
# class Solution(object):
#     def intToRoman(self, num):
#         s = ''
#         roman=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]

#         while num > 0:
#             for k, v in roman:
#                 if v <= num:
#                     ss = k * (num // v)
#                     s += ss
#                     num %= v
#                     break
#         return s
    
# wow..
# 4ms, Beats 79.56%
class Solution(object):
    def intToRoman(self, num):
        s = ''
        roman=[('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]

        for symbol, value in roman:
            while num >= value:
                s += symbol
                num -= value
        return s

if __name__ == "__main__":
    solution = Solution()
    num = 3749
    result = solution.intToRoman(num)
    print(result)