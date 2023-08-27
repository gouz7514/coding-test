# 나의 풀이
def solution(elements):
    num_dict = dict()
    arr = elements + elements[:len(elements) - 2]
    cnt = 1
    for i in range(len(elements)):
        for j in range(len(elements)):
            sum_num = sum(arr[j:j+cnt])
            if sum_num not in num_dict:
                num_dict[sum_num] = 1
        cnt += 1
    return len(num_dict.keys())

elements = [7, 9, 1, 1, 4]
print(solution(elements))

# 다른 사람의 풀이
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)