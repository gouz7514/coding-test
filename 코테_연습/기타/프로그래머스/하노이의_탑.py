# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 참고 링크
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
def solution(n):
    answer = []
    start, via, destination = 1, 2, 3

    def hanoi(n, start, via, destination):
        if n == 1:
            answer.append([start, destination])
        else:
            hanoi(n - 1, start, destination, via)
            answer.append([start, destination])
            hanoi(n - 1, via, start, destination)

    hanoi(n, start, via, destination)

    return answer

print(solution(3))