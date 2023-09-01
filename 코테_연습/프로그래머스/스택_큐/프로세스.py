# 나의 풀이
# def solution(priorities, location):
#     answer = 0
#     nums = [i for i in range(len(priorities))]
#     arr = [i for i in zip(nums, priorities)]
#     max_v = max(arr, key = lambda x : x[1])[1]
#     result = []

#     while arr:
#         element = arr.pop(0)
#         if max_v > element[1]:
#             arr.append(element)
#         else:
#             result.append(element)
#             if arr:
#                 max_v = max(arr, key = lambda x : x[1])[1]
    
#     for i in range(len(result)):
#         if result[i][0] == location:
#             answer = i + 1
#             break

#     return answer

# 다른 사람의 풀이
def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    while queue:
        element = queue.pop(0)
        if any(element[1] < q[1] for q in queue):
            queue.append(element)
        else:
            answer += 1
            if element[0] == location:
                return answer
    return answer

# 다른 사람의 풀이 2
def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse = True), 0
    print(search)
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            print(i, priority, c, s)
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))