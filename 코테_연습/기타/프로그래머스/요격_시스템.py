# 요격 시스템
# 최소 미사일 발사 횟수 찾아야 한다
# 나의 풀이
# def solution(targets):
#     answer = 0

#     targets.sort(key=lambda x: (x[0], x[1]))
#     x, y = 0, 0

#     for target in targets:
#         if target[0] >= x:
#             if target[0] >= y:
#                 answer += 1
#                 x, y = target[0], target[1]
#             else:
#                 x, y = max(x, target[0]), min(y, target[1])

#     return answer

# for문을 돌면서 
# 다른 사람의 풀이
# for문을 돌면서 정렬된 미사일 좌표 s가 이전 미사일 e와 같거나 큰 경우는 같이 요격할 수 없으므로 정답을 +1하고 e 좌표를 업데이트한다
def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))