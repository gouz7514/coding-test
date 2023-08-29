# dfs
# 나의 풀이
# dfs로는 시간 초과가 난다...
# from collections import Counter

# def solution(orders, course):
#     words = set()
#     answer = []

#     for order in orders:
#         for o in order:
#             words.add(o)

#     words = sorted(list(words))

#     def dfs(words, length, arr, result):
#         if len(arr) == length:
#             result.append(arr)
#             return
        
#         for i in range(len(words)):
#             dfs(words[i + 1:], length, arr + words[i], result)

#     for c in course:
#         combs = []
#         dfs(words, c, '', combs)

#         counter = Counter()
#         for comb in combs:
#             cnt = 0
#             for order in orders:
#                 for c in comb:
#                     if c not in order:
#                         break
#                 else:
#                     cnt += 1
#             counter[comb] = cnt
      
#         if len(counter) == 0:
#             continue
        
#         most_ordered = counter.most_common()
#         answer += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

#     return sorted(answer)

# # 다른 사람의 풀이
# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]

# 다른 사람의 풀이 2
import sys

def dict_update(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

def order_update_rec(d, s, i, rst):
    if i == len(s):
        dict_update(d, rst)
    else:
        order_update_rec(d, s, i+1, rst)
        order_update_rec(d, s, i+1, rst+s[i])

def solution(orders, course):
    order_dict = {}
    for order_i in range(len(orders)):
        orders[order_i] = sorted(orders[order_i])
        order_update_rec(order_dict, orders[order_i], 0, "")
    
    print(order_dict)

    result = []
    max_v = [ 0 for _ in range(len(course)) ]
    max_key = [ [] for _ in range(len(course)) ]
    for key in order_dict:
        for course_i, course_n in enumerate(course):
            print(key, course_i, course_n)
            if len(key) == course_n:
                if order_dict[key] > max_v[course_i]:
                    max_v[course_i] = order_dict[key]
                    max_key[course_i] = [key]
                elif order_dict[key] == max_v[course_i]:
                    max_key[course_i].append(key)
    for i, v in enumerate(max_v):
        if v >= 2:
            result += max_key[i]

    return sorted(result)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))