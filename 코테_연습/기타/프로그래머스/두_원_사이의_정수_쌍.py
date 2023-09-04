# 작은 원 위에 있을 수도 있으니까 작은 원 위의 점은 제외해야 한다
def solution(r1, r2):
    answer = 0
    cnt_r1, cnt_r2 = 0, 0
    max_r1, max_r2 = r1 - 1, r2 - 1

    for i in range(1, r1):
        while i ** 2 + max_r1 ** 2 >= r1 ** 2:
            max_r1 -= 1
        cnt_r1 += max_r1

    for i in range(1, r2):
        while i ** 2 + max_r2 ** 2 > r2 ** 2:
            max_r2 -= 1
        cnt_r2 += max_r2

    answer = 4 * ((r2 - r1 + 1) + (cnt_r2 - cnt_r1))

    return answer

r1, r2 = 5, 10
print(solution(r1, r2))
