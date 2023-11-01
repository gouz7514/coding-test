# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729
# 골드 5
# 절차지향적 사고로 접근하면 해결하기 힘들다
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
# n = int(input())
# cnt = 0
# answer = []

# def move(start, to):
#   # print(start, to)
#   answer.append((start, to))
#   global cnt
#   cnt += 1

# def hanoi(N, start, to, via):
#   if N == 1:
#     move(start, to)
#   else:
#     hanoi(N - 1, start, via, to)
#     move(start, to)
#     hanoi(N - 1, via, to, start)

# hanoi(n, '1', '3', '2')
# print(cnt)
# for i in answer:
#   print(*i)

n = int(input())

def move(a, b, n):
  if n == 1:
    print(a, b)
    return
  move(a, 6 - a - b, n - 1)
  print(a, b)
  move(6 - a - b, b, n - 1)

print((1 << n) - 1)
move(1, 3, n)