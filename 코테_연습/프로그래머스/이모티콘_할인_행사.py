# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 나의 풀이
# 할인율은 10, 20, 30, 40% 만 적용 가능
# 각 할인율이 적용된 이모티콘 가격에 대해 각 users가 구매하게 되는 경우 따지고 maximum 비교
# 실패 케이스는 무엇일까? - 부동소수점 오차?
# 주석 처리된 부분 때문에 틀린다
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    # discounts = [0.9, 0.8, 0.7, 0.6]
    discounts = [10, 20, 30, 40]

    for discount in product(discounts, repeat = len(emoticons)):
        # multiplied = [int(a * b) for a, b in zip(discount, emoticons)]
        multiplied = [int((100 - a) * b / 100) for a, b in zip(discount, emoticons)]
        result = [0, 0]
        
        for user in users:
            current_sum = 0
            for i in range(len(emoticons)):
                current_discount = discount[i]
                if user[0] <= current_discount:
                    current_sum += multiplied[i]
                # if (100 - user[0]) >= current_discount * 100:
                #     current_sum += multiplied[i]
            # 현재 총 구매 비용이 한도 금액 이상이라면 가입
            if current_sum >= user[1]:
                result[0] += 1
            else:
                result[1] += current_sum
                
        if answer[0] == result[0]:
            answer[1] = max(answer[1], result[1])
        elif answer[0] < result[0]:
            answer = result

    return answer

# 다른 사람의 풀이
# 순열을 아래 코드로 쉽게 만들 수 있다
def make_percentage_cases(prev):
    cases = []
    for li in prev:
        for n in [40, 30, 20, 10]:
            cases.append(li + [n])
    return cases

def solution(users, emoticons):
    answer = []

    cases = [[]]  # 가능한 이모티콘별 할인율 케이스들
    for _ in range(len(emoticons)):
        cases = make_percentage_cases(cases)
    print(cases)

    for case in cases:  # 완전 탐색
        result = [0, 0]
        for percentage, price in users:
            cost = 0
            for i in range(len(emoticons)):
                if case[i] >= percentage:  # 희망 할인율 이상이라면 구매
                    cost += emoticons[i] * (100 - case[i]) // 100
            if cost >= price:
                result[0] += 1
            else:
                result[1] += cost
        answer.append(result)
    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

print(solution(users, emoticons))