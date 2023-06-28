# Yangjojang of The Year
# https://www.acmicpc.net/problem/11557

# 나의 코드
# import sys

# T = int(sys.stdin.readline())
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     max_school = ''
#     max_drink = 0

#     for _ in range(N):
#         school, drink = sys.stdin.readline().split()
#         drink = int(drink)
#         if drink > max_drink:
#             max_drink = drink
#             max_school = school

#     print(max_school)

## dictionary 쓰는 방법
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    school_dict = {}

    for _ in range(N):
        school, drink = sys.stdin.readline().split()
        school_dict[school] = int(drink)

    sorted_arr = sorted(school_dict.items(), key = lambda x: x[1])
    print(sorted_arr[-1][0])
