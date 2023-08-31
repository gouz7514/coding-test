# 시리얼 번호
# https://www.acmicpc.net/problem/1431
# 숫자는 알파벳보다 먼저 온다 (아스키)
# 나의 풀이
# N = int(input())
# guitars = []

# for _ in range(N):
#   guitar = input()
#   numbers = ''.join([char for char in guitar if char.isdigit()])
#   guitars.append([guitar, 0 if numbers == '' else sum(list(map(int, [*numbers])))])

# guitars.sort(key = lambda x: (len(x[0]), x[1], x[0]))
# for guitar in guitars:
#   print(guitar[0])

# 다른 사람의 풀이
N = int(input())
guitars = []

def sum_num(input):
  num = 0
  for x in input:
    if x.isdigit():
      num += int(x)
  return num

for _ in range(N):
  guitars.append(input())

guitars.sort(key = lambda x : (len(x), sum_num(x), x))

for guitar in guitars:
  print(guitar)