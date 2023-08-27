# 나의 풀이
# def solution(n, t, m, p):
#     answer = ''
#     cur_number = 0
#     cur_order = 1
#     dic = {
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }

#     def n_number(n, number):
#         if number < n:
#             return dic[number] if number >= 10 else str(number)
        
#         quot, rem = 0, 0
#         result = ''

#         while number >= n:
#             quot, rem = number // n, number % n
#             result = (dic[rem] if rem >= 10 else str(rem)) + result
#             number = quot
            
#         return (dic[number] if number >= 10 else str(number)) + result
    
#     while len(answer) < t:
#         words = n_number(n, cur_number)

#         for word in words:
#             if cur_order == p:
#                 answer = answer + word
            
#             cur_order += 1
#             if cur_order > m:
#                 cur_order = 1

#             if len(answer) == t:
#                 break

#         cur_number += 1

#     return answer

# 나의 풀이 변형
DIGITS = list('0123456789ABCDEF')

def solution(n, t, m, p):
    answer = ''
    cur_number = 0
    cur_order = 1

    def n_number(n, number):
        if number < n:
            return DIGITS[number]
        
        quot, rem = 0, 0
        result = ''

        while number >= n:
            quot, rem = number // n, number % n
            result = DIGITS[rem] + result
            number = quot
            
        return DIGITS[number] + result
    
    while len(answer) < t:
        words = n_number(n, cur_number)

        for word in words:
            if cur_order == p:
                answer = answer + word
            
            cur_order += 1
            if cur_order > m:
                cur_order = 1

            if len(answer) == t:
                break

        cur_number += 1

    return answer

# 다른 사람의 풀이
# DIGITS = list('0123456789ABCDEF')

# def n_number(number, base):
#     if number < base:
#         return DIGITS[number]
    
#     q, r = divmod(number, base)
#     return n_number(q, base) + DIGITS[r]

# def n_number(number, base):
#     if number < base:
#         return DIGITS[number]
    
#     digits =[]
#     while number > 0:
#         digits.append(DIGITS[number % base])
#         number //= base

#     # 뒤집어서 반환
#     return ''.join(digits[::-1])

# def solution(n, t, m, p):
#     digits =[]
#     number = 0
#     while len(digits) < t * m:
#         digits += list(n_number(number, n))
#         turn += 1
#     return ''.join(digits[p-1::m][:t])

print(solution(16, 16, 2, 2))