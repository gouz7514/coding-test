# https://school.programmers.co.kr/learn/courses/30/lessons/134239
# 나의 풀이 - 정답
def solution(k, ranges):
    answer =[]
    graph = [k] # 꺾은선 그래프
    arr = [] # 우박수열

    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        graph.append(k)

    for i in range(len(graph) - 1):
        result = (graph[i] + graph[i + 1]) / 2
        arr.append(result)

    for r in ranges:
        a, b = r

        if b <= 0:
            b = len(arr) + b

        if a > b:
            answer.append(-1.0)
            continue

        answer.append(sum(arr[a:b]) if a != b else 0.0)

    return answer

# 다른 사람의 풀이
def solution(k, ranges):
    answer = []
    arr = [k]

    while k > 1:
        if not k % 2: k //= 2
        else: k = k * 3 + 1
        arr.append(k)

    area = [0]
    for i in range(len(arr) -1):
        area.append(area[-1] + (arr[i] + arr[i + 1]) / 2)
    print(area)

    for a, b in ranges:
        if a >= len(area) or b -1 < -len(area): answer.append(-1)
        elif area[b - 1] - area[a] < 0: answer.append(-1)
        else: answer.append(area[b - 1] - area[a])
        print(a, b, answer)

    return answer

k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(k, ranges))