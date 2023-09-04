# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 나의 풀이
# counter 사용해서 value 내림차순 정렬, k 이상될때까지 answer++
# counter를 안 쓰면? dict 만들면 된다
# from collections import Counter

# def solution(k, tangerine):
#     answer = 0
#     total = 0
#     counter = Counter(tangerine).most_common()

#     for i, c in counter:
#         if total < k:
#             total += c
#             answer += 1

#     return answer

def solution(k, tangerine):
    answer = 0
    total = 0
    dic = dict()

    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
    
    sorted_dict = sorted(dic.items(), key = lambda x: x[1], reverse=True)
    
    for i, c in sorted_dict:
        if total < k:
            total += c
            answer += 1

    return answer

# 다른 사람의 풀이
# 굳이 total을 쓰지 않고 k를 활용해도 된다
from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine).most_common()

    for i, c in counter:
        k -= c
        answer += 1
        if k <= 0:
            break

    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

