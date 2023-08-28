# https://school.programmers.co.kr/learn/courses/30/lessons/12953
# 나의 풀이 - 정답
# 유클리드 호제법 활용
def solution(arr):
    if len(arr) < 2:
        return arr[0]
    lcm = 0

    # arr을 정렬
    arr.sort()

    def getGcd(x, y):
        x, y = (x, y) if x > y else (y, x)
        r = x % y
        if r == 0:
            return y
        return getGcd(y, r)

    for i in range(len(arr) - 1):
        # 최대공약수 찾기
        gcd = getGcd(arr[i], arr[i + 1]) if lcm == 0 else getGcd(lcm, arr[i + 1])
        # 최소공배수 찾기
        lcm = (arr[i] * arr[i + 1]) // gcd if lcm == 0 else (lcm * arr[i + 1]) // gcd

    return lcm

arr = [2, 6, 8, 14]
print(solution(arr))