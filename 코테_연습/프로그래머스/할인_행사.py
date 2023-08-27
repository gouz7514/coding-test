def solution(want, number, discount):
    answer = 0
    dic = dict()
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount) - 10 + 1):
        dic2 = dic.copy()
        for j in range(10):
            if discount[i + j] in dic2:
                dic2[discount[i + j]] = dic2[discount[i + j]] - 1 if dic2[discount[i + j]] > 0 else 0
        if sum(list(dic2.values())) == 0:
            answer += 1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))